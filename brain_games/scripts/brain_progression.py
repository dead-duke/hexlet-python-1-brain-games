#!/usr/bin/env python3
from ..game_engine import game_engine
from ..games.progression_game import progression_game, progression_rule


def main():
    game_engine(progression_rule, progression_game)


if __name__ == '__main__':
    main()
