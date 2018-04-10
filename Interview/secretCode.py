import bisect

"""
在线用的是python2.7
竟然忘了python2.7 float运算需要 * 1.0
提交了一个错答案，过了8/9 哈哈
"""
def main(num, secretCode):
    secretCode.sort()
    if num == 0:
        return secretCode[0]
    total = sum(secretCode)
    for i in range(num - 1):
        target = total / (num - i)
        ind = bisect.bisect_left(secretCode, target)
        if secretCode[ind] == target:
            val = secretCode.pop(ind)
        elif abs(secretCode[ind] - target) >= abs(secretCode[ind - 1] - target):
            val = secretCode.pop(ind - 1)
        else:
            val = secretCode.pop(ind)
        total -= val
    return secretCode[0]


if __name__ == "__main__":
    print(main(4, [1, 2, 7, 100]))
    print(main(4, [3, 4, 5, 2]))
    print(main(3, [1, 4, 10000]))
