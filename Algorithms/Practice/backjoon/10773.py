# 재현이는 잘못된 수를 부르면, 0을 외치고 그러면 재민이는 가장 최근의 쓴 수를 지운다.
num_of_lines = int(input())

# 수만큼 받아서 list화
# rows = [int(input()) for i in range(num_of_lines)]

accounts = []
# O(N)
for i in range(num_of_lines):
    val = int(input())

    if val == 0:
        accounts.pop()
    else:
        accounts.append(val)

# 파이썬은 초당 20,000,000 가능
# O(2N) 이므로 O(N) => 1<= k <= 100,000 이므로, 100,000
# O(N)
print(sum(accounts))
