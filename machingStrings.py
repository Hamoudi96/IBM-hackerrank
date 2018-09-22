def matchingStrings(strings, queries):
    dic = {}
    for s in strings:
        if s in dic:
            num=dic[s]+1
            dic[s]=num
        else:
            dic[s]=1
    matchingStrings=[]
    for q in queries:
        if q in dic:
            matchingStrings.append(dic[q])
        else:
            matchingStrings.append(0)
    return matchingStrings

strings = ['a','b','c','a','c','a']
queries = ['a','c','d']
print(matchingStrings(strings, queries))

