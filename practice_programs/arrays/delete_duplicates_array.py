'''
WAP which takes as input a sorted array and updates it so that all duplicates have been removed and shited left
'''
# MY METHOD
def next_number(nums, current_pos):
    n = 0
    for i in nums[current_pos:]:
        if i != -1:
            return current_pos + n
        n += 1
    return -1
def delete_duplications(nums):
    previous = nums[0]
    total_duplication = 0
    length = len(nums)
    for i in range(1, length):
        if previous == nums[i]:
            nums[i] = -1
            total_duplication += 1
        else:
            previous = nums[i]
    pos = 0
    cnt = 0
    while cnt < total_duplication:
        if nums[pos] == -1:
            next_pos = next_number(nums, pos+1)
            nums[pos], nums[next_pos] = nums[next_pos], nums[pos]
            cnt += 1
        pos += 1
# BOOK METHOD
def del_dupli(nums):
    if not nums:
        return 0
    write_index = 1
    for i in range(1, len(nums)):
        if nums[write_index -1] != nums[i]:
            nums[write_index] = nums[i]
            write_index += 1
    return write_index

nums = [2,3,5,5,7,7,7,7,7,11,11,11,13]


print(del_dupli(nums))