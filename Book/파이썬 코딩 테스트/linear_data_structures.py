# 파이썬은 리스트가 동적 배열 자료형이다.
# 대부분의 동적 프로그래밍 언어들은 아예 정적 배열 자체가 없다.
# 동적 배열의 원리는 미리 초깃값을 작게 잡아 배열을 생성하고, 데이터가 추가되면서 꽉 채워지면, 늘려주고 모두 복사하는 식이다.
# 대개는 더블링이라 하여 2배씩 늘려주게 된다.
# 재할당 비율을 그로스 팩터, 성장 인자 라고 한다. 파이썬의 그로스 팩터는 초반에는 2배씩 늘려 가지만, 전체적으로는 약 1.125배로 다른 언어에 비해서는 다소 조금만 늘려간다.
# 더블링이 필요한 만큼 공간이 차게 되면, 새로운 메모리 공간에 더 큰 크기의 배열을 할당하고 복사하는 작업이 필요하므로 O(n) 비용이 발생한다.

# 덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라.


import re


nums = [2, 7, 11, 15]
target = 9

# 브루투 포스로 계산
def twoSum(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


print(twoSum(nums, target))

# in을 이용한 탐색
# 모든 조합을 비교하지 않고, 타겟에서 첫 번째 값을 뺀 값 target-n이 존재하는지 탐색하는 문제로 변경해보자.
def twoSum(nums: list[int], target: int) -> list[int]:
    # enumerate() : index와 값을 차례로 return
    for i, n in enumerate(nums):
        complement = target - n
        # 파이썬 레벨에서 값을 비교하는 것에 비해
        # 같은 시간 복잡도라도 in 연산 쪽이 훨씬 더 가볍고 빠르다.
        if complement in nums[i + 1 :]:
            return [nums.index(n), nums[i + 1 :].index(complement) + (i + 1)]


print(twoSum(nums, target))


# 첫 번째 수를 뺀 결과 키 조회
# list.index로 값을 빼는 연산은 O(n)이다. 딕셔너리로 바꿔서 연산 횟수를 줄이자.
def twoSum(nums: list[int], target: int) -> list[int]:
    nums_map = {}
    # 키와 값을 바꿔서 딕셔너리로 저장
    for i, num in enumerate(nums):
        nums_map[num] = i

    # 타겟에서 첫 번째 수를 뺀 결과를 키로 조회
    for i, num in enumerate(nums):
        complement = target - num
        #                                  현재 index와 target-num의 값의 index가 같지 않을 때
        if complement in nums[i + 1 :] and i != nums_map[complement]:
            return [i, nums_map[complement]]


print(twoSum(nums, target))


# 조회 구조 개선
def twosum(nums: list[int], target: int) -> list[int]:
    nums_map = {}
    # 하나의 for 문으로 통합
    for i, num in enumerate(nums):
        if target - num in nums[i + 1 :]:
            return [i, nums_map[target - num]]
        nums_map[num] = i


# 투 포인터 이용
# 단, 이 알고리즘은 list가 오름차순으로 정렬되어 있을 때 유효함.
# 두 포인터를 list의 양 끝에서 시작해서
# 더한 값 > target, 오른쪽 포인트를 왼쪽으로
# 더한 값 < target, 왼쪽 포인트를 오른쪽으로
def twoSum(nums: list[int], target: int) -> list[int]:
    left, right = 0, len(nums) - 1
    # 두 값이 같으면 조건을 만족하는 값이 없다는 의미
    while not left == right:
        # 합이 타겟보다 작으면 왼쪽 포인터를 오른쪽으로
        if nums[left] + nums[right] < target:
            left += 1
        # 합이 타겟보다 크면 오른쪽 포인터를 왼쪽으로
        elif nums[left] + nums[right] > target:
            right -= 1
        else:
            return [left, right]


# 단 위의 알고리즘은 정렬되어 있을 때 유효하다.
# 하지만, 이 문제는 인덱스를 출력하는 것이므로, 인덱스를 어지럽히면 값을 구하기 힘들다.


# 높이를 입력받아 비 온 후 얼마나 많은 물이 쌓일 수 있는지 계산하라.
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

# 투 포인터로 풀기
def trap(height: list[int]) -> int:
    if not height:
        return 0

    volume = 0
    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]

    while left < right:
        # left_max의 값은 이전 막대의 높이 값을 간직하게 함.
        # 그래서 height[left] 값이 이전 막대의 높이에 비해 낮아지면 volume 계산을 할 수 있도록 함.
        # 해당 인덱스의 경우, left_max와 height[left]의 값이 같으니까 0으로 volume의 계산도 유지하도록 해줌.
        left_max = max(height[left], left_max)
        right_max = max(height[right], right_max)

        # 더 높은 쪽을 향해 투 포인터 이동
        # 최대 높이가 왼쪽과 오른쪽을 가르는 기준이 된다.
        # left가 최대 높이에 다다르면, left_max는 max(height[left])에 의해 right_max 보다 커지게 되고
        # right 부분의 계산이 시작된다.
        if left_max <= right_max:
            volume += left_max - height[left]
            left += 1
        else:
            volume += right_max - height[right]
            right -= 1

    return volume


