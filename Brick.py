from turtle import Turtle

#brick object that has specified dimensions 10px by 20px
#each instance identifiable by row and column of placement

#inherits the Turtle class


class Brick(Turtle):
    def __init__(self, row, column, color):
        super().__init__()
        #ensure pen is up for each instance
        self.up()
        self.row = row
        self.column = column
        self.shape("square")
        self.shapesize(0.25, 0.25)
        self.color(color)
        self.color_name = color


    def destroy(self):
        self.hideturtle()



    #identifiable by string: "Brick (row num, col num)"
    def __repr__(self):
        return f"Brick{self.row,self.column}"


