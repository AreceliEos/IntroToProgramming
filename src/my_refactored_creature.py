import graphics as g
def DrawCircularShape(point1, radius, color, colorOut, window):
    head = g.Circle(point1, radius)
    head.setFill(color)
    head.setOutline(colorOut)
    head.draw(window)

def DrawCauldron(point1, radius, color, colorOut, window):
    base = g.Circle(point1, radius)
    base.setFill(color)
    base.setOutline(colorOut)
    base.draw(window)
#cauldrons - circle base and rectangluar rim # x3

def DrawRectangularShape(point1, point2, color, colorOut, window):
    body = g.Rectangle(point1, point2)
    body.setFill(color)
    body.setOutline(colorOut)
    body.draw(window)
#will be used for all rectangular components
    #body, legs, beard, top hat

def DrawAccessoryLines(point1, point2, window):
    line = g.Line(point1, point2)
    line.draw(window)
#will be used for belt and top hat lines
    #removing centerpoints and manually entering


win = g.GraphWin("My Refactored Creature", 400, 400)

DrawCircularShape(g.Point(195, 100), 25, 'tan', 'brown', win)

DrawCauldron(g.Point(300, 200), 25, 'grey', 'black', win)
DrawCauldron(g.Point(105, 230), 25, 'grey', 'black', win) 
DrawCauldron(g.Point(275, 300), 25, 'grey', 'black', win)

DrawRectangularShape(g.Point(175, 125), g.Point(215, 205), 'dark green', 'green', win)
DrawRectangularShape(g.Point(215, 225), g.Point(200, 205), 'dark green', 'green', win)
DrawRectangularShape(g.Point(190, 225), g.Point(175, 205), 'dark green', 'green', win)
DrawRectangularShape(g.Point(215, 35), g.Point(175, 75), 'dark green', 'green', win)
DrawRectangularShape(g.Point(185, 110), g.Point(205, 135), 'orange', 'red', win)
DrawRectangularShape(g.Point(330, 185), g.Point(270, 175), 'gold', 'black', win)
DrawRectangularShape(g.Point(75, 205), g.Point(135, 215), 'gold', 'black', win)
DrawRectangularShape(g.Point(305, 285), g.Point(245, 275), 'gold', 'black', win)

DrawAccessoryLines(g.Point(225, 75), g.Point(195, 75), win)
DrawAccessoryLines(g.Point(195, 75), g.Point(165, 75), win)
DrawAccessoryLines(g.Point(175, 175), g.Point(180, 175), win)
DrawAccessoryLines(g.Point(180, 175), g.Point(215, 175), win)
 
#textbox
textBox = g.Text(g.Point(200, 255), "Kiss Me, I'm Lucky!")
textBox.setOutline("yellow")
textBox.draw(win)
win.getMouse()
textBox.setOutline("pink")
textBox.draw(win)



