#!/usr/bin/env python3
from ..game_engine import start_game_engine
from ..games.progression_game import progression_rule, start_progression_game


def main():
    start_game_engine(progression_rule, start_progression_game)


if __name__ == '__main__':
    main()
