#Class responsible for keeping track of the score; Takes in a Brickplacer object and counts all the bricks
#that are present in the brick_data dictionary to form the score which will be displayed at the top right of screen

from turtle import Turtle





class Scoreboard:

    def __init__(self):
        self.score = 0
        self.lives = 3
        self.element_list = []
        self.round_2 = False

        self.writer = Turtle()
        self.writer.up()
        self.writer.hideturtle()

        self.writer2 = Turtle()
        self.writer2.up()
        self.writer2.hideturtle()


        # first take turtles to desired positions
        self.writer.goto(120,320)
        self.writer2.goto(-220,320)


        self.writer.color("white")
        self.writer.write(arg=f'Score: {self.score}', font=("Arial", 20, "normal"))

        self.writer2.color("white")
        self.writer2.write(arg=f'Lives: {self.lives}', font=("Arial", 20, "normal"))





    def process_score(self):
        self.writer.clear()
        self.writer.write(arg=f'Score: {self.score}', font=("Arial", 20, "normal"))


    def life_reduction(self):

        self.lives -= 1
        self.writer2.clear()
        self.writer2.write(arg=f'Lives: {self.lives}', font=("Arial", 20, "normal"))



    def game_over(self):

        # clear score and life count displays at top of screen
        self.writer.clear()
        self.writer2.clear()

        # use Scoreboard object's writing turtle to display the final score in the centre of the screen
        self.writer.goto(0, -50)
        self.writer.write(arg=f'Your Score: {self.score}', align='center', font=("Arial", 30, "bold"))

        self.writer3 = Turtle()
        self.writer3.hideturtle()
        self.writer3.color("red")
        self.writer3.goto(0,0)
        self.writer3.write(arg='GAME OVER!', align='center', font=("Arial", 40, "bold"))


    #once a brick has been removed, the brick element that made contact with the ball is stored here as a string.
    #the score is calculated based on the brick elements that are stored here
    def score_calc(self):

        #eliminate duplicates from list of elements so that score doesn't exceed maximum of 448

        new_list = list(set(self.element_list))

        if self.round_2 == False:
            counter = 0

        else:
            counter = 448

        for i in new_list:
            if i[6] in ['0', '1']:
                counter += 1

            elif i[6] in ['2', '3']:
                counter += 3

            elif i[6] in ['4', '5']:
                counter += 5

            else:
                counter += 7


        self.score = counter














