#!/usr/bin/env python3


class Plant:
    def __init__(self, name, height, age) -> None:
        self.name = name
        self.height = height
        self.age = age


class Garden:
    def __init__(self, plants: list[Plant]) -> None:
        self.plants = plants


class GardenManager:

    @classmethod
    def create_garden_network(cls, garden: Garden) -> None:
        cls.garden = garden


    class GardenStats:

        @staticmethod
        def calculate_stats() -> None:
            print("calculating stats...")
