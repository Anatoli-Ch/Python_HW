# You are given the firstname and lastname of a person on two different lines.
# Your task is to read them and print the following:
# Hello firstname lastname! You just delved into python.
# Input Format
# The first line contains the first name, and the second line contains the last name.
# Constraints
# The length of the first and last name ≤ .
# Output Format
# Print the output as mentioned above.
# Sample Input 0
# Ross
# Taylor
# Sample Output 0
# Hello Ross Taylor! You just delved into python.


def print_full_name(a, b):
    if len(a) and len(b) < 10:
        return 'Hello {} {}! You just delved into python.'.format(a, b)
    else:
        return 'first name or second name is to long'


first_name = input('Enter first name: ')
second_name = input('Enter second name: ')
print(print_full_name(first_name, second_name))
