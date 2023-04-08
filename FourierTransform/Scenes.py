from manim import *

class SquareFunction(Scene):
	def construct(self):
		axes = Axes(
            x_range = [-5, 5.1, 1],
            y_range = [-1.5, 1.5, 1],
            x_length = 2*TAU,
            axis_config = {"color": GREEN},
            # x_axis_config = {
            # "numbers_to_include":np.arange(-10, 10.1, 2),
            # # "numbers_with_elongated_ticks": np.arange(-10, 10.2, 2),
            # },
            tips = False,
            )

		def squareWave(x):
			if int(x)%2 == 0:
				return 1*x//abs(x)
			else:
				return -1*x//abs(x)
		# def Sin1(x):
		# 	return 2*(1-np.cos(1))*np.sin(x)
		# def Sin2(x):
		# 	return (2/2)*(1-np.cos(2))*np.sin(2*x)

		def Sinn(x, n):
			result = 0
			for i in range(1, n+1, 2):
				result += (2/(i*np.pi))*(2)*np.sin(i*x*np.pi)
			return result
		def SINN(x, i):
			return (2/(i*np.pi))*(2)*np.sin(i*x*np.pi)


		square_graph = axes.plot(squareWave, x_range = (-4.9, 4.9, 0.01), **{"discontinuities": [x for x in range(-5, 6)]})
		values = [0]
		values1 = [0]
		index = 1
		for i in range(1, 31, 2):
			values.append(axes.plot(lambda x: SINN(x, i), x_range = (-4.9, 4.9, 0.1)))
			values1.append(axes.plot(lambda x: Sinn(x, i), x_range = (-4.9, 4.9, 0.1), color = BLUE))
		#sin1_graph = axes.plot(Sin1, x_range = (-4.9, 4.9, 0.01))
		#sin2_graph = axes.plot(Sin2, x_range = (-4.9, 4.9, 0.01))
		#sinn_graph = axes.plot(Sinn, x_range = (-4.9, 4.9, 0.1))
		self.add(axes, square_graph,  values[1])
		self.play(ReplacementTransform(values[1], values1[1]))
		for i in range(2, 15):
			self.play(Create(values[i]))
			self.wait(1)
			self.play(ReplacementTransform(values[i], values1[i]), ReplacementTransform(values1[i-1], values1[i]))