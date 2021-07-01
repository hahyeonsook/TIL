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
class ListMode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 연결 리스트가 팰린드롬 구조인지 판별하라.

# 리스트 변환
from typing import List


class Solution:
    def isPalindrome(head: ListMode) -> bool:
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
from collections import deque


class Solution:
    def isPalindrome(head: ListMode) -> bool:
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


head = ListMode(1)
head.next = ListMode(2)
head.next.next = ListMode(3)
head.next.next.next = ListMode(2)
head.next.next.next.next = ListMode(1)

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
l1 = ListMode(1)
l1.next = ListMode(2)
l1.next.next = ListMode(4)

l2 = ListMode(1)
l2.next = ListMode(3)
l2.next.next = ListMode(4)

# 재귀 구조로 연결
class Solution:
    def mergeTwoLists(self, l1: ListMode, l2: ListMode) -> ListMode:
        if (not l1) or (l2 and l1.val > l2.val):
            l1, l2 = l2, l1
        # l1에 답 list를 생성함.
        # l2의 첫번째 값은 항상 l1.val보다 커야 하므로 위에서 l2가 더 작을 경우 l2로 옮김
        # 그리고 그 값을 제외한 잘린 값을 mergeTwoLists로 보내서 next를 지정하도록 함.
        if l1:
            l1.next = self.mergeTwoLists(l1.next, l2)
        # l1은 첫번째 if 문에서 항상 li2.val보다 작은 값을 가진 listmode를 return하게 됨.
        return l1


######
####해시
