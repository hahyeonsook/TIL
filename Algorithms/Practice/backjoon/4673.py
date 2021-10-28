if __name__ == "__main__":
    nums = [False] + [True] * 10000

    for n in range(1, 10000):
        num = n + sum(map(int, str(n)))
        if num < len(nums) - 1:
            nums[num] = False

    for idx in range(10000):
        if nums[idx]:
            print(idx)