print(trap(height))

# 스택 쌓기
# 스택을 쌓으면서, 현재 높이가 이전 높이보다 높을 때, 채움.
# https://www.youtube.com/watch?v=hOIQ28oI1tc
def trap(height: list[int]) -> int:
    stack = []
    volume = 0

    for i in range(len(height)):
        # 변곡점을 만나는 경우
        while stack and height[i] > height[stack[-1]]:
            # 스택에서 꺼낸다.
            top = stack.pop()

            if not len(stack):
                break

            # 이전과의 차이만큼 물 높이 처리
            # 인덱스 차이 계산, 현재 인덱스와 막대가 있던 인덱스의 차이 값 - 현재 인딕스는 포함 안하고 구하려고 하니까 현재 값 1 빼기.
            # 가로의 값
            distance = i - stack[-1] - 1
            # min((현재 i, 현재 인덱스의 높이), (현재 인덱스의 전의 전의 높이)) - 이전 기둥의 높이
            # min은 왜 넣는거지? 한쪽이 1이고 한쪽이 2인 바구니 안에는 1의 만큼만 물이 채워질 것이므로 작은 값을 높이로 하기 위해서
            # 세로의 값
            waters = min([height[i], height[stack[-1]]]) - height[top]

            volume += distance * waters

        stack.append(i)

    return volume


print(trap(height))


# 세 수의 합
# 배열을 입력받아 합으로 0을 만들 수 있는 엘리먼트를 출력하라.

nums = [-1, 0, 1, 2, -1, -4]

# 브루트 포스로 계산
def threeSum(nums: list[int]) -> list[list[int]]:
    results = []
    nums.sort()

    # 브루트 포스 n^3 반복
    for i in range(len(nums) - 2):
        # 중복된 값 건너뛰기
        # 이전에 이미 계산하고 넘어온 것이므로 굳이 계산할 필요 없음.
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, len(nums) - 1):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            for k in range(j + 1, len(nums)):
                if k > j + 1 and nums[k] == nums[k - 1]:
                    continue
                if nums[i] + nums[j] + nums[k] == 0:
                    results.append([nums[i], nums[j], nums[k]])

    return results


print(threeSum(nums))


# 투 포인터로 합 계산


def threeSum(nums: list[int]) -> list[list[int]]:
    results = []
    nums.sort()

    for i in range(len(nums) - 2):
        # 중복된 값 건너뛰기
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # 간격을 좁혀나가며 합 sum 계산
        left, right = 0, len(nums) - 1
        while left < right:
            sum = nums[i] + nums[left] + nums[right]
            if sum > 0:
                right -= 1
            elif sum < 0:
                left += 1
            else:
                # sum = 0인 경우이므로 정답 및 스킵 처리
                results.append([nums[i], nums[left], nums[right]])

                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1

        return results


