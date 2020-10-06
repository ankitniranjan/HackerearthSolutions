# Write your code here

def Steps(n):
    if n % 5 == 0:
        return n//5
    return n//5 + 1

if __name__ == '__main__':
    print(Steps(int(input())))
