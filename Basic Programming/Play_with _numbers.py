# Write your code here

n,q = map(int,input().split())
arr = list(map(int,input().split()))

for i in range(1,len(arr)):
    arr[i] = arr[i] + arr[i-1]

for _ in range(q):
    l,r = map(int,input().split())

    if l==1:
        sum1 = arr[r-1]
        avg = sum1//(r-l+1)
        print(avg)
    else:
        sum1 = arr[r-1] - arr[l-2]
        avg = sum1//(r-l+1)
        print(avg)
