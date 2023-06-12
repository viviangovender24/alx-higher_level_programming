#!/usr/bin/python3
def multiple_returns(sentence):
    le = len(sentence)
    return (le, sentence[0] if le > 0 else None)
