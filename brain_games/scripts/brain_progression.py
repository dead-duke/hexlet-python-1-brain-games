#!/usr/bin/env python3
from ..game_engine import game_engine
from ..games.brain_progression import brain_progression


def main():
    rule = 'What number is missing in the progression?'
    game_engine(rule, brain_progression)


if __name__ == '__main__':
    main()
