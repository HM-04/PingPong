import turtle

display_window = turtle.Screen()
display_window.title("Ping Pong")
display_window.bgcolor("black")
display_window.setup(width=900, height=500)
display_window.tracer(0)  

paddle_1 = turtle.Turtle()
paddle_1.speed(0) #speed of animation
paddle_1.shape("square")
paddle_1.color("white")
paddle_1.shapesize(stretch_wid=5, stretch_len=1) #default is 20px for h + w, w is now 5 times larger, h remains same (times by 1)
paddle_1.penup()
paddle_1.goto(-400, 0) #start at -350 for x and 0 for y, 0,0 is in middle of screen display

paddle_2 = turtle.Turtle()
paddle_2.speed(0) 
paddle_2.shape("square")
paddle_2.color("white")
paddle_2.shapesize(stretch_wid=5, stretch_len=1)
paddle_2.penup()
paddle_2.goto(400, 0)

ball = turtle.Turtle()
ball.speed(0) 
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.12 #moves by 0.12px right
ball.dy = 0.12  #moves by 0.12px up


#Scoring Title
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,210)
pen.write("Player A: 0   Player B: 0", align="center", font=("Courier", 18, "normal"))

#Score
score_a = 0
score_b = 0


#Moving Paddles
def paddle_1_up():
	y = paddle_1.ycor()     #gives y coordinate
	y += 20
	paddle_1.sety(y)

def paddle_1_down():
	y = paddle_1.ycor()    
	y -= 20
	paddle_1.sety(y)

def paddle_2_up():
	y = paddle_2.ycor()    
	y += 20
	paddle_2.sety(y)

def paddle_2_down():
	y = paddle_2.ycor()    
	y -= 20
	paddle_2.sety(y)


display_window.listen()     #listens for keyboard input
display_window.onkeypress(paddle_1_up, "w")
display_window.onkeypress(paddle_1_down, "s")

display_window.onkeypress(paddle_2_up, "Up")
display_window.onkeypress(paddle_2_down, "Down")

#Main game loop
while True:
	display_window.update()


	#To move the ball
	ball.setx(ball.xcor() + ball.dx)
	ball.sety(ball.ycor() + ball.dy)

	

	#Borders
	#height = 500px, 250px from middle,  ball is 20 x 100px, width = 900px
	if ball.ycor() > 240:
		ball.sety(240)
		ball.dy *= -1

	if ball.ycor() < -240:
		ball.sety(-240)
		ball.dy *= -1

	if ball.xcor() > 440:
		ball.goto(0,0)
		ball.dx *= -1
		score_a += 1
		pen.clear()
		pen.write("Player A: {}   Player B: {}".format(score_a, score_b), align="center", font=("Courier", 18, "normal"))

	if ball.xcor() < -440:
		ball.goto(0,0)
		ball.dx *= -1
		score_b += 1
		pen.clear()
		pen.write("Player A: {}   Player B: {}".format(score_a, score_b), align="center", font=("Courier", 18, "normal"))


	#Collision, paddle is 100px wide and 20px height
	if ball.xcor() > 380 and (ball.ycor() < paddle_2.ycor() + 40 and ball.ycor() > paddle_2.ycor() - 40):
		ball.dx *= -1
		ball.dy *= -1

	if ball.xcor() < -380 and (ball.ycor() < paddle_1.ycor() + 40 and ball.ycor() > paddle_1.ycor() - 40):
		ball.dx *= -1