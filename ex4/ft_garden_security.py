class SecurePlant:
    def __init__(self, name, height, age) -> None:
        self.name = name
        self.height = height
        self.age = age
    def set_height(self, height) -> None:
        self.height = height
    def set_age(self, age) -> None:
        self.age = age
    def get_height(self) -> int:
        return self.height
    def get_age(self) -> int:
        return self.age

