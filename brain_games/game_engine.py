from .cli import welcome_user, get_user_answer


def game_engine(rule, game):
    user_name = welcome_user()
    print(rule)

    for _ in range(3):
        (question, correct_answer) = game()
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
