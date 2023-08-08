#!/usr/bin/python3

def islower(c):
    i = 0

    for letter in range(ord('a'), ord('z') + 1):
        if c == chr(letter):  # Compare w/ char 'c'
            return True
        i += 1

    if i == 26:
        return False
