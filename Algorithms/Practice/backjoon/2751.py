# 250240kb 1928ms
def solution(N):
    nums = [int(input().strip()) for _ in range(N)]

    def merge(left, right):
        sorted_list = []
        left_idx, right_idx = 0, 0
        while left_idx < len(left) and right_idx < len(right):
            if left[left_idx] < right[right_idx]:
                sorted_list.append(left[left_idx])
                left_idx += 1
            else:
                sorted_list.append(right[right_idx])
                right_idx += 1
        while left_idx < len(left):
            sorted_list.append(left[left_idx])
            left_idx += 1
        while right_idx < len(right):
            sorted_list.append(right[right_idx])
            right_idx += 1
        return sorted_list

    def merge_sort(unsorted_list):
        if len(unsorted_list) <= 1:
            return unsorted_list

        piv = len(unsorted_list) // 2
        left = merge_sort(unsorted_list[:piv])
        right = merge_sort(unsorted_list[piv:])
        return merge(left, right)

    return "\n".join(map(str, merge_sort(nums)))


import sys

input = sys.stdin.readline

# 154148kb 1108ms -> O(NlogN)
def solution(N):
    nums = [int(input().strip()) for _ in range(N)]
    return "\n".join(map(str, sorted(nums)))


if __name__ == "__main__":
    print(solution(int(input().strip())))
