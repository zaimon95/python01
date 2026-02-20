# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_growth.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sla-gran <sla-gran@student.s19.be>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/20 11:50:25 by sla-gran          #+#    #+#              #
#    Updated: 2026/02/20 11:50:25 by sla-gran         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/env python3


class Plant:

    def __init__(self, name, height, days) -> None:
        self.name = name
        self.height = height
        self.days = days

    def __str__(self) -> str:
        return f"{self.name}: {self.height}cm, {self.days} days old"

    def grow(self) -> None:
        self.height += 1

    def age(self) -> None:
        self.days += 1
        self.grow()

    def get_info(self) -> str:
        return self.__str__()


if __name__ == "__main__":
    p1 = Plant("Rose", 25, 30)
    p2 = Plant("Sunflower", 30, 15)
    p3 = Plant("cactus", 15, 20)
    plants = [p1, p2, p3]
    for plant in plants:
        growth: int = 0
        for i in range(1, 8):
            if i == 1 or i == 7:
                print(f"=== Day {i} ===")
                print(plant.get_info())
            plant.age()
            growth += 1
            if i == 6:
                print(f"Growth this week: +{growth}cm")
