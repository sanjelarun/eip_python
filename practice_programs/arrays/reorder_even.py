# REORDER ARRAYS
# Reorder the arrays such that evens numbers are in front of the list [1,2,3] -> [2,1,3]


def swap(i, j, nums):
    nums[i] = nums[i] + nums[j]
    nums[j] = nums[i] - nums[j]
    nums[i] = nums[i] - nums[j]


def reorder(nums):
    j = len(nums) - 1
    i = 0
    while i < j:
        if nums[i] % 2  == 0:
            i += 1
        else:
            swap(i,j,nums)
            j -= 1

nums = [1,2,3,12,3,123,14,123,1]
reorder(nums)
print(nums)