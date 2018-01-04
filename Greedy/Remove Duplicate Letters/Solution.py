from collections import defaultdict
class Solution:
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        #
        idx = {c: i for i, c in enumerate(s)}
        result = ''
        for i, c in enumerate(s):
            print(result)
            if c not in result:
                while c < result[-1:] and i < idx[result[-1]]:
                    result = result[:-1]
                result += c
        return result



class Solution1:
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        total_count = defaultdict(int)
        for c in s:
            total_count[c] += 1

        stack = ['A']
        visited = set()
        for c in s:
            total_count[c] -= 1
            if c in visited:
                continue
            while stack[-1] > c:
                if total_count[stack[-1]] == 0:
                    break
                visited.remove(stack.pop())
            stack.append(c)
            visited.add(c)
        return ''.join(stack[1:])


