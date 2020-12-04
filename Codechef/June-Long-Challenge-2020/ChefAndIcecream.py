def chefIcecream(cust_money):
    chef_money=[]
    flag='YES'
    for i in range(len(cust_money)):
        if cust_money[i]==5:
            chef_money.append(cust_money[i])
        elif cust_money[i]==10 and (5 in chef_money):
                chef_money.remove(5)
                chef_money.append(cust_money[i])
        elif cust_money[i]==15 and (10 in chef_money or chef_money.count(5)>1):
            if 10 in chef_money:
                chef_money.remove(10)
            else:
                chef_money.remove(5)
                chef_money.remove(5)
        else:
            flag='NO'
            break
                
    return flag

for i in range(int(input())):
    n=int(input())
    cust_money=list(map(int,input().split()))
    print(chefIcecream(cust_money))









    
