import math

filename = "input.txt"

file = open(filename, "r")

def main():
    fresh = []
    available = []
    for l in [s.replace("\n","") for s in file.readlines()]:
        if "-" in l:
            fresh.append([int(s) for s in l.split("-")])
        elif len(l) != 0:
            available.append(int(l))

    # part 1
    fresh_count = 0
    for a in available:
        for f in fresh:
            if a in range(f[0], f[1]+1):
                fresh_count += 1
                break
    print(f"part 1: {fresh_count}")

    # part 2
    sorted_ranges = sorted(fresh,key=lambda x: x[0])
    changed = True
    while changed:
        changed = False
        for i,r in enumerate(sorted_ranges[:-1]):
            if sorted_ranges[i][1] >= sorted_ranges[i+1][0] - 1:
                sorted_ranges[i][1] = max(sorted_ranges[i][1], sorted_ranges[i+1][1])
                sorted_ranges.remove(sorted_ranges[i+1])
                changed=True
                break
    print(sum([r[1] - r[0] + 1 for r in sorted_ranges]))


    
if __name__ == "__main__":
    main()
