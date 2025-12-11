#!/usr/bin/env python3


class Plant:

    def __init__(self, name, height, days) -> None:
        self.name = name
        self.height = height
        self.days = days

    def grow(self) -> None:
        self.height += 1

    def age(self) -> None:
        self.days += 1
        self.grow()

    def get_info(self) -> None:
        return f"{self.name}: {self.height}cm, {self.days} days old"


if __name__ == "__main__":
    p1 = Plant("Rose", 25, 30)
    growth: int = 0
    print("=== Day 1 ===")
    print(p1.get_info())
    print("=== Day 7 ===")
    p1.age()
    p1.age()
    p1.age()
    p1.age()
    p1.age()
    p1.age()
    print(p1.get_info())
    print(f"Growth this week: +{growth}cm")
