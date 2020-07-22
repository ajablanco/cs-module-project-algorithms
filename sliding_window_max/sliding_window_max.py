'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
# iterate through by the number of k 
# initialize start and end of window length
    start = 0
    end = k
    # create new array for the max values 
    new_arr = []
    for i in nums:
        # create window variable from beg index to end index
        window = nums[start:end]
        # find max value within the window
        new_arr.append(max(window))
        # increment the beg index and end index as long as the last index is < nums length
        if end < len(nums):
            start += 1
            end += 1
        else:
            break
    return new_arr




if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
