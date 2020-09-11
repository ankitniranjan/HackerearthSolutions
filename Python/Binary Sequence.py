#		Given four integers x,y,a and b. Determine if there exists a binary string having x 0's and y 1's such that the total number of subsequences equal to the sequence "01" in it is a and the total number of subsequences equal to the sequence "10" in it is b.

#		A binary string is a string made of the characters '0' and '1' only.

#		A sequence a is a subsequence of a sequence b if can be obtained from b by deletion of several (possibly, zero or all) elements.



# Write your code here
def isPossible(x, y, a, b) : 
      
    if (x * y == a + b) : 
        return True
  
    return False 
   
if __name__ == "__main__" :  
    n = int(input())

    for i in range(n):
        x,y,a,b = list(map(int, input().split())) 
    
        if (isPossible(x, y, a, b)) : 
            print("Yes")  
        else : 
            print("No")  
