class Wolf:
    def __init__(self, current_x, current_y):
        self.x = current_x
        self.y = current_y
        self.hp = 2
        self.picture = '\U0001F43A'
        self.move = None

    def moving(self):
        self.move = randint(1, 9)
        if self.move == 1:
            self.x = self.x - 1
            self.y = self.y - 1
        if self.move == 2:
            self.y = self.y - 1
        if self.move == 3:
            self.x = self.x + 1
            self.y = self.y - 1
        if self.move == 4:
            self.x = self.x - 1
        if self.move == 5:
            pass
        if self.move == 6:
            self.x = self.x + 1
        if self.move == 7:
            self.x = self.x - 1
            self.y = self.y + 1
        if self.move == 8:
            self.y = self.y + 1
        if self.move == 9:
            self.x = self.x + 1
            self.y = self.y + 1

    def dying(self):
        self.picture = '\U0001F7E9'


wolf_amount = 1
wolf = Wolf(4, 1)
wolf.moving()
print(wolf.x, wolf.y)