for i in range(int(input())):
    n = int(input())
    a=list(map(int,input().split()))
    start=0
    flag=0
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if (a[i]**2) + (a[start]**2) == (a[j]**2):
                flag=1
            else:
                start+=1
    if flag==1:
        print("Yes")
    else:
        print("No")
