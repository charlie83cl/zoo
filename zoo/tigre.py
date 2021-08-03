from animal import Animal


class Tiger(Animal):
    def __init__(self, name, age, habitat, heath_level, hapiness_level):
        super().__init__(name, age, habitat, heath_level, hapiness_level)

    def eating(self, eat):
        if eat < 7:
            self.heath_level += 8
            self.hapiness_level += 10
        elif eat <= 20:
            self.heath_level += 15
            self.hapiness_level += 20
        else:
            self.heath_level += 22
            self.hapiness_level += 28
        return self

    def display_info(self):
        return super().display_info()+('y soy un animal rayado')
