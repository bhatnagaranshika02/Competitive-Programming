for i in range(int(input())):
               n,m = map(int,input().split())
               l=list(map(int,input().split()))
               b=[]
               i=-1
               count=0
               l.sort()
               while count!=m:
                   j=l.remove(i)
                   b.append(j)
                   count+=1
                   
                   i-=1
               print(*b)
               
