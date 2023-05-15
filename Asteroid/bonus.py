import random

from pygame import Vector2


class Bonus:
    def __init__(self):
        self.pos = Vector2()
        self.strenght = 1
        '''
        Type
        1 = lifeUp
        2 = speedUp
        3 = projectileUp (number)
        4 = projectileUp (size)
        4 = projectileUp (life)
        5 = shieldProj (duration)
        6 = 
        '''
        self.type = random.randint(1, 5)
        self.lifespan = 5


