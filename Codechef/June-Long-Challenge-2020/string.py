def pairs(a):
    count=0
    i=0
    while i<len(a)-1:
        if a[i]=='x':
            if a[i+1]  == 'y':
                count+=1
                i+=1
        elif a[i]=='y':
            if a[i+1] == 'x':
                count+=1
                i+=1
        i+=1
    return count

if __name__ == "__main__":
    for j in range(int(input())):
                   a=input()
                   print(pairs(a)) 
