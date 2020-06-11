'''
Input: an integer
Returns: an integer
'''
#####  Method 1  #####
# def eating_cookies(n):
#     # Your code here
# # base case: when there are no more cookies
#     if n == 0:
#         return 1

# # check for negative n values
#     elif n <= 0:
#         return 0

# # this represents our recursive case where there are still cookies to be eaten
#     return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)

#############################################################

#  Caching/memoization: Save work so it doesn't have to be repeated

#  Need some sort of data structure where we can save data
#  arrays and dictionaries
#  If we check our cache and the answer we are looking for is already in there,
#  just return that answer
#  how do we add answers into the cache?

def eating_cookies(n, cache = None):
    print(n)
# base case: when there are no more cookies
    if n == 0:
        return 1

# check for negative n values
    elif n < 0:
        return 0

#  init our cache
#  add a case to check cache
    elif cache and cache[n] > 0:
        return cache[n]
    else:
        if not cache:
            cache = [0 for _ in range(n+1)]  ### An array
            ### OR  ###
            # cache = {i: 0 for i in range(n+1)}   ### A dictionary
# save the answer to the cache 
# this represents our recursive case where there are still cookies to be eaten
        cache[n] = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)
    return cache[n]
   

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
