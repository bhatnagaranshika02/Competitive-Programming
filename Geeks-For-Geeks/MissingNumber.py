for i in range(int(input())):
    n = int(input())
    l=list(map(int,input().split()))
    t = (n+1)*(n+2)/2
    print(int(t-sum(l)))