# 투 포인터
# 대개는 시작점과 끝점 또는 왼쪽 포인터와 오른쪽 포인터 두 지점을 기준으로 하는 문제 풀이 전략을 뜻한다.
# 범위를 좁혀나가기 위해서는 일반적으로 배열이 정렬되어 있을 때 더 유용하다.

# 배열 파티션 1
# n 개의 페어를 이용한 min(a, b)의 합으로 만들 수 있는 가장 큰 수를 출력하라.
nums = [1, 4, 3, 2]

# 이건 입력 값이 항상 2n개일 때
def arrayPairSum(nums: list[int]) -> int:
    sum = 0
    pair = []
    nums.sort()
    # 페어의 min()을 합산했을 때 최대를 만드는 것은 결국 min()이 되도록 커야 한다는 뜻이고
    # 뒤에서 내림차순으로 집어넣으면 항상 최대 min 페어를 유지할 수 있음.
    # 입력값이 항상 2n개이므로 오름차순으로 앞에서 집어넣어도 됌.
    for n in nums:
        # 앞에서부터 오름차순으로 페어를 만들어서 합 계산
        pair.append(n)
        if len(pair) == 2:
            sum += min(pair)
            pair = []


print(arrayPairSum(nums))

# 짝수 번째 값 계산
# 일일이 min()을 구하지 않아도 짝수 번째 값을 더하면 될 것 같다.
# 정렬된 상태에서는 짝수 번째에 항상 작은 값이 위치하기 때문
def arrayPairSum(nums: list[int]) -> int:
    sum = 0
    nums.sort()

    for i, n in enumerate(nums):
        # 짝수 번째의 값의 합 계산
        if i % 2 == 0:
            sum += n

    return sum


# 파이썬다운 방식
def arrayPairSum(nums: list[int]) -> int:
    return sum(sorted(nums)[::2])


# 자신을 제외한 배열의 곱
# 배열을 입력받아 output[i]가 자신을 제외한 나머지 모든 요소의 곱셈 결과가 되도록 출력하라
nums = [1, 2, 3, 4]


def productExceptSelf(nums: list[int]) -> int:
    out = []
    p = 1

    # 왼쪽 곱셈
    for i in range(0, len(nums)):
        out.append(p)
        p = p * nums[i]

    p = 1
    #                            range 는 <= < 이므로 -1 해줘야 끝까지 감.
    for i in range(len(nums) - 1, 0 - 1, -1):
        out[i] = out[i] * p
        p = nums[i] * p

    return out


print(productExceptSelf(nums))


# 주식을 사고팔기 가장 좋은 시점
# 한 번의 거래로 낼 수 있는 최대 이익을 산출하라.
prices = [7, 1, 5, 3, 6, 4]

# 브루트 포스로 계산
def maxProfit(prices: list[int]) -> int:
    max_price = 0

    for i, price in enumerate(prices):
        for j in range(i, len(prices)):
            # 주식이므로 진행순서는 list index 순서이다. - 나와도 순서대로 팔아야 함.
            max_price = max(prices[j] - price, max_price)

    return max_price


print(maxProfit(prices))

import sys


def maxProfit(prices: list[int]) -> int:
    profit = 0
    min_price = sys.maxsize

    for i, price in enumerate(prices):
        min_price = min(price, min_price)
        profit = max(profit, price - min_price)

    return profit


print(maxProfit(prices))


