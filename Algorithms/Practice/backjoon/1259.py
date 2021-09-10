import sys

input = sys.stdin.readline
while True:
    num = input().strip()
    if num == "0":
        break
    elif num == num[::-1]:
        print("yes")
    else:
        print("no")
