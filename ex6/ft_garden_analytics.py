#!/usr/bin/env python3


class Plant:

    def __init__(self, name, height, age) -> None:
        self.name = name
        self.height = height
        self.age = age


class FloweringPlant(Plant):

    def __init__(self, name, height, age, color) -> None:
        super().__init__(name, height, age)
        self.color = color

    def blooming() -> bool:
        return True


class PrizeFlower(FloweringPlant):

    def __init__(self, name, height, age, color, prize) -> None:
        super().__init__(name, height, age, color)
        self.prize = prize


class Garden:

    def __init__(self, plants: list[Plant]) -> None:
        self.plants = plants


class GardenManager:

    @classmethod
    def create_garden_network(cls, garden: list[Garden]) -> None:
        cls.garden = garden

    class GardenStats:

        @staticmethod
        def calculate_stats() -> None:
            print("calculating stats...")


if __name__ == "__main__":
    rose = PrizeFlower("Rose", 15, 2, "red", 100)
    sunflower = FloweringPlant("Sunflower", 50, 20, "yellow")
    alice = Garden([rose, sunflower])
    manager = GardenManager([alice])
