def get_result(nums, k):
    count = 0

    while True:
        for x in range(k, 0, -1):
            if x in nums:
                nums.remove(x)
                k += 1
                count += 1
                break
        if len(nums) == 0:
            break
    return count


nums = [1, 2, 3, 4]
k = 1
print(get_result(nums, k))
