'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):
    # Your code here

#  The length of the input array
    length = len(arr)
#  The result array to be returned
    result = [0]*length

#  result[i] contains the product of all the elements to the left
#  If the element is at index '0', there are no elements to its left, thus:
    result[0] = 1

    for i in range(1, length):
#   result[i-1] already contains the product of elements to the left of 'i-1'
#   Multiplying it with arr[i-1] would give the product of all

#  elements to the left of index 'i'
        result[i] = arr[i-1] * result[i-1]

# R contains the product of all the elements to the right
# Note: for the element at index 'length - 1', there are no elements to the right,
# so the R would be 1
    
    rightProduct = 1
    for i in reversed(range(length)):

# For the index 'i', R would contain the 
# product of all elements to the right. We update R accordingly
        result[i] = result[i] * rightProduct
        rightProduct *= arr[i]

    return result
  


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")

#  Resource:   https://leetcode.com/problems/product-of-array-except-self/solution/
