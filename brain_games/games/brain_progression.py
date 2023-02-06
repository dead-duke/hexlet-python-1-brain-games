#!/usr/bin/env python3
from random import randint


def brain_progression():
    progression_step = randint(1, 10)
    progression_start = randint(1, 100)
    progression_length = 10
    progression_finish = progression_start + (progression_length * progression_step)
    progression = list(range(progression_start, progression_finish, progression_step))
    progression_empty_value = randint(0, progression_length - 1)

    question = ''
    for index, value in enumerate(progression):
        if index == progression_empty_value:
            question += '... '
        else:
            question += f'{value} '
    question = question.strip()

    correct_answer = progression[progression_empty_value]
    return (question, str(correct_answer))
