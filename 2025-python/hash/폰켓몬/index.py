def solution(nums):
    isIncluded = {}
    for num in nums:
        isIncluded[num] = True
    includedKeys = isIncluded.keys()
    maxNum = len(nums) /2
    return min(len(includedKeys), maxNum)

# --------------------------------

def solution(nums):
    return min(len(set(nums)), len(nums) // 2)
