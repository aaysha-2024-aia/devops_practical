nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
max_sum = nums[0]
current_sum = nums[0]
for i in nums[1:]:
 current_sum = max(i, current_sum + i)
 max_sum = max(max_sum, current_sum)
print("Largest sum:", max_sum)