# You are given an array nums consisting of positive integers where all integers have the same number of digits.
# The digit difference between two integers is the count of different digits that are in the same position in the two integers.
# Return the sum of the digit differences between all pairs of integers in nums.
# Example 1:
# Input: nums = [13,23,12]
# Output: 4
# Explanation:
# We have the following:
# - The digit difference between 13 and 23 is 1.
# - The digit difference between 13 and 12 is 1.
# - The digit difference between 23 and 12 is 2.
# So the total sum of digit differences between all pairs of integers is 1 + 1 + 2 = 4.
# Example 2:
# Input: nums = [10,10,10,10]
# Output: 0
# Explanation:
# All the integers in the array are the same. So the total sum of digit differences between all pairs of integers will be 0.
# Constraints:
# • 2 <= nums.length <= 10^5
# • 1 <= nums[il < 101g
# • All integers in nums have the same number of digits.
def solution(nums):
    # Convert integers to strings for easy digit comparison
    nums = [str(num) for num in nums]
    num_length = len(nums[0])  # Number of digits in each number
    n = len(nums)  # Total numbers in the array
    
    # Initialize an array to count occurrences of digits at each position
    digit_count = [[0] * 10 for _ in range(num_length)]
    
    # Count occurrences of each digit in every position
    for num in nums:
        for i, digit in enumerate(num):
            digit_count[i][int(digit)] += 1
    
    # Calculate the total digit differences
    total_difference = 0
    for i in range(num_length):  # For each digit position
        for d in range(10):  # For each digit from 0-9
            count_d = digit_count[i][d]
            total_difference += count_d * (n - count_d)  # Difference contribution for digit d
    
    # Since each pair is counted twice, divide the result by 2
    return total_difference // 2

# READ ME - DO NOT CHANGE
if __name__ == "__main__":
    line = input()  # Input as a string
    nums = [int(num) for num in line[1:-1].split(",")]  # Parse input into a list of integers
    print(solution(nums))


