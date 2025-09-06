#
#
#IDEAS PANEL:
#
#       --> General steps: choose no of symmetries (4 to 12), central object, circle, design level 1, and repeat till desired complexity
#       --> Try implementing pygame into this to add UI add different buttons and other thing that give it a feel like its an app 
#
#
#
#TODO (LONG TERM):
#
#       --> Layers: at least like 5 layers and each layer should have like 5 to 10 different patterns not counting different colours that could be added.
#       
#
#TODO (SHORT TERM):
#
#       --> Generation:
#               small stuff: circles, petals (covex, concave), half-ellipses, spiral, 
#               big stuff: om symbol, lotus, spiral mehendi design, snowflakes
#
#       --> Get the collab stuff going, as in Gibhub, SSD change karoge so that will be an issue, so do that ASAP
#
#
#TODO (RIGHT NOW!):
#
#       Fix:
#               --> issue with draw circle: it's not drawing at the center (maybe), try using bezier curve to approximate circle
#                                           values: A(10,0) , B(10, 5.5527), C(5.5527, 10), D(0, 10)   try implementing it
#
#               --> just put support for angle in draw curve, it's useless rn but just do it, whatever
#               --> there are also issues with draw petal idk what is happening but in extreme values it overlaps and stuff
#       
#       Implement:
#               --> a function that creates and fills colour in a sensible way, right now its a bit of a mess, it fills towards the center and away from it
#                   if asked and in a way that creates a nice box, have to keep track of extremas there for different directions, so do that
#
#               --> changing a_y to extreme values in draw petal had interesting results, experiment with that, might get mehendi design from this alone
#
#
#

import turtle
import math
import random

screen = turtle.Screen()
screen.setup(width=900, height=900)
screen.title("Kolam Designs")
pen = turtle.Turtle()

#Useful fuctions:
def draw_bezier_curve(x_a, x_b, x_c, x_d, y_a, y_b, y_c, y_d, offset_x=0, offset_y=0, angle = 0, colour = "blue", step = 0.01, t_min = 0.001, t_max = 1, colour_fill= False):
    pen.speed(0)
    pen_starting_position = (0, 0)
    if colour_fill:
        pen.fillcolor(colour)
        pen.begin_fill()
    pen.color(colour)
    pen.penup()

    t = t_min
    while t <= t_max:
        x = offset_x + t**3 * (x_a - 3*x_b + 3*x_c - x_d) + 3*t**2 * (x_b - 2*x_c + x_d) + 3*t * (x_c - x_d) + x_d
        y = offset_y + t**3 * (y_a - 3*y_b + 3*y_c - y_d) + 3*t**2 * (y_b - 2*y_c + y_d) + 3*t * (y_c - y_d) + y_d


        if t == t_min:
            pen_starting_position = turn_object(x, y, angle)
            

        pen.goto(turn_object(x, y, angle))
        pen.pendown()
        t += step

    if colour_fill:
        pen.goto(turn_object(offset_x, offset_y, angle))
        pen.goto(pen_starting_position)
        pen.end_fill()
def turn_object(x, y, degrees = 0):
     radius = math.sqrt(x**2 + y**2)
     if x == 0:
        angle = math.pi
     else:
        angle = math.atan(y/x)
     new_angle = degrees*math.pi/180 + angle
     return (radius * math.cos(new_angle), radius * math.sin(new_angle))


#Useless fuctions (but still keep them for now):
def draw_parametric_curve(func_x, func_y, offset_x=0, offset_y=0, angle = 0, colour = "blue", step = 0.01, t_min = 0, t_max = 1):
    pen.speed(0)
    pen.fillcolor(colour)
    pen_starting_position = (0, 0)
    pen.begin_fill()
    pen.color(colour)
    pen.penup()

    t = t_min
    while t <= t_max:
        x = offset_x + func_x(t)
        y = offset_y + func_y(t)

        if t == t_min:
            pen_starting_position = turn_object(x, y, angle)
            

        pen.goto(turn_object(x, y, angle))
        pen.pendown()
        t += step

    pen.goto(turn_object(offset_x, offset_y, angle))
    pen.goto(pen_starting_position)
    pen.end_fill()
