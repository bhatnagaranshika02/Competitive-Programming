

def PriceControl(l,k):
    summ=sum(l)
    sum2=0
    for i in range(len(l)):
        if l[i] <k:
            sum2+=l[i]
        else:
            sum2+=k
    return abs(summ-sum2)


if __name__ in '__main__':
    for i in range(int(input())):
        n,k = map(int,input().split())
        l=list(map(int,input().split()))
        print(PriceControl(l,k))
