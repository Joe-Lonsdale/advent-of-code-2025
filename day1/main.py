import math

filename = "input.txt"

file = open(filename, "r")

def main():
    pointer = 0
    zero_count = 0
    for line in file:
        negated = False
        prev_pointer = pointer
        print(f"POINTER: {pointer}")
        print(f"INSTRUCTION: {line}")
        if len(line) == 0:
            break
        if line[0] == 'L':
            pointer -= int(line[1:])
        else:
            pointer += int(line[1:])
        while pointer > 100:
            zero_count += 1
            pointer -= 100
        while pointer < 0:
            if prev_pointer == 0 and not negated:
                zero_count -= 1
                negated = True
            zero_count += 1
            pointer += 100
        pointer %= 100
        if pointer == 0:
            zero_count += 1
        print(f"ZERO COUNT: {zero_count}")
    print(zero_count)


if __name__ == "__main__":
    main()
