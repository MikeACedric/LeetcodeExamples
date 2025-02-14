# Check for duplicate number in a list of numbers

arr= [3,4,2,5,1]

# Brute force method
def checkForDuplicateNumber(list):
    n = len(list)
    for i in range(n):
        for j in range(i+1,n):
            if list[i] == list[j]:
                return True
    return False

# Faster method
def checkForDuplicateNumberwithSets(list):
    seen = set()
    for i in list:
        if i in seen:
            return True
        seen.add(i)
    return False
        
checkForDuplicateNumberwithSets(arr)
print("Duplicate in the list: ", checkForDuplicateNumberwithSets(arr))