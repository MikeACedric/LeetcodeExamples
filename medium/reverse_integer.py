"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

7. Reverse Integer
"""
x=123
def reverse(x):
    sign = -1 if x < 0 else 1
    x = abs(x)
    reversed_string = str(x)[::-1]
    reversed_number  = int(reversed_string)
    reversed_number *= sign
    if reversed_number < -2**31 or reversed_number > 2**31-1:
        return 0
    return reversed_number

print("Reversed integer:", reverse(x))
 