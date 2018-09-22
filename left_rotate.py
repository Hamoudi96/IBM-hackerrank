def rotLeft(a, d):
    r_list = []
    for i in range(d,len(a)):
        r_list.append(a[i])
    for i in range(0,d):
        r_list.append(a[i])
    return r_list

a=[1,2,3,4,5]
print(rotLeft(a, 4))