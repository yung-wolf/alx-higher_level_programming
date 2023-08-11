#!/usr/bin/python3

# Function to print alphabets in UPPERCASE
def print_alphabets():
    for char in range(ord('A'), ord('Z') + 1):
        print("{:c}".format(char), end="")
        if str(char) == 'Z':
            break
    print()  
