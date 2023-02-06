#!/usr/bin/env python3
from ..game_engine import game_engine
from ..games.brain_calc import brain_calc


def main():
    rule = 'What is the result of the expression?'
    game_engine(rule, brain_calc)


if __name__ == '__main__':
    main()
