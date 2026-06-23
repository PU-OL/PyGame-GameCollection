class cell():
    def __init__(self, x_cord, y_cord):
        self.x = x_cord
        self.y = y_cord

        self.filled = False
        self.conn = [False, False, False, False]  # [Up, Right, Down, Left]
        self.group = -1