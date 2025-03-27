def max_consecutive_sum(nums, k):
    if not nums or k > len(nums):
        return None
    
    max_sum = current_sum = sum(nums[:k])
    
    for i in range(k, len(nums)):
        current_sum += nums[i] - nums[i - k] 
        max_sum = max(max_sum, current_sum)
    
    return max_sum
nums = [2, 1, 5, 1, 3, 2]
k = 3
print(max_consecutive_sum(nums, k))
