
# Two Sum

# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

arr = [2, 7, 11, 15]
target = 9

# Brute Force Approach
def twoSum(nums, target):
    n= len(nums)
    for i in range(n):
        for j in range(i+1, n):
            if nums[i] + nums[j] == target:
                return [i,j]
    return []

# print("Indices of the two numbers that add up to the target:", twoSum(arr, target))


# Optimized Approach

def twoSumFaster(nums, target):
    hash_map = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in hash_map:
            return [hash_map[diff], i]
        hash_map[num] = i
    return []

print("Indices of the two numbers that add up to the target:", twoSumFaster(arr, target))


            