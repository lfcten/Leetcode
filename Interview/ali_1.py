import collections
import sys

if __name__ == "__main__":
    """
    线上提交未考虑相同前缀的entity同时出现的情况，还是A了。。
    """
    info = sys.stdin.readline().strip()
    sentence = sys.stdin.readline().strip()
    dic = collections.defaultdict(list)
    entitySet = info.split(";")
    query = set()
    for entity in entitySet:
        prop, ents = entity.split("_")
        for ent in ents.split("|"):
            query.add(ent)
            dic[ent].append(prop)

    query = sorted(list(query), key=len, reverse=True)

    for ind, word in enumerate(query):
        if word in sentence:
            sentence = sentence.replace(word, " " + "$" + str(ind) + "$" + "/" + ",".join(sorted(dic[word])) + " ")
    for ind, word in enumerate(query):
            sentence = sentence.replace("$" + str(ind) + "$", word)
    print(sentence.strip())
