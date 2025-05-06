from graphics import *

win = GraphWin("My Window", 400, 400)  # Create a window
circle = Circle(Point(200, 200), 50)   # Create a circle at (200,200) with radius 50
circle.setFill("blue")                 # Fill it with blue color
circle.draw(win)                       # Draw the circle in the window

win.getMouse()  # Pause until mouse click
win.close()     # Close the window
