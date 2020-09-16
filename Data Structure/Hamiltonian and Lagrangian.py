#Logic => We need to find all the lements which are greater or equal to all the elements
			placed right side of it.
			

# Write your code here
n = int(input())
arr = [int(x) for x in input().split()]
result = []

for i in range(n-1):
    current = arr[i]
    count = 0
    for j in range(i+1,n):
        if current >= arr[j]:
            count += 1
        else:
            break
    if count == n-i-1:
        result.append(current)
result.append(arr[n-1])     #Always included

print(*result, sep=' ')
