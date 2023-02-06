#!/usr/bin/env python3
from ..game_engine import game_engine
from ..games.calc_game import calc_game, calc_rule


def main():
    game_engine(calc_rule, calc_game)


if __name__ == '__main__':
    main()
