
# Porblem # 1365: How Many Numbers Are Smaller Than the Current Number
#brute force

arr = [8,1,2,2,3]
def smallerNumbersThanCurrent(nums):
    n= len(nums)
    result = []
    for i in range(n):
        count = 0
        for j in range(n):
            if nums[j] < nums[i]:
                count += 1
        result.append(count)
    return result

#print("Numbers smaller than the current number:", smallerNumbersThanCurrent(arr))


# Faster Method:

def smallerNumbersThanCurrentOptimized(nums):
    num_to_index = {}
    sorted_nums = sorted(nums)
    for i,n in enumerate(sorted_nums):
        if n not in num_to_index:
            num_to_index[n] = i
    result= []
    for num in nums:
                result.append(num_to_index[num])
    return result
            
print("Numbers smaller than the current number:", smallerNumbersThanCurrentOptimized(arr))

