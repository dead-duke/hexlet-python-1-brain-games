from random import randint


progression_rule = 'What number is missing in the progression?'


def start_progression_game():
    prog_step = randint(1, 10)
    prog_start = randint(1, 100)
    prog_length = 10
    prog_finish = prog_start + (prog_length * prog_step)
    prog = list(range(prog_start, prog_finish, prog_step))
    prog_hidden_index = randint(0, prog_length - 1)

    question = ''
    for index, value in enumerate(prog):
        if index == prog_hidden_index:
            question += '.. '
        else:
            question += f'{value} '
    question = question.strip()

    correct_answer = prog[prog_hidden_index]
    return (question, str(correct_answer))
