for i in range(int(input())):
    n = int(input())
    a=list(map(int,input().split()))
    l=[]
    for i in range(len(a)):
        if a.count(a[i]) == 1:
            l.append(a[i])
    print(*l)
