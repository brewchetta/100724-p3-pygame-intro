class Creature:

    alive_creatures = []
    dead_creatures = []

    def __init__(self, pos_x, pos_y, alive_image, dead_image):
        self.x = pos_x
        self.y = pos_y
        self.alive_image = alive_image
        self.dead_image = dead_image
        self.alive = True
        self.__class__.alive_creatures.append(self)

    def remove(self):
        self.__class__.alive_creatures.remove(self)
        self.__class__.dead_creatures.append(self)