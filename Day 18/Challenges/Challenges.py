from turtle import Screen
import turtle as t

import random
#challenge 3
tim = t.Turtle()
# tim.shape('turtle')
# tim.color('deep pink')
# my_colors =  ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# my_shapes = [3,4,5,6,7,8,9,10]

# for shapes in my_shapes:
#     for _ in range(shapes):
#         tim.color(my_colors[shapes-3])
#         tim.forward(100)
#         tim.left(360/shapes)

# challenge 4
t.colormode(255)
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)
# direction = [0,90,180,270]
# tim.pensize(10)
tim.speed(20)
# for _ in range(200):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(direction))
def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(100) 
        tim.setheading(tim.heading()+size_of_gap)
draw_spirograph(20 )
screen = Screen()
screen.exitonclick()