# Import the turtle module
import turtle

# Create a turtle object
t = turtle.Turtle()

# Set the speed and the shape of the turtle
t.speed(5)
t.shape("turtle")

# Draw a square for the base of the house
for i in range(4):
 t.forward(200) # Move forward by 200 units
 t.left(90) # Turn left by 90 degrees

t.penup() # Lift the pen up
t.goto(50, 200) 
t.left(45) # Turn left by 45 degrees
t.forward(141) # Move forward by 141 units (the diagonal of the square)
t.right(90) # Turn right by 90 degrees
t.forward(141) # Move forward by 141 units (the other diagonal of the square)

# Draw a door for the house
t.penup() # Lift the pen up
t.goto(50, 200) # Go to the position (50, 0)
t.pendown() # Put the pen down
t.right(135) # Turn right by 135 degrees
t.forward(100) # Move forward by 100 units
t.left(90) # Turn left by 90 degrees
t.forward(50) # Move forward by 50 units
t.left(90) # Turn left by 90 degrees
t.forward(100) # Move forward by 100 units

# Hide the turtle
t.hideturtle()

# Keep the window open until the user closes it
turtle.done()
