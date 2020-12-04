for i in range(int(input())):
    n = int(input())
    a=list(map(int,input().split()))
    l=[]
    for i in range(0,len(a)):
        for j in range(i+1,len(a)):
            if a[j] > a[i]:
                l.append(a[j])
        else:
            l.append(-1)
            break

    print(*l)
