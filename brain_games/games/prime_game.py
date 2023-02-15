from random import randint


prime_rule = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def start_prime_game():
    number = randint(1, 100)
    question = f'{number}'
    for divisor in range(1, number // 2):
        if (number % divisor == 0 and divisor != 1 and number != divisor):
            correct_answer = 'no'
            return (question, correct_answer)
    correct_answer = 'yes' if number != 1 else 'no'
    return (question, correct_answer)