# 최댓값과 최솟값
# sys 모듈을 활용하면 시스템이 지정할 수 있는 가장 높은 값, 가장 낮은 값을 활용할 수 있다.
# 사실 파이썬에서는 큰 의미가 없다. 파이썬의 숫자형은 임의 정밀도를 지원하여 사실상 무한대의 값을 지정할 수 있다.
# 하지만 일반적인 코딩 테스트의 경우, 모든 언어에 대응하는 공통된 테스트 케이스로 구성되어 있고,
# 따라서 파이썬에서 sys.maxsize로 충분히 모든 테스트 케이스를 통과할 수 있다.

# 연결 리스트
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 연결 리스트가 팰린드롬 구조인지 판별하라.

# 리스트 변환
from typing import List


class Solution:
    def isPalindrome(head: ListNode) -> bool:
        q: List = []

        if not head:
            return True

        node = head
        # 리스트 변환
        while node is not None:
            q.append(node.val)
            node = node.next

        # 팰린드롬 판별
        while len(q) > 1:
            if q.pop(0) != q.pop():
                return False

        return True


# 데크를 이용한 최적화
from collections import defaultdict, deque


class Solution:
    def isPalindrome(head: ListNode) -> bool:
        q: Deque = deque()

        if not head:
            return True

        node = head
        while node is not None:
            if q.popleft() != q.pop():
                return False

        return True


# 런너를 이용한 풀이


class Solution:
    def isPalindrome(head) -> bool:
        rev = None
        slow = fast = head
        # 런너를 이용해 역순 연결 리스트 구성
        # fast.next = None 이라서 끝나는 경우는 홀수
        # fast = None 이라서 끝나는 경우는 짝수
        while fast and fast.next:
            fast = fast.next.next
            # 다중 할당
            # rev, rev.next = slow, rev
            # slow = slow.next 로 할 경우, 값이 올바르게 나오지 않음.
            # rev = 1, slow = 2->3 이라고 하자.
            # 아래의 경우, 세 개의 할당 작업이 한 번에 일어난다.
            # rev = slow, rev.next = rev, slow = slow.next
            # 파이썬은 원시 타입이 존재하지 않고, 모든 것이 객체이다.
            # 문자와 숫자의 경우 불변 객체라는 점만 다르다.
            # 그래서 문자나 숫자를 변수에 할당할 경우, 변수 이름으로 메모리에 자리를 갖는 것이 아니라,
            # 숫자나 문자가 할당되고, 변수는 그 문자나 숫자의 메모리 주소를 할당하게 된다.
            # 따라서 rev = slow 의 경우 slow의 값이 rev로 복사되는 것이 아니라 slow의 id 값을 rev가 참조하게 된다.
            # rev의 값을 변경시키면 같은 id를 참조하고 있는 slow의 값도 변경되게 되는 것이다.
            # 나눠서 선언하게 될 경우, rev = 2->3, rev.next = 1 => rev = 2->1이 되고 같은 id를 공유하는 slow도 2->1이 된다.
            # 그러면 slow.next = 1이 되어 slow = 1이 되는 것이다.
            rev, rev.next, slow = slow, rev, slow.next
        # 연결 리스트가 홀수일 때는 slow가 중앙 값에서 시작함.
        # 그런데, 홀수의 경우 rev는 가운데 값을 가지지 않음.
        # 그래서 slow도 중앙 값을 제외한 연결 리스트를 가지고 있어야 함.
        # 홀수일 경우 fast는 None이 아니므로 slow를 한 칸 더 이동시킴.
        if fast:
            slow = slow.next

        # 팰린드롬 여부 확인
        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
        # not None >>> True
        return not rev


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(2)
head.next.next.next.next = ListNode(1)

sol = Solution
print(sol.isPalindrome(head))


