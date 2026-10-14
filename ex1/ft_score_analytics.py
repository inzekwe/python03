#!/usr/bin/env python3
import sys


def main() -> None:
    """Process and analyze game scores from command-line arguments."""
    print("=== Player Score Analytics ===")
    args = sys.argv[1:]
    if not args:
        print(
            "No scores provided. Usage: "
            "python3 ft_score_analytics.py <score1> <score2>"
        )
        return

    valid_scores: list[int] = []
    for arg in args:
        try:
            score = int(arg)
            valid_scores.append(score)
        except ValueError:
            print(f"Invalid parameter: '{arg}'")

    if not valid_scores:
        print(
            "No scores provided. Usage: "
            "python3 ft_score_analytics.py <score1> <score2>"
        )
        return

    print(f"Scores processed: {valid_scores}")
    total_players = len(valid_scores)
    total_score = sum(valid_scores)
    average_score = total_score / total_players
    high_score = max(valid_scores)
    low_score = min(valid_scores)
    score_range = high_score - low_score

    print(f"Total players: {total_players}")
    print(f"Total score: {total_score}")
    print(f"Average score: {average_score}")
    print(f"High score: {high_score}")
    print(f"Low score: {low_score}")
    print(f"Score range: {score_range}")


if __name__ == "__main__":
    main()
