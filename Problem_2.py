# Imagine you're exploring a sequence of numbers up to a certain limit. Within this sequence, you're on the lookout for pairs of special numbers. These pairs have a unique quality - when you add them together, you get a specific target sum, and both numbers are prime.
# Can you provide a sorted list of these special pairs, following the given criteria?

# Example 1:
# Input: n = 18
# Output: [|5,13],[7,11]]
# Explanation: In this example, there are two special pairs that satisfy the criteria.
# These pairs are [5,13] and [7,11], and we return them in the sorted order as described in the problem statement.

# Example 2:
# Input: n = 13
# Output: [[2,11]]
# the 12,11]] array.
# Explanation: We can show that there is only one pair [2,11] gives a sum of 13, so we return

# Constraints:
#   • 1 <= n <= 1016
# code
from typing import List

def sieve_of_eratosthenes(limit: int) -> List[bool]:
    """Generate a list of booleans indicating primality of numbers up to 'limit'."""
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime
    for i in range(2, int(limit ** 0.5) + 1):
        if is_prime[i]:
            for multiple in range(i * i, limit + 1, i):
                is_prime[multiple] = False
    return is_prime

def special_pairs(n: int) -> List[List[int]]:
    if n < 2:
        return []  # No prime pairs can sum to less than 2
    
    is_prime = sieve_of_eratosthenes(n)
    result = []
    
    for p in range(2, n):
        if is_prime[p] and is_prime[n - p] and p <= n - p:
            result.append([p, n - p])
    
    return result

# READ ME - DO NOT CHANGE
if __name__ == "__main__":
    n = int(input())
    output = special_pairs(n)
    if output == []:
        print("[]")
    else:
        output_str_list = ["[%s]" % ",".join(map(str, combination)) for combination in output]
        output_str = "[%s]" % ",".join(output_str_list)
        print(output_str)
