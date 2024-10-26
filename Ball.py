from turtle import Turtle




class Ball(Turtle):
    #takes in the Brickplacer, Barrier, Screen and Paddle objects for collision detection
    def __init__(self):
        super().__init__()

        self.up()
        self.shape('square')
        self.color('white')
        self.shapesize(0.2, 0.2)
        self.speed = 5















