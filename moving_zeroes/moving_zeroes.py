'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    n = len(arr)
    count = 0

    for i in range(0, n):
        if (arr[i] != 0):
            arr[count], arr[i] = arr[i], arr[count]
            count += 1
    return arr

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    # arr = [0, 3, 1, 0, -2]
    arr = [4, 2,0,19,0,5,7,0,3,3,0,2,0,1,0]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")

#  Resources:
# 1.  https://tutorialspoint.dev/data-structure/arrays/move-zeroes-end-array
# 2.  https://www.geeksforgeeks.org/move-zeroes-end-array-set-2-using-single-traversal/
