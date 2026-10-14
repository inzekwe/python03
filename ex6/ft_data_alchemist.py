#!/usr/bin/env python3
import random


def main() -> None:
    """
    Transform player data and compute score statistics
    via comprehensions.
    """
    print("=== Game Data Alchemist ===")
    initial_players = [
        'Alice', 'bob', 'Charlie', 'dylan', 'Emma',
        'Gregory', 'john', 'kevin', 'Liam'
    ]
    print(f"Initial list of players: {initial_players}")

    capitalized_all = [name.capitalize() for name in initial_players]
    print(f"New list with all names capitalized: {capitalized_all}")

    capitalized_only = [name for name in initial_players if name[0].isupper()]
    print(f"New list of capitalized names only: {capitalized_only}")

    score_dict = {name: random.randint(50, 1000) for name in capitalized_all}
    print(f"Score dict: {score_dict}")

    avg_score = sum(score_dict.values()) / len(score_dict)
    print(f"Score average is {avg_score:.2f}")

    high_scores = {
        name: score for name, score in score_dict.items() if score > avg_score
    }
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()
