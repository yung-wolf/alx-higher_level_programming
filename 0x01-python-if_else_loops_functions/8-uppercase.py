#!/usr/bin/python3

def uppercase(str):
    word = ""

    for char in str:
        if ord('a') <= ord(char) <= ord('z'):
            char = chr(ord(char) - 32)
            word += char
        else:
            word += char
    print("{}".format(word))
