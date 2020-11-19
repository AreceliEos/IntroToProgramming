import graphics as g
#lepracaun
#make graphics window
win = g.GraphWin("Mythical Creature", 400, 400)

#body
body = g.Rectangle(g.Point(175, 125), g.Point(215, 205))
body.setFill("dark green")
body.setOutline("green")
body.draw(win)

#right leg
rightLeg = g.Rectangle(g.Point(215, 225), g.Point(200, 205))
rightLeg.setFill("dark green")
rightLeg.setOutline("green")
rightLeg.draw(win)

#left leg
leftLeg = rightLeg.clone()
leftLeg.move(-25, 0)
leftLeg.draw(win)

#nose
nose = g.Point(195, 100)

#head
head = g.Circle(nose, 25)
head.setFill("tan")
head.setOutline("brown")
head.draw(win)

#beard
beard = g.Rectangle(g.Point(185, 110), g.Point(205, 135))
beard.setFill("orange")
beard.setOutline("red")
beard.draw(win)

#top hat
topHat = g.Rectangle(g.Point(215, 35), g.Point(175, 75))
topHat.setFill("dark green")
topHat.setOutline("green")
topHat.draw(win)
centerPoint = g.Point(195, 75)
leftHatLine = g.Line(g.Point(225, 75), centerPoint)
leftHatLine.draw(win)
rightHatLine = g.Line(centerPoint, g.Point(165, 75))
rightHatLine.draw(win)

#belt
centerPoint = g.Point(180, 175)
leftBeltLine = g.Line(g.Point(175, 175), centerPoint)
leftBeltLine.draw(win)
rightBeltLine = g.Line(centerPoint, g.Point(215, 175))
rightBeltLine.draw(win)

#text label
textBox = g.Text(g.Point(200, 255), "Kiss Me, I'm Lucky!")
textBox.setOutline("yellow")
textBox.draw(win)

win.getMouse()
head.setFill("pink")



