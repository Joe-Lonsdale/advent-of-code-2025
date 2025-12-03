import math

filename = "input.txt"

file = open(filename, "r")

def get_biggest_jolts(num_batteries, bank):
    if(num_batteries == 1):
        return sorted(bank)[-1]
    if(num_batteries == len(bank)):
        return bank
    max = 0
    max_i = 0
    for i in range(len(bank) - num_batteries + 1):
        if (int(bank[i]) > max):
            max = int(bank[i])
            max_i = i
    return f'{bank[max_i]}{get_biggest_jolts(num_batteries-1, bank[max_i+1:])}'

def main():
    input = [l.replace("\n","") for l in file.readlines()]
    # part 1
    p1_jolts = 0
    for line in input:
        max = 0
        for a in range(len(line)-1):
            for b in range(1,len(line)-a):
                this_jolts = int(f'{line[a]}{(line[int(b+a)])}')
                if(this_jolts > max):
                    max = this_jolts
        p1_jolts += max
    print(f"part 1: {p1_jolts}")

    # part 2
    p2_jolts = 0
    for line in input:
        p2_jolts += int(get_biggest_jolts(12, line))
    print(f"part 2: {p2_jolts}")

if __name__ == "__main__":
    main()
