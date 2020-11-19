import graphics as g

#make graphics window
win = g.GraphWin("Happy Face", 200, 200)

#left and right pupils
leftPupil = g.Point(50, 75)
rightPupil = g.Point(150, 75)

#left eye
leftEye = g.Circle(leftPupil, 25)
leftEye.setFill("white")
leftEye.setOutline("red")
leftEye.draw(win)
leftPupil.draw(win)

#right eye
rightEye = leftEye.clone()
rightEye.move(100, 0)
rightEye.draw(win)
rightPupil.draw(win)

#nose
nose = g.Rectangle(g.Point(75, 125), g.Point(125, 150))
nose.draw(win)

#mouth
centerMouthPoint = g.Point(100, 175)
leftMouthLine = g.Line(g.Point(40, 155), centerMouthPoint)
leftMouthLine.draw(win)
rightMouthLine = g.Line(centerMouthPoint, g.Point(160, 155))
rightMouthLine.draw(win)

#.Text(center Point(x, y), string)
textBox = g.Text(g.Point(100, 187), "Hello Human")
textBox.draw(win)

#.Entry(center point, width)
entryBox = g.Entry(g.Point(100, 25), 10)
entryBox.draw(win)

win.getMouse()
messageText = entryBox.getText()
textBox.setText(messageText)



                        
