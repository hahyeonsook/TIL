from collections import deque


def solution1(number):
    cards = deque([i + 1 for i in range(number)])

    # O(N)
    while len(cards) > 1:
        cards.popleft()
        # O(N)
        cards.rotate(-1)

    return cards[0]


def solution2(number):
    cards = deque([i + 1 for i in range(number)])

    # O(N)
    while len(cards) > 1:
        cards.popleft()

        val = cards.popleft()
        cards.append(val)

    return cards[0]


# 파이썬은 초당 20,000,000 가능
# 보통 5초 제한, 5초에 100,000,000
# O(N^2) <= 250,000,000,000
print(solution1(4))  # 4
print(solution2(4))  # 4


N = int(input())
cards = deque([i + 1 for i in range(N)])

while len(cards) > 1:
    cards.popleft()

    val = cards.popleft()
    cards.append(val)

print(cards[0])
