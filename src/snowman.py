import graphics as g

#draws window
win = g.GraphWin("Snow Penguin", 400 , 400)
#draws bottom circle
bottomPoint = g.Point(200, 320)
bottomCircle = g.Circle(bottomPoint, 80)
bottomCircle.draw(win)
#draws middle circle
middlePoint = g.Point(200, 180)
middleCircle = g.Circle(middlePoint, 60)
middleCircle.draw(win)
#draws top circle
topPoint = g.Point(200, 80)
topCircle = g.Circle(topPoint, 40)
topCircle.draw(win)

leftEye = g.Point(190, 60)
leftEye.draw(win)

rightEye = leftEye.clone()
rightEye.move(20,0)
rightEye.draw(win)

noseOne = g.Line(topPoint, g.Point(210, 90))
noseTwo = g.Line(g.Point(210, 90), g.Point(210,80))
noseThree = g.Line(g.Point(210,80), topPoint)
noseOne.draw(win)
noseTwo.draw(win)
noseThree.draw(win)
