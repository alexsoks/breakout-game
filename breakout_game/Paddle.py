from turtle import Turtle, Screen
from Barrier import Barrier

#paddle class that intially consists of paddle that takes in the Brickplacer object and uses its
# brick_data attribute to determine when it should reduce by half

class Paddle(Turtle):
    def __init__(self, barrier: Barrier):
        super().__init__()

        self.barrier = barrier
        #list of segments that will store the different parts of the paddle
        self.segments = {}

        #place paddle in starting position and fill up the segments dictionary with the paddle elements


        center_xpos = 0

        #place initial segment
        t = Turtle()
        t.up()
        t.color("pink")
        t.shape("square")
        t.shapesize(0.3, 0.6)
        t.goto(center_xpos, -240)
        #place in dictionary
        self.segments["middle"] = t




        for i in [12, 24]:
            #place a segment on both sides
            t1 = Turtle()
            t1.up()
            t1.color("pink")
            t1.shape("square")
            t1.shapesize(0.3, 0.6)
            t1.goto(center_xpos + i, -240)
            #place in dictionary
            if i == 12:
                self.segments["r1"] = t1
            else:
                self.segments["r2"] = t1


            t2 = Turtle()
            t2.up()
            t2.color("pink")
            t2.shape("square")
            t2.shapesize(0.3, 0.6)
            t2.goto(center_xpos - i, -240)
            if i == 12:
                self.segments["l1"] = t2
            else:
                self.segments["l2"] = t2



    # movement functions

    def move_right(self):

        if self.segments["r2"].xcor()+2 <= self.barrier.right.xcor()-14:
            for (pos, segment) in self.segments.items():
                segment.goto(segment.xcor()+40, segment.ycor())


    def move_left(self):

        if self.segments["l2"].xcor() - 4 >= self.barrier.left.xcor() +16:
            for (pos, segment) in self.segments.items():
                segment.goto(segment.xcor()-40, segment.ycor())



    #function that allows you to define an x coordinate, and the middle segment moves there
    def move_to(self, x):
        #first move the middle segment to x coordinate
        self.segments["middle"].goto(x, -240)

        #now move the other segments to positions corresponding to this new centre x coordinate
        for i in [12, 24]:
            if i == 12:
                self.segments["r1"].goto(x + i, -240)
                self.segments["l1"].goto(x - i, -240)

            else:
                self.segments["r2"].goto(x + i, -240)
                self.segments["l2"].goto(x - i, -240)



    #move_to function for the half paddle
    def move_to_b(self, x):
        # first move the middle segment to x coordinate
        self.segments["middle"].goto(x, -240)

        # now move the other segments to positions corresponding to this new centre x coordinate
        for i in [6, 12]:
            if i == 6:
                self.segments["r1"].goto(x + i, -240)
                self.segments["l1"].goto(x - i, -240)

            else:
                self.segments["r2"].goto(x + i, -240)
                self.segments["l2"].goto(x - i, -240)








    def half_paddle(self):

        #get current position of middle segment
        current_x_pos = self.segments["middle"].xcor()


        #clear current paddle
        for (pos, seg) in self.segments.items():
            seg.hideturtle()
            self.segments[pos] = "o"





        #generate new paddle
        center_xpos = current_x_pos

        # place initial segment
        t = Turtle()
        t.up()
        t.color("pink")
        t.shape("square")
        t.shapesize(0.3, 0.3)
        t.goto(center_xpos, -240)
        # place in dictionary
        self.segments["middle"] = t

        for i in [6, 12]:
            # place a segment on both sides
            t1 = Turtle()
            t1.up()
            t1.color("pink")
            t1.shape("square")
            t1.shapesize(0.3, 0.3)
            t1.goto(center_xpos + i, -240)
            # place in dictionary
            if i == 6:
                self.segments["r1"] = t1
            else:
                self.segments["r2"] = t1

            t2 = Turtle()
            t2.up()
            t2.color("pink")
            t2.shape("square")
            t2.shapesize(0.3, 0.3)
            t2.goto(center_xpos - i, -240)
            if i == 6:
                self.segments["l1"] = t2
            else:
                self.segments["l2"] = t2














