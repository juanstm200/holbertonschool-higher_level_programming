#!/usr/bin/python3
def multiple_returns(sentence):
    if (sentence):
        lent = len(sentence)
        return (lent, sentence[0])
    return (0, None)
