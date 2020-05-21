'''
Input: an integer
Returns: an integer
'''

# Memoization/caching/saving: lets us save our work so we don't have to recompute it again

# Need some sort of data structure to save the data
# arrays and dictionaries
# If we check our cache and see that the answer we're looking for is already in there, just return that answer
# What if the cache doesn't have what we're looking for? Or how do we get answers in there?
# There's going to be a first time for calculating an answer, and we're going to do it the same way we're currently doing it

def eating_cookies(n, cache=None): # O(3^n) three decisions being made every time drops to O(n) when using cache
    print(n)
    # base case: when there are no more cookies
    if n == 0:
        return 1
    
    elif n < 0:
        return 0

    # init our cache if we don't have it yet
    # add a case to have us check the cache
    elif cache and cache[n] > 0:
        return cache[n]

    else:
        if not cache:
            cache = [0 for _ in range(n+1)]
            # cache = {i: 0 for i in range(n+1)} # dictionary setup
        # we can save our answer to the cache now
        cache[n] = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)
    return cache[n]

    # above represents eating one, two and three cookies
    # above represents our recursive cas where there still are some cookies to eat
    
    
    



    #---------------------------------------------------------------------------------------
    # Your code here

    # cookies = 0

    # if n < 0:
    #     return 0
    # if n == 0 or n == 1:
    #     return 1
    # else:
    #     cookies += eating_cookies(n-1)
    #     cookies += eating_cookies(n-2)
    #     cookies += eating_cookies(n-3)

    # return cookies
    # if n == 0:
    #     return 1
    # for i in range(1,5):
    #     if n >= i:
    #         cookies += eating_cookies(n - 1)
    # return cookies


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 900

    print(
        f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to eat {num_cookies} cookies")
