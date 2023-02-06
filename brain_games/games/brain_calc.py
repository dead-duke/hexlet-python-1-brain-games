#!/usr/bin/env python3
from random import randint


def brain_calc():
    operand_one = randint(1, 100)
    operand_two = randint(1, 100)
    sign = randint(1, 3)
    if sign == 1:
        sign = '+'
        correct_answer = operand_one + operand_two
    if sign == 2:
        sign = '-'
        correct_answer = operand_one - operand_two
    if sign == 3:
        sign = '*'
        correct_answer = operand_one * operand_two
    question = f'{operand_one} {sign} {operand_two}'
    return (question, str(correct_answer))
