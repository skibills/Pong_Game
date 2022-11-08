import turtle as t



def run_game():
    window = t.Screen()
    window.title("Pong Game")
    window.bgcolor("green")
    window.setup(width = 800, height = 600)
    window.tracer(0)

    Player_1 = window.textinput("Player 1", "Name of the player: ")
    Player_2 = window.textinput("Player 2", "Name of the player: ")

#Score
    player1score = 0
    player2score = 0



#Left paddle
    leftpaddle = t.Turtle()
    leftpaddle.speed(0)
    leftpaddle.shape("square")
    leftpaddle.color("red")
    leftpaddle.shapesize(stretch_wid = 4.5, stretch_len = 0.5)
    leftpaddle.penup()
    leftpaddle.goto(-350, 0)



#Right paddle
    rightpaddle = t.Turtle()
    rightpaddle.speed(0)
    rightpaddle.shape("square")
    rightpaddle.color("blue")
    rightpaddle.shapesize(stretch_wid = 4.5, stretch_len = 0.5)
    rightpaddle.penup()
    rightpaddle.goto(350, 0)



#Ball
    ball = t.Turtle()
    ball.speed(0)
    ball.shape("circle")
    ball.color("white")
    ball.penup()
    ball.goto(0, 0)
    ball_x_direction = 0.2
    ball_y_direction = 0.2



#Pen
    pen = t.Turtle()
    pen.speed(0)
    pen.color("yellow")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 260)
    pen.write(str(Player_1) + " : 0    " + str(Player_2) + " : 0    ", align = "center", font = ('Calibri', 24, 'bold'))




#Left paddle movement
    def leftpaddleup():
        y = leftpaddle.ycor()
        y = y + 75
        leftpaddle.sety(y)

    def leftpaddledown():
        y = leftpaddle.ycor()
        y = y - 75
        leftpaddle.sety(y)



#Right paddle movement
    def rightpaddleup():
        y = rightpaddle.ycor()
        y = y + 75
        rightpaddle.sety(y)

    def rightpaddledown():
        y = rightpaddle.ycor()
        y = y - 75
        rightpaddle.sety(y)
    


#Keybinds
    window.listen()
    window.onkeypress(leftpaddleup, 'w')
    window.onkeypress(leftpaddledown, 's')
    window.onkeypress(rightpaddleup, 'Up')
    window.onkeypress(rightpaddledown, 'Down')




    while True:
        window.update()
    
    
#Ball movement
        ball.setx(ball.xcor() + ball_x_direction)
        ball.sety(ball.ycor() + ball_y_direction)



#Ball/Paddle collisions
        if(ball.xcor() > 340) and (ball.xcor() < 350) and (ball.ycor() < rightpaddle.ycor() + 40 and ball.ycor() > rightpaddle.ycor() - 40):
            ball.setx(340)
            ball_x_direction = ball_x_direction * -1

        if(ball.xcor() < -340) and (ball.xcor() > -350) and (ball.ycor() < leftpaddle.ycor() + 40 and ball.ycor() > leftpaddle.ycor() - 40):
            ball.setx(-340)
            ball_x_direction = ball_x_direction * -1



#Pong table border
        if ball.ycor() >= 260:
            ball.sety(260)
            ball_y_direction *= -1

        if ball.ycor() <= -260:
            ball.sety(-260)
            ball_y_direction *= -1



#Ball Out/Player Scores
        if ball.xcor() > 390:
            ball.goto(0, 0)
            ball_x_direction *= -1
            player1score = player1score + 1
            pen.clear()
            pen.write(str(Player_1) + " : {}    ".format(player1score) + str(Player_2) + " : {}    ".format(player2score),
                      align="center", font=('Calibri', 24, 'bold'))

        if ball.xcor() < -390:
            ball.goto(0, 0)
            ball_x_direction *= -1
            player2score = player2score + 1
            pen.clear()
            pen.write(str(Player_1) + " : {}    ".format(player1score) + str(Player_2) + " : {}    ".format(player2score),
                      align="center", font=('Calibri', 24, 'bold'))


#Wins
        if player1score >= 1: ##
            ball_y_direction = 0
            ball_x_direction = 0
            restart = window.textinput("Game Over.", "Do you want to play again ? (Y/N)")
            if restart == "y":
                window.resetscreen()
                run_game()
            else:
                break
        
        if player2score >= 1: ##
            ball_y_direction = 0
            ball_x_direction = 0
            restart = window.textinput("Game Over.", "Do you want to play again ? (Y/N)")
            if restart == "y":
                window.resetscreen()
                run_game()
            else:
                break        
            
            

run_game()        
    

    



