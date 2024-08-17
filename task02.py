# Task 2
# It is necessary to develop a function that takes a string as an input parameter,
# adds all its characters to a deque (from the collections module in Python),
# and then compares the characters from both ends of the deque to determine if the string is a palindrome.
# The program should correctly handle both even and odd length strings,
# and be case-insensitive and whitespace-insensitive.

from collections import deque

def is_palindrome(entered_str):
    # Convert the string to lower case and remove non-alphanumeric characters
    entered_str = ''.join(char.lower() for char in entered_str if char.isalnum())
    # Add all characters to a deque
    dq = deque(entered_str)
    # Compare characters from both ends of the deque
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    return True


entered_str = input("Enter some text >>> ")
print(is_palindrome(entered_str))