# Write your code here

def Palindrom(string):
    end = len(string)
    med = end // 2
    for i in range(med):
        if string[i] == string[end-i-1]:
            continue
        return "NO"
    return "YES"

if __name__ == '__main__':
    print(Palindrom(input()))
