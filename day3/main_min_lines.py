def f(n, b):
    return sorted(b)[-1] if n == 1 else b if n == len(b) else f'{b[b.find(max(b[:len(b) - n + 1]))]}{f(n-1, b[b.find(max(b[:len(b) - n + 1]))+1:])}'
i = [l.replace("\n","") for l in open("input.txt", "r").readlines()]
print(f"part 1: {sum([int(f(2,l)) for l in i])}\npart 2: {sum([int(f(12,l)) for l in i])}")