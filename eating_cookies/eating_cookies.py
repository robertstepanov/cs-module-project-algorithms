'''
Input: an integer
Returns: an integer
'''


def eating_cookies(n):
    # Your code here

    cookies = 0

    if n < 0:
        return 0
    if n == 0 or n == 1:
        return 1
    else:
        cookies += eating_cookies(n-1)
        cookies += eating_cookies(n-2)
        cookies += eating_cookies(n-3)

    return cookies
    # if n == 0:
    #     return 1
    # for i in range(1,5):
    #     if n >= i:
    #         cookies += eating_cookies(n - 1)
    # return cookies


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(
        f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
