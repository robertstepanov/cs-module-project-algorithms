'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''


# def single_number(nums):
#     no_dups = []

#     # iterate through nums

#     # using an array to hold the dups and then searching through it
#     # one thing that arrays are not great at are searching for a particular value
#     # in the worst case, thats going to beO(n)
#     # what are other data structures that are better suited to being searched?

#     for x in nums: # O(n)
#         if x not in no_dups: # O(n)
#             no_dups.append(x)
#         else:
#             no_dups.remove(x)
#     return no_dups[0] # O(n)
# O(2*n) ~ O(n)
def single_number(nums):
    # keep track of the counts of how many times we've seen a particular number
    # dictionaries are better at being searched
    # very common pattern

    counts = {}
    # O(n)
    # loop through nums to tally up how many times we've seen each number
    for x in nums: # O(1)
        if x in counts:
            del counts[x]
        else:
            counts[x] = 1

    # loop through all the key value pairs in counts to find the one pair whose value is 1
    # O(n)
    for num in counts: 
        if counts[num] == 1:
            return num

    #-------------------------------------------------------------------
    # Your code here

    # for i in range(len(arr)):

    #     duplicate = False

    #     for j in range(len(arr)):

    #         if i != j and arr[i] == arr[j]:
    #             duplicate = True

    #     if not duplicate:
    #         return arr[i]

    # return -1


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
