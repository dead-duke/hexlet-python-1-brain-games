#!/usr/bin/env python3
from ..game_engine import start_game_engine
from ..games.even_game import even_rule, start_even_game


def main():
    start_game_engine(even_rule, start_even_game)


if __name__ == '__main__':
    main()
