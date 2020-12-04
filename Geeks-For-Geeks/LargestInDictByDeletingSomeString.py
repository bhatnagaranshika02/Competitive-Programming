def isSubSequence(str1, str2): 
  
    m = len(str1); 
    n = len(str2); 
  
    j = 0; 
    i = 0; 
    while (i < n and j < m): 
        if (str1[j] == str2[i]): 
            j += 1; 
        i += 1; 
    return (j == m); 

def findLongestString(dict1, str1): 
    result = ""; 
    length = 0; 
  
    for word in dict1: 
          
        if (length < len(word) and isSubSequence(word, str1)): 
            result = word; 
            length = len(word); 
  
    return result; 
  
  
for i in range(int(input())):
    n =int(input())
    dict1=list(input().split())
    str1 = input()
    print(findLongestString(dict1, str1)); 
