from turtle import Turtle


class Barrier(Turtle):
    def __init__(self):
        super().__init__()

        #generate long Turtle objects that act as barriers
        self.bottom = Turtle()
        self.bottom.up()
        self.bottom.color("black")
        self.bottom.shape("square")
        self.bottom.shapesize(0.01, 29)
        self.bottom.goto(0, -337)

        self.left = Turtle()
        self.left.up()
        self.left.color("red")
        self.left.shape("square")
        self.left.shapesize(500, 0.01)
        self.left.goto(-252, 0)

        self.top = Turtle()
        self.top.up()
        self.top.color("red")
        self.top.shape("square")
        self.top.shapesize(0.01, 500)
        self.top.goto(0, 347)

        self.right = Turtle()
        self.right.up()
        self.right.color("red")
        self.right.shape("square")
        self.right.shapesize(500, 0.01)
        self.right.goto(241, 0)





