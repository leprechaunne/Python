from graphics import *
def main():
    win = GraphWin("Snake", 500, 500)
    win.setBackground("black")
    c = Circle(Point(50,50), 10)
    c.draw(win)
    win.getMouse() # pause for click in window
    win.close()
main()
