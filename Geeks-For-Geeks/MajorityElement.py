
for i in range(int(input())):
    n = int(input())
    a=list(map(int,input().split()))
    l=[]
    count=0
    b=[]
    for i in range(len(a)):
        if a[i] not in l:
            l.append(a[i])
            if a.count(a[i]) > (n/2) :
                b.append(a[i])
                count = 1

    if count == 0:
        print("-1")
    else:
        print(*b)
