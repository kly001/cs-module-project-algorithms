'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''

#  Method 1
def sliding_window_max(nums, k):
    # Your code here
    max = 0
    length = len(nums)
    

    for i in range(length - k+1):
        max = nums[i]
        for j in range(1, k):
            if nums[i+j] > max:
                max = nums[i+j]
        print(str(max))
##################################################

# Method 2
# def sliding_window_max(nums, k):
#     if not nums:
#         return []
#     return [max(nums[i:i+k]) for i in range(len(nums) - k + 1)]

if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(nums, k)}")

#  Resource:

# 1.  https://www.geeksforgeeks.org/sliding-window-maximum-maximum-of-all-subnumsays-of-size-k/?ref=rp
