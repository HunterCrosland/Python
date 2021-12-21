def search(nums: list, target: int) -> int:

    l = 0
    r = len(nums) - 1

    while (l < r):

        mid = l+r >> 1

        if target > nums[mid]:
            l = mid + 1

        elif target < nums[mid]:
            r = mid - 1

        else:
            return mid

    return l if nums[l] == target else -1
