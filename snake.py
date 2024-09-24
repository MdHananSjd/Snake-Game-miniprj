#imports
import turtle
import time
import random

delay = 0.1

#scores
score = 0
high_score = 0

#setting up the screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor('yellow')
wn.setup(width = 600, height = 600, 
         startx = None, starty = None)
wn.tracer(0)

#snake head
head = turtle.Turtle() #our turtle instance is named head
head.speed(5) #10
head.shape('square')
head.color('black')
head.penup()
head.goto(0,0)
head.direction = 'stop'


#snake food
food = turtle.Turtle()
food.speed(0)
food.shape('square')
food.color('red')
food.penup()
food.goto(0, 100)

segments = []

#scoreboards
sc = turtle.Turtle()
sc.shape('square')
sc.color('blue')
sc.penup()
sc.hideturtle()
sc.goto(0, 260)
sc.write('Score: 0 High Score: 0', align ='center',
          font = ('ds-digital', 24, 'normal'))

#functions
def go_up():
    if head.direction != 'down':
        head.direction = 'up'
def go_down():
    if head.direction != 'up':
        head.direction = 'down'
def go_right():
    if head.direction != 'left':
        head.direction = 'right'
def go_left():
    if head.direction != 'right':
        head.direction = 'left'

def move():
    if head.direction == 'up':
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == 'down':
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == 'right':
        x = head.xcor()
        head.setx(x + 20)
    if head.direction == 'left':
        x = head.xcor()
        head.setx(x - 20)

#keybinds setting
wn.listen()
wn.onkeypress(go_up, 'w')
wn.onkeypress(go_left, 'a')
wn.onkeypress(go_down, 's')
wn.onkeypress(go_right, 'd')

#Main loop

while True:
    wn.update()

    #check collision with border area

    if head.xcor() > 290 or head.xcor() < -290 or head.ycor()>290 or head.ycor() < -290:
        time.sleep(2)
        head.goto(0,0)
        head.direction = 'stop'        

        #hiding the segments of the body
        for i in segments():
            i.goto(1000, 1000) #putting it out of range
        #clearing the segments
        segments.clear()

        #reset score
        score = 0

        #reset delay
        delay = 0.1

        sc.clear()
        sc.write(f'score: {score} High Score: {high_score}', 
                 align = 'center', 
                 font = ('ds-digital', 24, 'normal'))
    

    #check collision with food
    if head.distance(food) < 20 :
        #move the food to a random location
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        #add a new segment to the head
        new_seg = turtle.Turtle()
        new_seg.speed(5) 
        new_seg.shape('square')
        new_seg.color('blue')
        new_seg.penup()
        segments.append(new_seg)

        #shorten the delay
        delay -= 0.001
        #increase the score
        score += 10

        if score > high_score:
            high_score = score
        sc.clear()
        sc.write(f'score: {score} High Score: {high_score}', 
                 align = 'center', 
                 font = ('ds-digital', 24, 'normal'))

    #moving the segments in reverse order

    for i in range(len(segments) -1, 0, -1):
            x = segments[i-1].xcor()
            y = segments[i-1].ycor()
            segments[i].goto(x,y)
    # move segment 0 to head
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()

    #checking for collision with body
    for segment in segments:
        if segment.distance(head) < 20 :
            time.sleep(1)
            head.goto(0,0)
            head.direction = 'stop' 

            #hide segments
            for segment in segments:
                segment.goto(1000, 1000) #sending that shi away
            segments.clear()
            score = 0
            selay = 0.1

            #update the score
            sc.clear()
            sc.write(f'score: {score} High Score: {high_score}', 
                 align = 'center', 
                 font = ('ds-digital', 24, 'normal'))
    time.sleep(delay)

wn.mainloop()