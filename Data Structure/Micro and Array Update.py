T = int(input())
for i in range(T):
    N,K = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]
    
    diff = K - min(arr)

    if diff>0:
        print(diff)
    else:
        print(0)
