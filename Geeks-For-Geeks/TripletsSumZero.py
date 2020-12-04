from itertools import combinations
for i in range(int(input())):
    n = int(input())
    a=list(map(int,input().split()))
    count=0
    b = set(combinations(a,3))
    b= list(b)
    for i in b:
        if sum(i) == 0:
            count=  1
            break
        else:
            pass
    if count== 1:
        print('1')
    else:
        print(0)
