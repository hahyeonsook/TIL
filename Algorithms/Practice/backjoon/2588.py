A = int(input().strip())
B = input().strip()

answer = 0
for idx, number in enumerate(B[::-1]):
    temp = A * int(number)
    print(temp)
    answer += temp * (10 ** idx)
print(answer)
