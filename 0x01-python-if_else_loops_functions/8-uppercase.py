#!/usr/bin/python3

def uppercase(str):
    for char in str:
        if ord('A') <= ord(char) <= ord('Z'):
            print(char, end="")
        elif ord('a') <= ord(char) <= ord('z'):
            char = chr(ord(char) - 32)
            print(char, end="")
        else:
            print(char, end="")

    print()
