#!/usr/bin/env python3
from ..game_engine import game_engine
from ..games.prime_game import prime_game, prime_rule


def main():
    game_engine(prime_rule, prime_game)


if __name__ == '__main__':
    main()
