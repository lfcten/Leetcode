"""
模板匹配
<[播]放|来>[一|几]<首|曲|个>@{singer}的<歌[曲]|[流行]音乐>
来几首@{singer}的歌
"""
import re
import sys

if __name__ == "__main__":
    info = sys.stdin.readline().strip()
    sentence = sys.stdin.readline().strip()
    pattern = re.compile(info.replace("<", "(").replace(">", ")").replace("[", "(").replace("]", ")?"))
    a = re.search(pattern, sentence)
    if a:
        print(1)
    else:
        print(0)
