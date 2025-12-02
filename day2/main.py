import math

filename = "input.txt"

file = open(filename, "r")

def main():
    input = [l.split("-") for l in file.readline().split(",")]
    invalid_ids = []
    for a,b in input:
        pointer = int(a)
        while pointer <= int(b):
            pointer_str = str(pointer)
            for x in range(1, len(pointer_str)):
                if len(pointer_str) % x == 0:
                    chunks = int(len(pointer_str)/x)
                    if(pointer_str == [pointer_str[:x]*chunks][0] and pointer not in invalid_ids):
                        print(f"{pointer_str}")
                        invalid_ids.append(pointer)
            pointer += 1
    print(f"TOTAL: {sum(invalid_ids)}")
    

if __name__ == "__main__":
    main()
