class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(buildings) == 0:
            return []

        if len(buildings) == 1:
            return [[buildings[0][0], buildings[0][2]], [buildings[0][1], 0]]

        mid = len(buildings) // 2
        left = self.getSkyline(buildings[:mid])
        right = self.getSkyline(buildings[mid:])

        return self.merge(left, right)

    def merge(self, left, right):
        output = [[0, 0]]
        i, j, m, n = 0, 0, len(left), len(right)
        ly, ry = -1, -1
        while i < m and j < n:
            ansx = -1
            ansy = -1
            if left[i][0] < right[j][0]:
                ly = left[i][1]
                ansx = left[i][0]
                ansy = max(ly, ry)
                i += 1
            elif left[i][0] > right[j][0]:
                ry = right[j][1]
                ansx = right[j][0]
                ansy = max(ly, ry)
                j += 1
            elif left[i][0] == right[j][0]:
                ly = left[i][1]
                ry = right[j][1]
                ansx = left[i][0]
                ansy = max(ly, ry)
                i += 1
                j += 1
            # ansx - the one that comes first in x-axis
            # ansy - the tallest height that is 'overshadowing' current point
            if ansx != -1 and output[-1][1] != ansy:
                # if the taller point is already dominating, the ansx will not appear in silhouette
                output.append([ansx, ansy])

        while i < m:
            output.append(left[i][:])
            i += 1

        while j < n:
            output.append(right[j][:])
            j += 1
        return output[1:]


class Solution1:
    def getSkyline(self, buildings):
        events = sorted([(L, -H, R) for L, R, H in buildings] + list({(R, 0, None) for _, R, _ in buildings}))
        res, hp = [[0, 0]], [(0, float("inf"))]
        for x, negH, R in events:
            while x >= hp[0][1]:
                heapq.heappop(hp)
            if negH:
                heapq.heappush(hp, (negH, R))
            if res[-1][1] + hp[0][0]:
                res += [x, -hp[0][0]],
        return res[1:]


class Solution3:
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        skyline = []
        # 重合点
        positions = set([b[0] for b in buildings] + [b[1] for b in buildings])

        # use heapq to generate priority queue, use empty list initialize
        cur = []

        i = 0
        num = len(buildings)
        for pos in sorted(positions):
            while i < num and buildings[i][0] <= pos:
                heapq.heappush(cur, (-buildings[i][2], buildings[i][1]))
                i += 1

            while cur and cur[0][1] <= pos:
                heapq.heappop(cur)

            height = 0
            if cur:
                height = -cur[0][0]

            if not skyline or skyline[-1][1] != height:
                skyline.append([pos, height])

        return skyline
