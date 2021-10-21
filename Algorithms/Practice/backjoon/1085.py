X, Y, W, H = map(int, input().split())

print(min(X, Y, abs(W-X), abs(H-Y)))