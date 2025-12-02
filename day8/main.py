import math

filename = "input.txt"

file = open(filename, "r")

def main():
    input = [l.split("-") for l in file.readline().split(",")]

if __name__ == "__main__":
    main()
