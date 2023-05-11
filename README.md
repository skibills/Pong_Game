# Pong_Game

The code is for a simple Pong game using the Python turtle graphics library. Pong is a two-dimensional sports game that simulates table tennis, and the players use paddles to hit a ball back and forth over a net.

The code begins with importing the turtle graphics library, which allows for the creation of graphic components such as paddles, ball, and text.

The run_game() function is the main function of the game that initiates the game window with the Screen() method. It sets the title of the game window, background color, window size, and turns off screen updates with the tracer(0) method.

It then prompts the user to input the names of the two players through the textinput() method.

The code then creates the visual components of the game. It starts with creating the left and right paddles using the Turtle() method, setting their color, size, and position with the shapesize(), color(), penup(), and goto() methods.

Next, the ball is created with a similar process, along with its movement direction using the ball_x_direction and ball_y_direction variables.

The code then creates a pen object that will display the player scores on the screen using the write() method.

Two functions, leftpaddleup() and leftpaddledown(), are created to move the left paddle up and down using the sety() method, respectively. Similarly, two functions, rightpaddleup() and rightpaddledown(), are created to move the right paddle up and down using the sety() method.

Next, the keybinds for the game are set using the listen() method and the onkeypress() method. The up and down arrow keys control the movement of the right paddle, while the 'w' and 's' keys control the movement of the left paddle.

The main game loop is set up using the while True: loop. Inside this loop, the window is constantly updated with the update() method.

The ball's movement is then updated using the setx() and sety() methods. Next, the code checks for collisions between the ball and the paddles using the if statement. If the ball collides with a paddle, it bounces off in the opposite direction.

The code then checks for collisions with the top and bottom borders of the game screen. If the ball hits the top or bottom border, it bounces off in the opposite direction.

Finally, the code checks if the ball goes out of bounds. If the ball goes out of bounds, the player score is updated and displayed on the screen using the write() method. If a player's score reaches 5 points, the game is over, and the code prompts the user to play again if desired.
