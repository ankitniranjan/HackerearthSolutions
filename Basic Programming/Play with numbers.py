# Write your code here

def Mean(arr,l,h):
    mean = (l+h)//2
    i = 0
    while arr[i] < mean:
        i += 1
    if arr[i+1] == mean:
        return arr[i+1]
    return arr[i]

if __name__ == '__main__':
    n, T = map(int, input().split())
    arr = [int(x) for x in input().split()]
    for _ in range(T):
        l,h = map(int, input().split())
        print(Mean(arr,l,h))
