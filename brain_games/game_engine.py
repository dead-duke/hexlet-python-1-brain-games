from .cli import get_user_answer, greetings_user


def start_game_engine(rule, start_game):
    user_name = greetings_user()
    print(rule)

    for _ in range(3):
        (question, correct_answer) = start_game()
        print(f'Question: {question}')
        user_answer = get_user_answer()
        if user_answer != correct_answer:
            message = f"'{user_answer}' is wrong answer ;(."
            message += f" Correct answer was '{correct_answer}'.\n"
            message += f"Let's try again, {user_name}!"
            print(message)
            return
        print('Correct!')

    print(f'Congratulations, {user_name}!')
