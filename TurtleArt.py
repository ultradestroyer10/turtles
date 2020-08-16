import turtle

t = turtle.Turtle()
turtle.bgcolor("black")
t.speed(0)

colours = ["red", "blue", "green", "orange", "yellow"]

def drawingOfShape(m):
    for x in range(m):
        t.forward(100)
        t.left(360/m)
        
#Enter how many sides your basic shape should have
numberOfSides = int(input("Enter the number of sides your shape should have: "))

y = 0
while y < 200:
    for i in colours:
        t.color(i)
        drawingOfShape(numberOfSides)
        y = y + 1
        #t.forward(15)
        t.left(5)


input("Press on any key to close ")