# 런너 기법
# 연결 리스트를 순회할 때, 2개의 포인터를 동시에 사용하는 기법이다. 한 포인터가 다른 포인터보다 앞서게 하여
# 병합 지점이나 중간 위치, 길이 등을 판별할 때 유용하게 사용할 수 있다.
# 2개의 포인터는 각각 빠른 런너, 느린 런너라고 부르는데, 대개 빠른 런너는 두 칸씩 건너뛰고 느린 런너는 한 칸씩 이동하게 한다.
# 이때 빠른 런너가 연결 리스트의 끝에 도달하면, 느린 런너는 정확히 연결 리스트의 중간 지점을 가리키게 된다.
# 이 같은 방식으로 중간 위치를 찾아내면, 여기서부터 값을 비교하거나 뒤집기를 시도하는 등 여러모로 활용할 수 있어
# 연결 리스트 문제에서는 반드시 쓰이는 기법이기도 하다.

# 두 정렬 리스트의 병합
# 정렬되어 있는 두 연결 리스트를 합쳐라.
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

# 재귀 구조로 연결
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if (not l1) or (l2 and l1.val > l2.val):
            l1, l2 = l2, l1
        # l1에 답 list를 생성함.
        # l2의 첫번째 값은 항상 l1.val보다 커야 하므로 위에서 l2가 더 작을 경우 l2로 옮김
        # 그리고 그 값을 제외한 잘린 값을 mergeTwoLists로 보내서 next를 지정하도록 함.
        if l1:
            l1.next = self.mergeTwoLists(l1.next, l2)
        # l1은 첫번째 if 문에서 항상 li2.val보다 작은 값을 가진 listNode를 return하게 됨.
        return l1


# 역순 연결 리스트
class Solution:
    def reverseList(head: ListNode) -> ListNode:
        def reverse(node: ListNode, prev: ListNode = None):
            if not node:
                return prev
            next, node.next = node.next, prev
            return reverse(next, node)

        return reverse(head)


class Solution:
    def reverseList(haed: ListNode) -> ListNode:
        node, prev = head, None

        while node:
            next, node.next = node.next, prev
            prev, node = (node,)

        return prev


# 3부 선형 자료구조/해시 테이블

# 해시맵 디자인
# 다음의 기능을 제공하는 해시맵을 디자인하라.
# put(key, value)
# get(key)
# remove(key)
import collections


class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None


class MyHashMap:
    def __init__(self):
        self.size = 1000
        self.table = collections.defaultdict(ListNode)

    def put(self, key: int, value: int) -> None:
        index = key % self.size
        # defaultdict로 자동으로 생성해주기 때문에
        # self.table[index] is None은 항상 False이다.
        # 인덱스에 노드가 없다면 삽입 후 종료
        if self.table[index].value is None:
            self.table[index] = ListNode(key, value)
            return

        # 해시 충돌이 발생하는 경우
        # 개별 체이닝 방식으로 충돌을 해결.
        # 인덱스에 노드가 존재하는 경우 연결 리스트 처리
        p = self.table[index]
        while p:
            # 이미 키가 존재하는 경우, 값을 저장하고 빠짐.
            if p.key == key:
                p.value = value
                return
            if p.next is None:
                break
            # p의 next로 이동해서 끝의 연결 리스트를 찾음.
            p = p.next
        p.next = ListNode(key, value)

    # 조회
    def get(self, key: int) -> int:
        index = key % self.size
        if self.table[index].value is None:
            return -1

        # 노드가 존재할 때 일치하는 키 탐색
        p = self.table[index]
        while p:
            if p.key == key:
                return p.value
            p = p.next
        return -1

    # 삭제
    def remove(self, key: int) -> None:
        index = key % self.size
        if self.table[index].value is None:
            return

        # 인덱스의 첫 번째 노드일 때 삭제 처리
        p = self.table[index]
        if p.key == key:
            self.table[index] = ListNode() if p.next is None else p.next
            return

        # 연결 리스트의 노드 삭제
        prev = p
        while p:
            if p.key == key:
                prev.next = p.next
                return
            prev, p = p, p.next


# J는 보석이며, S는 갖고 있는 돌이다. S에는 보석이 몇 개나 있을까? 대소문자는 구분한다.
J = "aA"
S = "aAAbbbb"


