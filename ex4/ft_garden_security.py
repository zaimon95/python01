#!/usr/bin/env python3
"""A module that creates a plant in a secure way."""


class SecurePlant:
    """A secure plant where the attributes are protrected."""

    def __init__(self, name) -> None:
        """Construct a SecurePlant.

        :param name:
            The name of the plant. It'a a string.
        """
        self.name = name

    def set_height(self, height) -> None:
        """Setter for height.

        :param height:
            The height of the plant. it's a number and cannot be negative.
        """
        if (height <= 0):
            print()
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected\n")
        else:
            self.__height = height
            print(f"Height updated: {height}cm [OK]")

    def set_age(self, age) -> None:
        """Setter for age.

        :param age:
            The age of the plant. it's a number and cannot be negative.
        """
        if (age <= 0):
            print()
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected\n")
        else:
            self.__age = age
            print(f"Age updated: {age} days [OK]")

    def get_height(self) -> int:
        """Getter for height.

        :returns:
            The height of the plant.
        """
        return self.__height

    def get_age(self) -> int:
        """Getter for age.

        :returns:
            The age of the plant
        """
        return self.__age


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = SecurePlant("Rose")
    print(f"Plant created: {rose.name}")
    rose.set_height(25)
    rose.set_age(30)
    rose.set_height(-5)
    print(f"Current plant: {rose.name} ", end='')
    print(f"({rose.get_height()}cm, {rose.get_age()} days)")
