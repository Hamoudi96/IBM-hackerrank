def twoStrings(s1, s2):
    for s in s1:
        if s in s2:
            return "YES"
    return "NO"

s1='hi'
s2='li'
print(twoStrings(s1, s2))
