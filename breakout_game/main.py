#import statements
from turtle import Screen, Turtle, getcanvas
import turtle

from Brick import Brick
from BrickPlacer import BrickPlacer
from Paddle import Paddle
from Ball import Ball
from Barrier import Barrier
from Scoreboard import Scoreboard
import time
import random
import pprint


#initiate screen
screen = Screen()

screen.setup(width=508, height=700)


#screen formatting
screen.bgcolor("black")

#ensure screen listening is on
screen.listen()


#set screen tracer to 0 for quick build
screen.tracer(0)


#initiate Scoreboard object and pass in Brickplacer object
sb = Scoreboard()


#initiate BrickPlacer object and call build function to set up brick layout
b = BrickPlacer(sb)
b.build()



#initiate barrier
br = Barrier()


#initiate Paddle object
p = Paddle(br)



#initiate ball object
ball = Ball()


#put ball in starting position
ball.goto(0, -230)



#set random heading of ball before movement
ball.setheading(random.randint(70, 110))


###### mouse position detection functionality ########
def on_motion(event):

    x = event.x - turtle.window_width() / 2
    y = -event.y + turtle.window_height() / 2

    if half_paddle_mode == False:
        p.move_to(x)

    else:
        p.move_to_b(x)



getcanvas().bind("<Motion>", on_motion)




#half paddle variable
half_paddle_mode = False



# initialise counter for when ball hits top wall
top_hit_count = 0
paddle_hit_count = 0
max_speed = False



