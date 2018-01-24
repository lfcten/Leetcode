"""
# 60ms
def de_bruijn(k, n):
    try:
        # let's see if k can be cast to an integer;
        # if so, make our alphabet a list
        _ = int(k)
        alphabet = list(map(str, range(k)))

    except (ValueError, TypeError):
        alphabet = k
        k = len(k)

    a = [0] * k * n
    sequence = []
    def db(t, p):
        if t > n:
            if n % p == 0:
                sequence.extend(a[1:p + 1])
        else:
            a[t] = a[t - p]
            db(t + 1, p)
            for j in range(a[t - p] + 1, k):
                a[t] = j
                db(t + 1, t)
    db(1, 1)
    return "".join(alphabet[i] for i in sequence) // "".join(alphabet[i] for i in sequence + sequence[: n-1])
"""



# 99ms
class Solution:
    def crackSafe(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        ans = "0" * (n - 1)
        visits = set()
        for x in range(k ** n):
            current = ans[-n + 1:] if n > 1 else ''
            for y in range(k - 1, -1, -1):
                if current + str(y) not in visits:
                    visits.add(current + str(y))
                    ans += str(y)
                    break
        return ans

# 71ms
import collections
class Solution1:
    def crackSafe(self, n, k):
        toVisit = collections.defaultdict(lambda: list(map(str, range(k))))
        toVisit["0" * (n - 1)] = list(map(str, range(1, k)))
        ans = "0" * n
        while True:
            print(ans)
            cur = ans[len(ans) - n + 1:]
            print(cur)
            if not toVisit[cur]: return ans
            ans += toVisit[cur].pop()


if __name__ == "__main__":
    cls = Solution1()
    cls.crackSafe(2, 3)