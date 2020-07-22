'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # if el is zero, del from list
    non_zero = [i for i in arr if i != 0]
    zero = [i for i in arr if i == 0]
    non_zero.extend(zero)
    return non_zero

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")