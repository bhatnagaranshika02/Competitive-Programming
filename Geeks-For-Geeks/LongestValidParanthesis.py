for i in range(int(input())):
    a= input()
    count=0
    for i in range(len(a)):
        if a[i] == '(':
            if a[i+1] ==')':
                count+=2
        else:
            pass
    print(count)
