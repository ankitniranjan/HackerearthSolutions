# Write your code here

def Maze(string):
    pos = [0 ,0]
    for char in string:
        if char == 'L':
            pos[0] -= 1
        elif char == 'R':
            pos[0] += 1
        elif char == 'U':
            pos[1] += 1
        else:
            pos[1] -= 1
    return pos
	
if __name__ == '__main__':
    print(*Maze(input()))
