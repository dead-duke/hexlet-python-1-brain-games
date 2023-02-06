#!/usr/bin/env python3
from random import randint


def brain_progression():
    prog_step = randint(1, 10)
    prog_start = randint(1, 100)
    prog_length = 10
    prog_finish = prog_start + (prog_length * prog_step)
    prog = list(range(prog_start, prog_finish, prog_step))
    prog_empty_value = randint(0, prog_length - 1)

    question = ''
    for index, value in enumerate(prog):
        if index == prog_empty_value:
            question += '... '
        else:
            question += f'{value} '
    question = question.strip()

    correct_answer = prog[prog_empty_value]
    return (question, str(correct_answer))
