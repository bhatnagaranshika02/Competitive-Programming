def power(n):
    n=n/2
    if n==2:
        return True
    elif n>2:
        return power(n)
    else:
        return False




for i in range(int(input())):
    n = int(input())
    if power(n):
        print("Yes")
    else:
        print("No")
    
44