def numJewelsInStones(J: str, S: str) -> int:
    freqs = {}
    count = 0

    # 돌(S)의 빈도 수 계산
    for char in S:
        if char not in freqs:
            freqs[char] = 1
        else:
            freqs[char] += 1

    # 보석(J)의 빈도 수 계산
    for char in J:
        if char in freqs:
            count += freqs[char]

    return count


print(numJewelsInStones(J, S))

# defaultdict를 이용한 비교 생략
import collections


def numJewelsInStones(J: str, S: str) -> int:
    freqs = collections.defaultdict(int)
    count = 0

    # 비교 없이 돌(S) 빈도 수 계산
    for char in S:
        freqs[char] += 1

    # 비교없이 보석(J) 빈도 수 합산
    for char in J:
        count += freqs[char]

    return count


print(numJewelsInStones(J, S))


# Counter로 계산 생략
def numJewelsInStones(J: str, S: str) -> int:
    freqs = collections.Counter(S)  # 돌(S) 빈도 수 계산
    count = 0

    for char in J:
        # Counter는 존재하지 않는 키의 경우 KeyError를 발생하는 게 아니라 0을 출력해주기 때문에,
        # defaultdict와 마찬가지로 에러에 대한 예외 처리 없이 할 수 있음.
        count += freqs[char]

    return count


# 파이썬다운 방식
def numJewelsInStones(J: str, S: str) -> int:
    # [s for s in S] >>> ['a', 'A', 'A', 'b', 'b', 'b', 'b']
    # [s in J for s in S] >>> [True, True, True, False, False, False, False]
    return sum(s in J for s in S)


print(numJewelsInStones(J, S))


# 중복 문자가 없는 가장 긴 부분 문자열의 길이를 리턴
string1 = "abcabcdbb"
string2 = "bbbbb"
string3 = "pwwkew"

# 슬라이딩 윈도우와 투 포인터로 사이즈 조절
def lengthOfLongestSubstring(s: str) -> int:
    used = {}
    # start, index가 두 개의 포인터임.
    # 각각 연속적이지 않은 부분 문자열의 시작과 끝을 맡고 있음.
    max_length = start = 0
    for index, char in enumerate(s):
        # 이미 등장했던 문자라면 'start' 위치 갱신
        #                   슬라이싱 밖에 있는 동일한 문자는 무시하기 위한 조건
        #                   슬라이싱이란, 현재 탐색하고 있는 중복없는 부분 문자열 부분을 말함.
        if char in used and start <= used[char]:
            # 이 경우 start는 이 전에 나왔던 char의 위치 + 1이 된다.
            # 왜냐면, start는 중복없는 문자열의 시작이어야 하므로,
            # 중복된 문자의 다음부터 시작해야 조건을 맞출 수 있기 때문
            start = used[char] + 1
        # 처음 보는 문자일 경우, 부분 문자열의 길이를 확인하면서 더 큰 값인 경우 갱신.
        else:
            max_length = max(max_length, index - start + 1)

        # 현재 문자의 위치 삽입
        used[char] = index

    return max_length


lengthOfLongestSubstring(string1)
lengthOfLongestSubstring(string2)
lengthOfLongestSubstring(string3)

# 상위 k번 이상 등장하는 요소를 추출하라.
nums = [1, 1, 1, 2, 2, 3]
k = 2

# Counter를 이용한 음수 순 추출

import collections
import heapq


def topKRfrequent(nums: List[int], k: int) -> List[int]:
    freqs = collections.Counter(nums)
    freqs_heaps = []

    for f in freqs:
        #              원소를 추가할 list, 추가할 원소
        #                            f의 횟수를 음수로,
        # 이렇게 음수로 하면 최대 힙을 얻을 수 있음.
        heapq.heappush(freqs_heaps, (-freqs[f], f))

    topk = list()
    # k번 만큼 추출, 최소 합(Min Heap)이므로 가장 작은 음수 순으로 추출
    for _ in range(k):
        # heap[0]은 최소 값이 나옴.
        # heappop도 최소 값이 나오는데, 여기는 최대 힙으로 저장했으므로, 최대 값이 나옴
        # 튜플로 (횟수, 요소)로 저장되어 있으므로 [1] 을 출력하면 요소 값만 출력할 수 있음.
        topk.append(heapq.heappop(freqs_heaps)[1])

    return topk


