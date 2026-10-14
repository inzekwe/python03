#!/usr/bin/env python3
import random
from typing import Generator

PLAYERS = ["alice", "bob", "charlie", "dylan"]
ACTIONS = [
    "run", "eat", "sleep", "grab", "move", "climb", "swim", "use", "release"
]


def gen_event() -> Generator[tuple[str, str], None, None]:
    """Endless generator yielding random player events."""
    while True:
        player = random.choice(PLAYERS)
        action = random.choice(ACTIONS)
        yield (player, action)


def consume_event(
    events_list: list[tuple[str, str]]
) -> Generator[tuple[str, str], None, None]:
    """Generator that randomly consumes and yields items from a list."""
    while events_list:
        index = random.randint(0, len(events_list) - 1)
        event = events_list.pop(index)
        yield event


def main() -> None:
    """Simulate streaming events and consuming lists via generators."""
    print("=== Game Data Stream Processor ===")
    event_gen = gen_event()

    for i in range(1000):
        player, action = next(event_gen)
        print(f"Event {i}: Player {player} did action {action}")

    ten_events = [next(event_gen) for _ in range(10)]
    print(f"Built list of 10 events: {ten_events}")

    for ev in consume_event(ten_events):
        print(f"Got event from list: {ev}")
        print(f"Remains in list: {ten_events}")


if __name__ == "__main__":
    main()
