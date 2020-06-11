#  [0, 1, 1, 2, 3, 5, 8, 13, 21]

#  Recursive:
def rec_fib(n):
    # base cases
    if n == 0:
        return 0
    if n == 1:
        return 1
    return rec_fib(n-1) + rec_fib(n-2)

print("rec_fib:")
print(rec_fib(4))
print(rec_fib(6))
print(rec_fib(10))
print(rec_fib(20))

##################################################

#  Storing values using a cache


cache = {0: 1, 1: 1}  ## ; global; includes base cases
def rec_fib_with_cache(n):
    if n in cache:
        return cache[n]
    cache[n] = rec_fib(n-1) + rec_fib(n-2)
    
    return cache[n]

print("rec_fib_with_cache: ")
print (rec_fib_with_cache(4))
print (rec_fib_with_cache(6))
print (rec_fib_with_cache(10))
print (rec_fib_with_cache(20))