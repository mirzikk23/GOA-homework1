from turtle import *

#we want to paint three house with sun

#step 1: draw a square

penup()
goto(200,0)
pendown()

color("green")
begin_fill
speed(100)
width(6)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
end_fill()

penup()
goto(200,200)
pendown()

color("green")
begin_fill()
right(220)
forward(155)
right(100)
forward(152)
color("yellow")
end_fill()

penup()
goto(180,0)
pendown()

color("green")
begin_fill()
end_fill()
left(140)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)

penup()
goto(-20,200)
pendown()

color("green")
begin_fill()
left(50)
forward(155)
right(100)
forward(155)
color("yellow")
end_fill()


penup()
goto(-40,0)
pendown()

color("green")
begin_fill()
left(140)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)


penup()
goto(-240,200)
pendown()

color("green")
begin_fill()
left(50)
forward(155)
right(100)
forward(155)
color("yellow")
end_fill()

penup()
goto(-55,170)
pendown()

right(40)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)

penup()
goto(-170,170)
pendown()

right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)

penup()
goto(270,0)
pendown()

color("brown")
begin_fill()
left(90)
forward(105)
right(90)
forward(50)
right(90)
forward(105)
color("brown")
end_fill()

penup()
goto(100,0)
pendown()

color("brown")
begin_fill()
back(105)
right(90)
forward(50)
left(90)
forward(105)
color("brown")
end_fill()

penup()
goto(-40,0)
pendown()

color("brown")
begin_fill()
left(90)
forward(-70)
left(90)
forward(105)
left(90)
forward(50)
left(90)
forward(105)
color("brown")
end_fill()

penup()
goto(45,170)
pendown()

color("blue")
begin_fill
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)


penup()
goto(165,170)
pendown()

right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)

penup()
goto(215,170)
pendown()

color("orange")
begin_fill
right(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)

penup()
goto(375,170)
pendown()

left(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)

color("yellow")
begin_fill()
penup()
goto(-375,310)
pendown()

forward(60)

penup()
goto(-375,310)
pendown()

right(90)
forward(60)

penup()
goto(-375,310)
pendown()

right(90)
forward(60)

penup()
goto(-375,310)
pendown()

right(90)
forward(60)

penup()
goto(-375,310)
pendown()

right(45)
forward(50)

penup()
goto(-375,310)
pendown()

right(90)
forward(50)

penup()
goto(-375,310)
pendown()

right(90)
forward(50)

penup()
goto(-375,310)
pendown()

right(90)
forward(50)


exitonclick()