#ball movement function
def move_ball():

    global top_hit_count
    global paddle_hit_count
    global max_speed
    global half_paddle_mode





    # increase ball speed depending on hit count
    if paddle_hit_count >= 2:
        ball.speed = 6

    if paddle_hit_count >= 12:
        ball.speed = 7

    if max_speed == True:
        ball.speed = 8
        

    ball.forward(ball.speed)



    for (row, row_dict) in b.brick_data.items():
        for (brick_col, el_list) in row_dict.items():
            for element in el_list:


                #once in contact with a particular element
                if ball.distance(element) <= 10:

                    #store the element in the Scoreboard object's element list
                    sb.element_list.append(str(element))


                    # if the block was orange or red, set max_speed to True
                    if element.color_name in ["orange", "red"]:
                        max_speed = True

                    #This method will process the elements in the Scoreboard object's element list to update
                    #the score based on the element's row numbers
                    sb.score_calc()

                    # update scoreboard
                    sb.process_score()



                    if el_list.index(element) in [0, 5]:
                        if 90 > ball.heading() >= 0:
                            new_h = ball.heading() + 180

                        elif 360 >= ball.heading() > 270:
                            new_h = ball.heading() - 180

                        elif 180 > ball.heading() > 90:
                            new_h = ball.heading() + 180

                        else:
                            new_h = ball.heading() - 180

                        ball.setheading(new_h)



                    else:

                        new_h = 360 - (ball.heading())

                        if 225 <= new_h <= 315:
                            ball.setheading(new_h)

                        elif new_h > 315:
                            new_h = 315
                            ball.setheading(new_h)

                        elif 135 < new_h < 225:
                            new_h = 225
                            ball.setheading(new_h)

                        elif 135 >= new_h >= 45:
                            ball.setheading(new_h)

                        elif new_h < 45:
                            new_h = 45
                            ball.setheading(new_h)

                    # delete_block() function that removes brick elements from corresponding brick in dictionary based on
                    # the row & column attributes of the brick object being contacted, thus removing then from the screen
                    b.delete_block(element)

                    #recursion to avoid multiple direction switches
                    move_ball()





    #left wall collision
    if ball.xcor() <= -252:

        if 180 >= ball.heading() > 90:
            new_h = 180 - ball.heading()
            ball.setheading(new_h)


        elif 270 > ball.heading() > 180:
            new_h = 270 + (270 - ball.heading())
            ball.setheading(new_h)

    #right wall collision
    if ball.xcor() >= 241:

        if 270 <= ball.heading() <= 360:
            new_h = 540 - ball.heading()
            ball.setheading(new_h)

        elif 90 > ball.heading() > 0:
            new_h = 180 - ball.heading()
            ball.setheading(new_h)

    #top wall collision
    if ball.ycor() >= 347:
        top_hit_count += 1

        if top_hit_count == 1:
            half_paddle_mode = True
            p.half_paddle()


        if 90 > ball.heading() > 0:
            new_h = 360 - ball.heading()
            ball.setheading(new_h)

        elif 180 > ball.heading() > 90:
            new_h = 360 - ball.heading()
            ball.setheading(new_h)

        elif ball.heading() == 90:
            new_h = 360 - ball.heading()
            ball.setheading(new_h)





    #when ball reaches height lower than or equal to the paddle line, if in the same x range as paddle, deflect

    #check if ball on the paddle line
    if ball.ycor() <= -235:
        # print(ball.speed)

        for (pos, seg) in p.segments.items():
            if seg.distance(ball) <= 10:

                #when ball is moving to the right
                if 360 > ball.heading() > 270:
                    # if ball hits centre, simple rebound
                    if pos == "middle":
                        new_h = 360 - ball.heading()
                        ball.setheading(new_h)
                        paddle_hit_count += 1
                        move_ball()

                    #if ball hits left portion, bounce off in opposite direction
                    if pos in ["l1", "l2"]:
                        new_h = ball.heading() - 180
                        ball.setheading(new_h)
                        paddle_hit_count += 1
                        move_ball()

                    elif pos == "r1":
                        new_h = 360 - ball.heading()
                        ball.setheading(new_h - 7)
                        paddle_hit_count += 1
                        move_ball()

                    elif pos == "r2":
                        new_h = 360 - ball.heading()
                        ball.setheading(new_h - 14)
                        paddle_hit_count += 1
                        move_ball()



                #when ball is moving to the left
                elif 270 > ball.heading() > 180:
                    if pos == "middle":
                        new_h = 360 - ball.heading()
                        ball.setheading(new_h)
                        move_ball()

                    # if ball hits right portion, bounce off in opposite direction
                    elif pos in ["r1", "r2"]:
                        new_h = ball.heading() - 180
                        ball.setheading(new_h)
                        paddle_hit_count += 1
                        move_ball()

                    elif pos == "l1":
                        new_h = 360 - ball.heading()
                        ball.setheading(new_h + 7)
                        paddle_hit_count += 1
                        move_ball()

                    elif pos == "l2":
                        new_h = 360 - ball.heading()
                        ball.setheading(new_h + 14)
                        paddle_hit_count += 1
                        move_ball()


                #when ball is moving straight down

                elif ball.heading() == 270:
                    if pos in ["r1", "r2"]:
                        new_h = 45
                        ball.setheading(new_h)
                        paddle_hit_count += 1
                        move_ball()

                    if pos in ["l1", "l2"]:
                        new_h = 135
                        ball.setheading(new_h)
                        paddle_hit_count += 1
                        move_ball()

                    if pos == "middle":
                        new_h = 360 - ball.heading()
                        ball.setheading(new_h)
                        paddle_hit_count += 1
                        move_ball()


    #ball miss actions
    if ball.ycor() < -400:
        sb.life_reduction()
        # put ball in starting position
        rand_pos = random.randint(-230, 230)
        rand_heading = random.randint(45, 135)
        ball.setheading(rand_heading)
        #bal respawn placement just above y coordinste where paddle deflection is considered to eliminate interference
        ball.goto(rand_pos, -236)




    #enables bottom barrier deflection if game is over
    if b.game_fin:

        ball.goto(0, -336)

        br.bottom.color("red")

        if ball.ycor() <= -337:

            #when ball is moving to the right
            if 360 > ball.heading() > 270:
                new_h = 360 - ball.heading()
                ball.setheading(new_h)

            #when ball is moving to the left
            elif 270 > ball.heading() > 180:
                new_h = 360 - ball.heading()
                ball.setheading(new_h)



    ######### Brick counting code ##########

    # determines if all the blocks have been hit and if 1st time, set the BrickPlacer object's 'rebuild'
    # object to True: If all blocks are broken again and this parameter is already set as True, The game
    # will continue to run (ball rebouding off walls); for this to happen activate bottom barrier's
    # rebounding functionality. Leave lives and score displayed on the screen


    #initialise brick counter
    brick_count = 0

    for (row, row_dict) in b.brick_data.items():
        for (brick_col, list) in row_dict.items():
            # if the length of the element list is 0, that implies the absence of a brick, therefore if
            # it's full process that as the brick being absent and add to the brick count
            if len(list) > 0:
                brick_count += 1


    #if after all the bricks have been counted, the brick count is still 0 and also the bricks haven't been rebuilt
    #before, rebuild the bricks, otherwise, end the game by allowing ball to deflect on all walls infinitely

    if brick_count == 0:
        if b.rebuild == False:
            b.rebuild = True

            #relocate ball to original position
            ball.goto(0, -230)

            sb.round_2 = True

            #clear the Scoreboard object's element_list
            sb.element_list = []

            b.build()

        else:
            #triggers the appearance and activation of the bottom barrier so that ball can rebound
            b.game_fin = True






    global game_on

    #game loss actions
    if sb.lives == 0:

        #hide ball
        ball.hideturtle()

        game_on = False

        #call Scoreboard object's game_over function that prints 'Game over!' on screen and displays final score
        sb.game_over()




game_on = True



while game_on == True:

    move_ball()


    #update screen to reflect changes
    screen.update()


screen.exitonclick()
