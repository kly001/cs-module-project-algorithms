'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here

#  Apply the formula:  2*(sum_of_array_without_duplicates) – (sum_of_array)
    return 2 * sum(set(arr)) - sum(arr)



if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")

    #  Resource: https://www.geeksforgeeks.org/find-element-appears-array-every-element-appears-twice/