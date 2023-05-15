#!/usr/bin/python3

def multiple_returns(sentence):
    length = len(sentence)
    if length == 0:
        result = (0, None)
        return result
    else:
        char_1 = sentence[0]
        return length, char_1