print(topKRfrequent(nums, k))


def topKRfrequent(nums: List[int], k: int) -> List[int]:
    # [(1, 3), (2, 2)] -> [(1, 2), (3, 2)]로 [요소, 횟수]로 바뀌게 됨.
    return list(zip(*collections.Counter(nums).most_common(k)))[0]


# zip() 함수는 2개 이상의 시퀀스를 짧은 길이를 기준으로 일대일 대응하는 새로운 튜플 시퀀스를 만드는 역할을 한다.
# >>> a=[1,2,3,4,5]
# >>> b=[2,3,4,5]
# >>> c=[3,4,5]
# >>> list(zip(a, b))
# 짧은 b를 기준으로 a와 일대일 대응하는 새로운 튜플 시퀀스를 만듦.
# >>> [(1, 2), (2, 3), (3, 4), (4, 5)]
# >>> list(zip(a,b,c))
# 짧은 c를 기준으로 a와 b를 일대일 대응하는 새로운 시퀀스를 만듦.
# [(1, 2, 3), (2, 3, 4), (3, 4, 5)]

# * 언패킹
# >>> collections.Counter(nums).most_common()
# [(1, 3), (2, 2), (3, 1)]
# >>> list(zip(collections.Counter(nums).most_common(2)))
# [((1, 3),), ((2, 2),)]


# 데크, 우선순위 큐
# 데크는 더블 엔디드 큐(Double-Ended Queue)의 줄임말로, 글자 그대로 양쪽 끝을 모두 추출할 수 있는, 큐를 일반화한 형태의 추상 자료형(ADT)
# Python에서는 collections 모듈에서 deque라는 이름으로 지원한다.
# collections.deque는 이중 연결 리스트로 구현되어 있다. CPython에서는 고정 길이 하위 배열을 지닌 이중 연결 리스트로 구현되어 있으며,
# 내부 구현을 살펴보면 dequeobject가 block 노드의 이중 연결 리스트로 구현되어 있는 것을 확인할 수 있다.

"""
//cpython/Modlues/_collectionsmodule.c
typedef struct BLOCK{
    struct BLOCK *leftlink;
    PyObject *data[BLOCKLEN];
    struct BLOCK *rightlink;
} block;

typedef struct {
    ...
    block *leftblock;
    block *rightblock;
    Py_ssize leftindex;
    Py_ssize rightindex;
    Py_ssize maxlen;
    ...
} dequeObject;
"""
# 사실상 아무런 의미없이 단순히 풀이를 위해 구현되어 있다.
# 다음 연산을 제공하는 원형 데크를 디자인하라.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class MyCircularDeque:
    # k: 최대 길이 정보
    def __init__(self, k: int):
        self.head, self.tail = ListNode(None), ListNode(None)
        self.k, self.len = k, 0
        self.head.right, self.tail.left = self.tail, self.head

    # 이중 연결 리스트에 신규 노드 삽입
    def _add(self, node: ListNode, new: ListNode):
        n = node.right
        node.right = new
        new.left, new.right = node, n

    def _del(self, node: ListNode):
        n = node.right.right
        node.right = n
        n.left = node

    def insertFront(self, value: int) -> bool:
        if self.len == self.k:
            return False
        self.len += 1
        self._add(self.head, ListNode(value))
        return True

    def insertLast(self, value: int) -> bool:
        if self.len == self.k:
            return False
        self.len += 1
        self._add(self.tail, ListNode(value))
        return True

    def deleteFront(self) -> bool:
        if self.len == 0:
            return False
        self.len -= 1
        self._del(self.head)
        return True

    def deleteLast(self) -> bool:
        if self.len == 0:
            return False
        self.len -= 1
        self._del(self.tail)
        return True

    def getFront(self) -> int:
        return self.head.val if self.len else -1

    def getLast(self) -> int:
        return self.tail.val if self.len else -1

    def isEmpty(self) -> bool:
        return self.len == 0

    def isFull(self) -> bool:
        return self.len == self.k


