#python3

# Write your code here
def Divisible(arr,N):
    res = []
    half = N//2
    for i in range(half):
        res.append(arr[i][0])
    for i in range(half,N):
        res.append(arr[i][-1])
    res = int(''.join(res))
    if res%11 == 0:
        return "OUI"
    return "NON"

if __name__  == '__main__':
    N = int(input())
    arr = [x for x in input().split()]
    print(Divisible(arr,N))
