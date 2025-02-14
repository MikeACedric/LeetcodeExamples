
# check if a number is missing from a list of numbers

arr = [3,4,2,5,6]
n=6
def checkForMissingNumberInRange(arr, n):
    for num in range(1, n+1):
        if num not in arr:
            return num
    return None

# print("Missing number in the list:", checkForMissingNumberInRange(arr, n))


# Faster method

def checkForMissingNumberInRangeWithSum(arr,n):
    expected_sum= n*(n+1)//2
    actual_sum = sum(arr)
    return expected_sum - actual_sum


print("Missing number in the list:", checkForMissingNumberInRangeWithSum(arr, n))