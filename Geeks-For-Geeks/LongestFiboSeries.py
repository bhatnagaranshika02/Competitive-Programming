for i in range(int(input())):
    n = int(input())
    a =list(map(int,input().split()))
    start = 1
    third =2
    l=[]
    l1=[]
    for i in range(len(a)):
        if a[i] + a[start] == a[third]:
            l.append(a[i])
            start = 1
            third = 1

    
