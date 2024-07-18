# Task 3 (Optional Task)
# In many programming languages, we deal with expressions enclosed by delimiter characters,
# such as round ( ), square [ ], or curly brackets { }.
# Write a program that reads a string with a sequence of delimiter characters, such as
# ( ) { [ ] ( ) ( ) { } } }, and provides an appropriate message when the delimiters are symmetrical,
# asymmetrical, like ( ( ( ) , or when the delimiters of different types are paired, like ( }.
# 💡 Use a stack to remember the currently open delimiter characters.
# Example of expected results:
# ( ){[ 1 ]( 1 + 3 )( ){ }}: Symmetrical
# ( 23 ( 2 - 3);: Asymmetrical
# ( 11 }: Asymmetrical


def check_delims(sequence):
    stack = []
    matching_pairs = {')': '(', ']': '[', '}': '{'}
    
    for char in sequence:
        if char in matching_pairs.values():
            stack.append(char)
        elif char in matching_pairs.keys():
            if stack and stack[-1] == matching_pairs[char]:
                stack.pop()
            else:
                return "Asymmetrical"
    return "Symmetrical" if not stack else "Asymmetrical"

sequence = input("Enter some sequence of delimiter characters >>> ")
print(check_delims(sequence))
