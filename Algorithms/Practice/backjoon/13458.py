from math import ceil

if __name__ == "__main__":
    N = int(input().strip())
    candidates = list(map(int, input().strip().split()))
    B, C = map(int, input().strip().split())

    count = 0
    for candidate in candidates:
        candidate -= B
        count += 1
        if candidate > 0:
            count += ceil(candidate / C)

    print(count)
