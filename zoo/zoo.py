# from animal import Animal
from leon import Lion
from tigre import Tiger
from oso import Bear


class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name

    def add_animal(self, new_animal):
        for animal in self.animals:
            if animal.name == new_animal.name:
                return False
        self.animals.append(new_animal)
        return True

    def remove_animal(self, free_animal):
        for animal in self.animals:
            if animal.name == free_animal.name:
                self.animals.remove(free_animal)
                return True
            else:
                return False

    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            print(animal.display_info())