# 우선순위 큐
# 큐 도는 스택과 같은 추상 자료형과 유사하지만 추가로 각 요소의 우선순위와 연관되어 있다.
# 힙 정렬 등을 활용한다.

# k 개의 정렬된 리스트를 1개의 정렬된 리스트로 병합하라.
def print_linked_list(lists):
    node = lists
    while node:
        print(f"{node.val}", end=" ")
        node = node.next
    print()


class ListNode:
    def __init__(self, val=None):
        self.val = val
        self.next = None


l1 = ListNode(1)
l1.next = ListNode(4)
l1.next.next = ListNode(5)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

l3 = ListNode(2)
l3.next = ListNode(6)

lsts = [l1, l2, l3]

import heapq


def mergeLists(lists: List[ListNode]) -> ListNode:
    root = result = ListNode(None)
    heap = []

    # 각 연결 리스트의 루트를 힙에 저장
    for i in range(len(lists)):
        # 연결 리스트의 루트값이 같을 경우, 에러가 발생함
        # 중복 값을 구분할 수 있는 추가 인자가 필요함.
        if lists[i]:
            heapq.heappush(heap, (lists[i].val, i, lists[i]))

    # 힙 추출 이후 다음 노드는 다시 저장
    while heap:
        # node = (연결 리스트의 루트 값, 연결 리스트의 index 값, 연결 리스트의 루트 노드)
        #      가장 작은 노드의 연결 리스트부터 차례로 나옴.
        node = heapq.heappop(heap)
        # 연결 리스트의 index 값
        idx = node[1]
        # id(result) == id(node[2]) True
        # id(result.next) == id(node[2]) False
        # 이 부분은 root에 값을 저장하기 위한 것임
        # result = node[2]로 하면 root = result이므로 값이 계속 node[2]로 변경됨.
        # 그런데, next를 먼저 지정하면 root는 None->node[2]의 상태가 됨.
        result.next = node[2]
        # 2221366727872 2221366727872
        # print(id(root.next), id(result.next))

        result = result.next
        # 2221366727536 2221366727872
        # print(id(root), id(result))
        # k개의 연결 리스트가 모두 힙에 계속 들어 있어야 그 중에서 가장 작은 노드가 항상 차례로 나올 수 있으므로,
        # 추출한 연결 리스트의 그 다음 노드는 다시 힙에 추가함.
        if result.next:
            heapq.heappush(heap, (result.next.val, idx, result.next))
    return root.next


n = mergeLists(lsts)
print_linked_list(n)

# PriorityQueue의 _get()와 _put()은 모두 heapq 모듈의 heappop()과 heappush()를 그대로 사용하므로 둘은 동일하다.
# 차이점은 스레드 세이프 클래스라는 점이다.
# 파이썬은 GIL 특성상 멀티 스레딩이 거의 의미가 없기 때문에 대부분 멀치 프로세싱으로 활용한다.
# 따라서 굳이 멀티 스레드로 구현할 게 아니라면 PriorityQueue 모듈은 사용할 필요가 없다.

# 파이썬 전역 인터프리터 락(GIL)
# 하나의 스레드가 자원을 독점하는 형태로 실행된다. CPU가 하나던 당시에는 그럴만 했으나, 지금처럼 멀티 코어가 당연한 세상에서
# 하나의 스레드가 자원을 독점하고 실행되는 제약은 치명적이다.
