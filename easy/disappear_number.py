
# Problem 448: Find All Numbers Disappeared in an Array

# Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

arr = [4,3,2,7,8,2,3,1]

def findDisappearedNumbers(nums):
   num = set(nums)
   res = []
   n = len(nums)
   for i in range(1, n+1):
        if i not in num:
            res.append(i) 
   return res

print("Array containing Disappered Numbers:", findDisappearedNumbers(arr))



