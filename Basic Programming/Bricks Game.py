# Write your code here

def Bricks(N):
    i = 1
    while True:
        if N > i*3:
            N = N - i*3
            i += 1
            continue
        else:
            if N < i:
                return "Patlu"
            else:
                return "Motu"

if __name__ == '__main__':
    N = int(input())
    print(Bricks(N))
