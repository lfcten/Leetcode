import collections


class Solution:
    def findRotateSteps(self, ring, key):
        """
        :type ring: str
        :type key: str
        :rtype: int
        """
        m, n = len(ring), len(key)

        def dist(i, j):
            return min(abs(i - j), m - abs(i - j))

        dic = collections.defaultdict(list)

        for i in range(m):
            dic[ring[i]] += i,

        state = {0: 0}
        for k in key:
            next_state = {}
            for j in dic[k]:
                next_state[j] = float("inf")
                for i in state:
                    next_state[j] = min(next_state[j], dist(i, j) + state[i])
            state = next_state

        return min(state.values()) + m


class Solution1:
    def findRotateSteps(self, ring, key):
        """
        :type ring: str
        :type key: str
        :rtype: int
        """

        R = len(ring)
        K = len(key)

        map_R = {}
        for i, x in enumerate(ring):
            map_R[x] = map_R.get(x, ()) + (i,)

        # DP
        #	f(i,j): min. step to spell key[j:] starting from ring[i]
        # progress:
        #	f(i,j) = INF,								if ring[i] != key[j]
        #		   = min_k { min(abs(i-k), abs(i+R-k), abs(i-R-k)) + 1 + f(k,j+1) | ring[k] == key[j+1] }

        f = [[0] * K for _ in range(R)]

        # f(*,K-1)
        for i in map_R[key[K - 1]]:
            f[i][K - 1] = 0

        for j in range(K - 1)[::-1]:
            for i in map_R[key[j]]:

                # sanity check
                if key[j] == key[j + 1]:
                    f[i][j] = 1 + f[i][j + 1]
                    continue

                f[i][j] = min(
                    [min(abs(i - k), abs(i + R - k), abs(i - R - k)) + 1 + f[k][j + 1] for k in map_R[key[j + 1]]])

        return min([min(k, R - k) + 1 + f[k][0] for k in map_R[key[0]]])


if __name__ == "__main__":
    cls = Solution()
    print(cls.findRotateSteps("godding", "og"))
