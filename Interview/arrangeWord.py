import collections
"""
判断一个数组中的字符串能够排成首尾相连的形式
"""

def isValid(words):
    xx = set()  # 记录首尾相同的字母
    first = collections.defaultdict(int)
    last = collections.defaultdict(int)
    for word in words:
        if word[0] == word[-1]:
            xx.add(word[0])
        else:
            first[word[0]] += 1
            last[word[-1]] += 1

    flag1 = ''
    flag2 = ''
    for key, value in first.items():
        if last[key] == value:
            if key in xx:
                xx.remove(key)
            continue
        elif last[key] == value + 1:
            if not flag1:
                flag1 = key
                if key in xx:
                    xx.remove(key)
            else:
                return False
        elif last[key] == value - 1:
            if not flag2:
                flag2 = key
                if key in xx:
                    xx.remove(key)
            else:
                return False
        else:
            return False

    return False if xx else True


if __name__ == "__main__":
    print(isValid(['ab', 'ab', 'ba']))
    print(isValid(['ab', 'ba', 'bb']))
    print(isValid(['ab', 'ab', 'bbb', 'bb', 'ba']))
    print(isValid(['ab', 'bab', 'aaa', 'aab']))
    print(isValid(['aaaa', 'bbbbbbb', 'ccccccc', 'aaaacccc']))
