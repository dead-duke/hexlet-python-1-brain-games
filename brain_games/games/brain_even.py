#!/usr/bin/env python3
from random import randint


def brain_even():
    question = randint(1, 100)
    correct_answer = 'yes' if question % 2 == 0 else 'no'
    return (question, correct_answer)
