for i in range(int(input())):
    a=list(map(int,input().split()))
    sum = int(input())
    l=[]
    summ = 0
    l1=[]
    start=0
    flag=0
    for i in range(len(a)):
        summ+=a[i]
        l.append(i)
        while summ > sum:
            summ -=a[start]
            l.remove(start)
            start+=1
        if summ == sum:
            flag=1
            break
    if flag ==1:
        print(l[0],l[-1])
    else:
        print('-1')


