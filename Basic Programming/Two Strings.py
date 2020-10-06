# Write your code here

def Isequal(string1,string2):
    if sorted(string1) == sorted(string2):
        return "YES"
    return "NO"


if __name__ == '__main__':
    N = int(input())

    for i in range(N):
        string1, string2 = input().split()
        print(Isequal(string1, string2))
