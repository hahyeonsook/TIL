import sys

input = sys.stdin.readline
display_nums = {
    0: 0b1111110,
    1: 0b0001100,
    2: 0b1011011,
    3: 0b0011111,
    4: 0b0101101,
    5: 0b0110111,
    6: 0b1110111,
    7: 0b0011100,
    8: 0b1111111,
    9: 0b0111111,
}

# n, k, p, x = input().split()


def solution(n, k, p, x):
    results = [[0] * int(k)]

    for n_index in range(int(k)):
        current_floor = int(x[n_index])
        for d_index in range(len(display_nums)):
            xor = bin(display_nums[d_index] ^ display_nums[current_floor]).count("1")
            if xor != 0 and xor < int(p) + 1:
                if n_index == 0:
                    results.append([f"{d_index}", xor])
                else:
                    results[d_index][0] = f"{results[d_index][0]}{d_index}"
                    results[d_index][1] += xor
    print(results)


solution("48", "2", "5", "35")
