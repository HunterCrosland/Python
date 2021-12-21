def findMaxConsecutiveOnes(nums: list) -> int:
    counter = 0
    maxi = 0
    for num in nums:
        if num == 1:
            counter += 1
        else:
            maxi = max(counter,maxi)
            counter = 0
    maxi = max(counter,maxi)
    return maxi
