from manim import *
import random
class StereographicProjection(ThreeDScene):
        def construct(self):
                resolution_fa = 1
                self.set_camera_orientation(phi=75 * DEGREES, theta=-160 * DEGREES)
                axes = ThreeDAxes(x_range=(-5, 5, 1), y_range=(-5, 5, 1), z_range=(-1, 1, 0.5))
                # def param_surface(u, v):
                #       x = u
                #       y = v

                #       return z
                def pointOnSphere(x, y):
                        modz = np.sqrt(x**2+y**2)
                        return [4*x/(modz**2+4), 4*y/(modz**2+4), 2*modz**2/(modz**2+4)]
                surface_plane = Surface(
                        lambda u, v: axes.c2p(u, v, 0),
                        resolution=(resolution_fa, resolution_fa),
                        v_range=[-5, 5],
                        u_range=[-5, 5],
                        ).set_color(GREEN)
                surface_plane.set_style(fill_opacity=1)
                sphere = Sphere(center = [0, 0, 1], resolution = (50, 50), fill_opacity = 0.1).set_color(GRAY)
                # surface_plane.set_fill_by_value(axes=axes, colors=[(RED, -0.5), (YELLOW, 0), (GREEN, 0.5)], axis=2)
                line = Line(start = [-3, -3, 0], end = [0, 0, 2], **{"stroke_width": 1})
                point = [-3, -3, 0]
                dot1 = Sphere(center = point, radius = 0.05, resolution = (5, 5))
                dot2 = Sphere(center = pointOnSphere(-3, -3), radius = 0.05, resolution = (5, 5)).set_color(RED)
                # print(dot1Temp.get_center(random.randit))
                # dot1.add_updater(
                #       lambda mobject: mobject.move_to(dot1Temp.get_center()))
                dot2.add_updater(
                        lambda mobject: mobject.move_to(pointOnSphere(dot1.get_center()[0], dot1.get_center()[1]))
                        )
                line = always_redraw(lambda: Line(start = [0, 0, 2], end = dot1.get_center(), **{"stroke_width": 1}))
                self.add(axes, surface_plane, sphere, line, dot1, dot2)
                self.wait(2)
                for i in range(10):
                        self.play(dot1.animate.move_to([random.randint(-5, 5), random.randint(-5, 5), 0]))
                self.wait()
                self.play(dot1.animate.move_to([10,10,0]), run_time = 2)
                self.play(dot1.animate.move_to([-10, 10, 0]), run_time = 2)
                self.play(dot1.animate.move_to([-10, -10, 0]), run_time = 2)
                self.play(dot1.animate.move_to([10, -10, 0]), run_time = 2)
                self.play(dot1.animate.move_to([100, -100, 0]), run_time = 3)
                self.wait()