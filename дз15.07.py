def polindrom(s):
    a = []
    for x in s:
        a.append(x)
    b = []
    for i in range(len(a)-1, -1, -1):
        b.append(a[i])
    if b==a:
        print('True')
    else:
        print('False')

polindrom(input())