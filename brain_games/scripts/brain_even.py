#!/usr/bin/env python3
from ..game_engine import game_engine
from ..games.even_game import even_game, even_rule


def main():
    game_engine(even_rule, even_game)


if __name__ == '__main__':
    main()
