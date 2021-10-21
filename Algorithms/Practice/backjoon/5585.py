price = 1000 - int(input().strip())

answer = 0
money = [500, 100, 50, 10, 5, 1]
for m in money:
    n, price = divmod(price, m)
    answer += n
print(answer)
