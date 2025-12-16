#!/usr/bin/env python3
"""A module for all types of Plants."""


class Plant:
    """A class of a plant."""

    def __init__(self, name, height, age) -> None:
        """
        Construct a plant with his name, height and age.

        :param name str: the name of the plant.
        :param height int: the height of the plant in cm.
        :param age int: the age of the plant in days.
        """
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    """A type of plant that is a flower."""

    def __init__(self, name, height, age, color) -> None:
        """
        Construct a flower which is a plant with a color.

        :param name str: the name of the flower.
        :param height int: the height of the flower in cm.
        :param age int: the age of the flower in days.
        :param color str: the color of the flower.
        """
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        """Print a message saying the flower blooms."""
        print(f"{self.name} is blooming beatifully!")

    def print_flower(self) -> None:
        """Print what is needed for a flower."""
        print(f"{rose.name} ({type(rose).__name__}):", end=" ")
        print(f"{rose.height}cm, {rose.age} days, {rose.color} color")
        self.bloom()
        print()


class Tree(Plant):
    """A type of plant that is actually a tree."""

    def __init__(self, name, height, age, trunk_diameter) -> None:
        """
        Construct a tree which inherits Plant but with a trunk_diameter.

        :param name str: the name of the tree
        :param height int: the height of the tree in cm
        :param age int: the age of the tree in days
        :param trunk_diameter int: the diameter of the trunk of the tree in cm
        """
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        """Print the surface of the shade the tree will produce."""
        shade: int = (self.height * self.trunk_diameter) // 1000
        print(f"{self.name} provides {shade} square meters of shade")

    def print_tree(self) -> None:
        """Print the explanation of the tree."""
        print(f"{self.name} ({type(self).__name__}):", end=" ")
        print(f"{self.height}cm, {self.age} days,", end=" ")
        print(f"{self.trunk_diameter}cm diameter")
        self.produce_shade()
        print()


class Vegetable(Plant):
    """A type of plant which is a vegetable."""

    def __init__(self, name, height, age, harvest_season, nutritional_value):
        """
        Construct a vegetable which is a plant with a harvest_season.

        :param name str: the name of the vegetable
        :param height int: the height of the vegetable in cm
        :param age int: the age of the vegetable in days
        :param harvest_season str: the season at which you harvest the
        vegetable (summer, fall, winter, spring)
        :param nutritional_value str: what the vegetable gives as benefits
        to the body when eating it
        """
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def print_veg(self) -> None:
        """Print what is needed for a vegetable."""
        print(f"{self.name} ({type(self).__name__}):", end=" ")
        print(f"{self.height}cm, {self.age} days,", end=" ")
        print(f"{self.harvest_season} harvest")
        print(f"{self.name} is rich in {self.nutritional_value}")
        print()


if __name__ == "__main__":
    print("=== Garden Plant Types ===\n")
    rose = Flower("Rose", 25, 30, "red")
    rose.print_flower()
    oak = Tree("Oak", 500, 1825, 50)
    oak.print_tree()
    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    tomato.print_veg()
