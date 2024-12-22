from random import randint

even_rule = 'Answer "yes" if the number is even, otherwise answer "no".'


def start_even_game():
    question = randint(1, 100)
    correct_answer = 'yes' if question % 2 == 0 else 'no'
    return (question, correct_answer)
