# Write your code here

def Decide(l,p):
    if l <= 23 and p >= 500 and p <= 1000:
        return "Take Medicine"
    return "Don't take Medicine"

if __name__ == '__main__':
    l, p = map(int, input().split())
    print(Decide(l,p))
