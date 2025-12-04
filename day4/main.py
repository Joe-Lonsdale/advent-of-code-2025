import math

filename = "input.txt"

file = open(filename, "r")

def main():
    input = [[1 if w == '@' else 0 for w in l.replace("\n","")] for l in file.readlines()]
    accessible = 0
    width = len(input[0])
    height = len(input)
    accessible_indices = []
    first = True
    while len(accessible_indices) != 0 or first:
        if first:
            first = False
        else:
            for y,x in accessible_indices:
                input[y][x] = 0
            accessible += len(accessible_indices)
            accessible_indices = []
        for y in range(height):
            for x in range(width):
                neighbours = 0
                if not input[y][x]: continue
                for y_i in range(-1,2):
                    curr_y = y + y_i
                    for x_i in range(-1,2):
                        curr_x = x + x_i
                        if curr_y == y and curr_x == x: continue
                        if curr_y >= 0 and curr_y < height and curr_x >= 0 and curr_x < width and input[curr_y][curr_x]:
                            neighbours += 1
                if neighbours < 4:
                    accessible_indices.append([y,x])
    print(accessible)


if __name__ == "__main__":
    main()
