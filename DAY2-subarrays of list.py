def printSubsets(nums, index, result, value):
    if index == len(nums):
        print(result)
        value[0] += 1
        return
 
    result.append(nums[index])
    printSubsets(nums, index + 1, result, value)
    result.pop()

    printSubsets(nums, index + 1, result, value)
 
 
nums = [10, 20, 30, 40, 50, 60, 65]
 
value = [0]
printSubsets(nums, 0, [], value)
print(value[0])
