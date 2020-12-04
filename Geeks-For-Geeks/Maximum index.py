for k in range(int(input())):
    n=int(input())
    a = list(map(int,input().split()))
    maxx=-1
    for i in range(len(a)):
        for j in range(i,len(a)):
            if a[i] <= a[j]:
                
                g = j-i
                
                if g>maxx:
                    maxx = g
    print(maxx)