def draw_curve(func, start, end, angle, color):
    turtle.speed(0)
    turtle.penup()
    turtle.color(color)
    
    
    for x in range(start, end): 
        y = func(x / 20) 
        if start <= y * 20 <= end:
            turtle.goto(x, y * 20)
            turtle.pendown()
        else:
            turtle.penup()


#Different shape designes:
def draw_circle(offset_x=0, offset_y=0, radius=10, colour="blue"):
    pen.fillcolor(colour)
    pen.begin_fill()
    pen.pencolor(colour)
    pen.goto(offset_x, offset_y-radius/2)
    pen.circle(radius)
    pen.end_fill()
def draw_petal(offset_x=0, offset_y=0, thickness=100, tallness=200, roundness=0.5, sharpness=1, angle=0, colour="blue", draw_top=True, draw_bottom=True):
    b_x = roundness*tallness + (1-roundness)*tallness/4
    b_y = (1-sharpness)*thickness
    if draw_top:
        draw_bezier_curve(tallness, b_x, tallness/4, 0, -2, b_y, thickness, thickness/2, offset_x, offset_y, angle, colour)
    if draw_bottom:
        draw_bezier_curve(tallness, b_x, tallness/4, 0, 2, -1*b_y, -1*thickness, -1*thickness/2, offset_x, offset_y, angle, colour)


#Different layers and patterns (hopefully someday):






#MAIN PROGRAM
print("start")               #for debug



no_of_symmetry = 4
animations = False
if not animations:
    turtle.tracer(0, 0)




# Create stuff here


size = 200
draw_circle(radius=1)
for angle in range(0, 360, 360//no_of_symmetry):

    for repeat in range(0,50, 10):
        A = (size-2*repeat, repeat)
        B = (size-2*repeat, size)
        C = (size-2*repeat, size)
        D = (-repeat, size)
        draw_bezier_curve(A[0], B[0], C[0], D[0], A[1], B[1], C[1], D[1], colour="black", offset_x=repeat, offset_y=-size-repeat, angle=angle, t_max=1.01)
        draw_bezier_curve(A[0], B[0], C[0], D[0], A[1], B[1], C[1], D[1], colour="black", offset_x=-size+repeat, offset_y=size-size-repeat, angle=angle, t_max=1.01)






""" 


turn_angle_step = 360//no_of_symmetry
for turn_angle in range(0, 360-no_of_symmetry, turn_angle_step):
    draw_petal(1, 0, 100, 1.5*250, 0.4, 0.8, angle=turn_angle, colour="purple")
    draw_petal(1, 0, 100, 250, 0.4, 0.8, angle=turn_angle, colour="pink")


draw_petal(1, 0, 100, 1.5*250, 0.4, 0.8, 0, colour="purple", draw_top=False)
draw_petal(1, 0, 100, 250, 0.4, 0.8, 0, colour="pink", draw_top=False)


for turn_angle in range(0, 360-no_of_symmetry, turn_angle_step):
    draw_petal(1, 0, 100*0.7, 1.5*250*0.7, 0.4, 0.8, angle=turn_angle+turn_angle_step/2, colour="red")
    draw_petal(1, 0, 100*0.7, 250*0.7, 0.4, 0.8, angle=turn_angle+turn_angle_step/2, colour="blue")
    
draw_petal(1, 0, 100*0.7, 1.5*250*0.7, 0.4, 0.8, turn_angle_step/2, colour="red", draw_top=False)
draw_petal(1, 0, 100*0.7, 250*0.7, 0.4, 0.8, turn_angle_step/2, colour="blue", draw_top=False)

draw_circle(0, -25, radius=50, colour="orange")
 """





pen.hideturtle()
if not animations:
    turtle.update()
print("stop")                 #for debug
screen.mainloop()
    




