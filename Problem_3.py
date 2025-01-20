# You are using proxy server and Imagine you are given a string named proxy, which is essentially an unparsed string of numbers, sub-divided by decimals (.) or colons (:). Your quest is to determine what kind of treasure this string holds.
# Is it a secret IPv4 code reflected by the format "x1.x2.X3.X4"? An IPv4 code is an elusive four-segment code where each segment (xi) ranges from 0 to 255 and does not keep any leading zeroes in hiding. For instance, famous IPv4 sequences like "192.168.1.1" and "192.168.1.0" are valid, but wannabe sequences like "192.168.01.1", "192.168.1.00"' and "192.168@1.1" are invalid as they disobey the code of IPv4 formatting laws.
# Or is it conveying an IPv6 message encapsulated in the format "x1:x2:x3:x4:x5:x6:x7 :x8"?
# Here, every xi segment can host between 1 to 4 characters. This mysterious string is allowed to contain digits, lowercase English letters ('a' to 'f'), or uppercase English letters ('A' to 'F'), and leading zeros are welcomed. Valid IPv6 messages could be
# "1990:0db8:85a3:0000:0000:8a2e:0370:7334" or "1990:db8:85a3:0:0:8A2E:0370:7334"
# ', while
# "1990:0db8:85a3::8A2E:037j:7334" and "01990:0db8:85a3:0000:0000:8a2e:0370:7334" fail as authentic IPv6 messages.
# If the proxy does not unlock a valid IPv4 or IPv6 message, return "Neither"; the string holds no treasure. So, will you be able to decipher this code?
# Example 1:
# Input: proxy = "172.16.254.1"
# Output: "IPv4"
# Explanation: This is a valid IPv4 address, return "IPv4".
# Example 2:
# Input: proxy = "1990:0db8:85a3:0:0:8A2E
# Something wrong with the question or blank content?
# Output: "IPv6"
# Explanation: This is a valid IPv6 address,
# code

from typing import List

def validIPAddress(queryIP: str) -> str:
    def isIPv4(segment: str) -> bool:
        # Check if the segment is a valid IPv4 segment
        if not segment.isdigit():
            return False
        if not (0 <= int(segment) <= 255):
            return False
        if len(segment) > 1 and segment[0] == '0':  # No leading zeroes
            return False
        return True

    def isIPv6(segment: str) -> bool:
        # Check if the segment is a valid IPv6 segment
        if len(segment) < 1 or len(segment) > 4:
            return False
        for char in segment:
            if not (char.isdigit() or char.lower() in "abcdef"):
                return False
        return True

    # Check for IPv4
    if queryIP.count('.') == 3:
        parts = queryIP.split('.')
        if all(isIPv4(part) for part in parts):
            return "IPv4"

    # Check for IPv6
    if queryIP.count(':') == 7:
        parts = queryIP.split(':')
        if all(isIPv6(part) for part in parts):
            return "IPv6"

    # Neither
    return "Neither"

# READ ME - DO NOT CHANGE
if __name__ == "__main__":
    a = input()
    output = validIPAddress(a)
    print(output)
