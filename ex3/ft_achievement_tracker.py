#!/usr/bin/env python3
import random

ALL_POSSIBLE_ACHIEVEMENTS = [
    'Crafting Genius', 'Strategist', 'World Savior', 'Speed Runner',
    'Survivor', 'Master Explorer', 'Treasure Hunter', 'Unstoppable',
    'Hidden Path Finder', 'First Steps', 'Collector Supreme',
    'Untouchable', 'Sharp Mind', 'Boss Slayer'
]


def gen_player_achievements() -> set[str]:
    """Generate a random set of achievements for a player."""
    count = random.randint(3, len(ALL_POSSIBLE_ACHIEVEMENTS))
    return set(random.sample(ALL_POSSIBLE_ACHIEVEMENTS, count))


def main() -> None:
    """Analyze achievement sets across players using set operations."""
    print("=== Achievement Tracker System ===")
    players = {
        "Alice": gen_player_achievements(),
        "Bob": gen_player_achievements(),
        "Charlie": gen_player_achievements(),
        "Dylan": gen_player_achievements()
    }

    for name, ach in players.items():
        print(f"Player {name}: {ach}")

    all_distinct = set().union(*(players.values()))
    print(f"All distinct achievements: {all_distinct}")

    common = set.intersection(*(players.values()))
    print(f"Common achievements: {common}")

    all_ach_set = set(ALL_POSSIBLE_ACHIEVEMENTS)

    for name, ach in players.items():
        others_union = set().union(*(
            ach_set for p_name, ach_set in players.items() if p_name != name
        ))
        only_this = ach - others_union
        print(f"Only {name} has: {only_this}")

    for name, ach in players.items():
        missing = all_ach_set - ach
        print(f"{name} is missing: {missing}")


if __name__ == "__main__":
    main()
