#!/usr/bin/env python3
import sys


def main() -> None:
    """
    Parse inventory arguments, calculate item percentages,
    and update items.
    """
    print("=== Inventory System Analysis ===")
    args = sys.argv[1:]
    inventory: dict[str, int] = {}
    seen_items: set[str] = set()

    for arg in args:
        if ":" not in arg:
            print(f"Error invalid parameter '{arg}'")
            continue
        parts = arg.split(":", 1)
        item = parts[0].strip()
        qty_str = parts[1].strip()

        if item in seen_items:
            print(f"Redundant item '{item}' discarding")
            continue

        try:
            qty = int(qty_str)
        except ValueError as e:
            print(f"Quantity error for '{item}': {e}")
            continue

        seen_items.add(item)
        inventory[item] = qty

    print(f"Got inventory: {inventory}")
    item_list = list(inventory.keys())
    print(f"Item list: {item_list}")

    total_qty = sum(inventory.values())
    print(f"Total quantity of the {len(inventory)} items: {total_qty}")

    for item, qty in inventory.items():
        percentage = (qty / total_qty) * 100 if total_qty > 0 else 0.0
        print(f"Item {item} represents {percentage:.1f}%")

    if inventory:
        most_abundant = max(inventory.items(), key=lambda x: x[1])
        least_abundant = min(inventory.items(), key=lambda x: x[1])
        print(
            f"Item most abundant: {most_abundant[0]} "
            f"with quantity {most_abundant[1]}"
        )
        print(
            f"Item least abundant: {least_abundant[0]} "
            f"with quantity {least_abundant[1]}"
        )

    inventory["magic_item"] = 1
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
