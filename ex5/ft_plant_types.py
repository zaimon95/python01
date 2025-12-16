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
        shade: int = self.height * self.trunk_diameter
        print(f"{self.name} provides {shade} square meters of shade")


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

    def nutrition(self) -> None:
        """Print what nutritional value the vegetable gives."""
        print(f"{self.name} is rich in {self.nutritional_value}")
