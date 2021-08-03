from animal import Animal
class Lion(Animal):
    def __init__(self, name, age, habitat, heath_level, hapiness_level, melena):
        super().__init__(name, age, habitat, heath_level, hapiness_level)
        self.melena = melena

    def eating(self, eat):
        super().eating()
        if eat < 5:
            self.heath_level += 5
            self.hapiness_level += 5
        elif eat <= 20:
            self.heath_level += 10
            self.hapiness_level += 15
        else:
            self.heath_level += 20
            self.hapiness_level += 25
        return self

    def display_info(self):
        return super().display_info()+('tengo melena' if self.melena == True else 'no tengo melena')