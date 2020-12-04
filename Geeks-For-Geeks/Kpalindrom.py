for i in range(int(input())):
    a,n = input().split()
    print(a)
    n = int(n)
    count=0
    b = a[:]
    if a == a[::-1]:
        count+=1
        
    else:
        for i in range (len(a)):
            a=list(a)
            a=a.remove(a[i])
            print(a)
            if a == a[::-1]:
                count+=1
            else:
                a=' '.join(b)    
    if count == n:
        print('1')
    else:
        print('0')
        
