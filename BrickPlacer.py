from turtle import Screen
from Brick import Brick
from Scoreboard import Scoreboard

#BrickPlacer object creates the game's coloured brick structure, assigning specific colours, rows, columns
#and points to each brick and then storing each instance in a structured dictionary for reference



class BrickPlacer:

    def __init__(self, scoreboard:Scoreboard):
        # class stores each brick instance, identifiable by
        self.brick_data = {
            0: {},
            1: {},
            2: {},
            3: {},
            4: {},
            5: {},
            6: {},
            7: {}
        }

        #parameter to determine whether blocks have been rebuilt for round 2 or not
        self.rebuild = False
        self.game_fin = False
        self.scoreboard = scoreboard
    def build(self):
        #list of (y-coordinates, colour) for class to plot the bricks on the screen
        row_heights = [(0, 190, "yellow"), (1, 200, "yellow"), (2, 210, "green"), (3, 220, "green"),
                       (4, 230, "orange"), (5, 240, "orange"), (6, 250, "red"), (7, 260, "red")]




        for row, y_val, colour in row_heights:
            #create a row of 14 blocks, with the colour dependent on the row
            x = -246  #-229
            for i in range(14):
                brick_list = []
                for j in range(6):
                    b = Brick(row=row, column=i, color=colour)
                    b.goto(x, y_val)
                    brick_list.append(b)
                    # store each brick instance in the brick_data dictionary:
                    self.brick_data[row][b.column] = brick_list
                    x += 5

                x += 5



    def delete_block(self, element: Brick):

        for seg in self.brick_data[element.row][element.column]:
            seg.destroy()

        #remove brick key-value pair from overall dictionary
        self.brick_data[element.row][element.column] = []
















































