class Solution:
    # @return a string
    def longestPalindrome(self, s):
        if len(s) <= 1:
            return s
        maxLen = 1
        start = 0
        for i in range(1, len(s)):
            if i - maxLen >= 1 and s[i - maxLen - 1:i - maxLen + maxLen // 2] == s[i - maxLen // 2:i + 1][::-1]:
                start = i - maxLen - 1
                maxLen += 2
                continue

            if i - maxLen >= 0 and s[i - maxLen:i - maxLen // 2] == s[i - (maxLen - 1) // 2:i + 1][::-1]:
                start = i - maxLen
                maxLen += 1
        return s[start:start + maxLen]


# sample 59 ms submission
class Solution1:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        size = len(s)
        if size <= 1 or s == s[::-1]:
            return s
        start, max_len = 0, 1
        for idx in range(1, size):
            add2 = s[idx - max_len - 1: idx + 1]
            if idx - max_len - 1 >= 0 and add2 == add2[::-1]:
                start = idx - max_len - 1
                max_len += 2
                continue
            add1 = s[idx - max_len: idx + 1]
            if add1 == add1[::-1]:
                start = idx - max_len
                max_len += 1
        return s[start: (start + max_len)]

#sample 8 ms submission
class Solution3:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        self.max_len = 1
        self.ind = 0
        self.n = len(s)
        if self.n <= 1:
            return s

        i = 0
        while i < self.n:
            i = self.manacher(s, i)
            i += 1
        return s[self.ind: self.ind + self.max_len]


    def manacher(self, s, pos):
        i, j = pos - 1, pos
        while j < self.n - 1 and s[j] == s[j + 1]:
            j += 1
        nextCenter = j

        while i >= 0 and j < self.n and s[i] == s[j]:
            i -= 1
            j += 1

        if j - i - 1 > self.max_len:
            self.max_len = j - i - 1
            self.ind = i + 1

        return nextCenter
