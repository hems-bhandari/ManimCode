import math
import numpy
from manim import *
points = numpy.zeros(341, dtype = list)
def addPoints(x1, y1, x2, y2, n):
	if n>340:
		return 0
	points[n] = [x1, y1, x2, y2]
	(x11, y11) = (x1+(x2-x1)/3, y1+(y2-y1)/3)
	(x12, y12) = (x1 + (x2-x1)/2-math.sqrt(3)*(y2-y1)/6, y1 + (y2-y1)/2+math.sqrt(3)*(x2-x1)/6)
	(x13, y13) = (x1+2*(x2-x1)/3, y1+2*(y2-y1)/3)
	addPoints(x1, y1, x11, y11, 4*n+1)
	addPoints(x11, y11, x12, y12, 4*n+2)
	addPoints(x12, y12, x13, y13, 4*n+3)
	addPoints(x13, y13, x2, y2, 4*n+4)



addPoints(-6, -1, 6, -1, 0)

lines = []
color = ['#b711ff', '#ff6700', '#f81894', '#ffb919', '#0fc5e3']
class KochCurve(Scene):
	def construct(self):
		colorIndex = 0
		for i, point in enumerate(points):
			x1 = point[0]
			y1 = point[1]
			x2 = point[2]
			y2 = point[3]
			
			if i == 1:
				colorIndex+=1
			if i == 4+1:
				colorIndex+=1
			if i == 4+16+1:
				colorIndex += 1
			if i == 4+16+64+1:
				colorIndex += 1

			lines.append(Line(start = [x1, y1, 0], end = [x2, y2, 0], color = color[colorIndex], **{"stroke_width": 2}))
		for i in range(len(lines)):
			if i == 0:
				self.play(Create(lines[i]), run_time = 2)
			if i>=1 and i<=4:
				self.play(Create(lines[i], run_time = 1))
			if i>=5 and i<=4+16:
				self.play(Create(lines[i], run_time = 0.5))
			if i>=4+16+1 and i<=4+16+64:
				self.play(Create(lines[i], run_time = 0.1))
			if i>=4+16+64+1 and i<=4+16+64+256:
				self.play(Create(lines[i], run_time = 0.05))


			if i == 4:
				self.play(FadeOut(lines[0]))
			if i == 4 + 16:
				firstGroup = VGroup()
				for i in range(1, 5):
					firstGroup.add(lines[i])
				self.play(FadeOut(firstGroup))
			if i == 4 + 16 + 64:
				secondGroup = VGroup()
				for i in range(5, 4+16+1):
					secondGroup.add(lines[i])
				self.play(FadeOut(secondGroup))
			if i == 4+16+64+256:
				thirdGroup = VGroup()
				for i in range(4+16+1, 4+16+64+1):
					thirdGroup.add(lines[i])
				self.play(FadeOut(thirdGroup))

		self.wait(2)
