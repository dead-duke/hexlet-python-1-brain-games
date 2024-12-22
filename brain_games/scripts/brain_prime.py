#!/usr/bin/env python3
from ..game_engine import start_game_engine
from ..games.prime_game import prime_rule, start_prime_game


def main():
    start_game_engine(prime_rule, start_prime_game)


if __name__ == '__main__':
    main()
