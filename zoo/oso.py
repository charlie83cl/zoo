from animal import Animal


class Bear(Animal):
    def __init__(self, name, age, habitat, heath_level, hapiness_level, bear_type):
        super().__init__(name, age, habitat, heath_level, hapiness_level)
        self.bear_type = bear_type

    def display_info(self):
        if self.bear_type == 1:
            return super().display_info()+('y soy un oso Pardo')
        elif self.bear_type == 2:
            return super().display_info()+('y soy un oso Grizzly')
        elif self.bear_type == 3:
            return super().display_info()+('y soy un oso Negro')
        else:
            return super().display_info()+('y soy un oso cualquiera')