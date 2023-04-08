from manim import *
from manim.animation.creation import Create

class SimplePendulum(Scene):
    def construct(self):
        # Parameters
        L = 2  # Length of pendulum
        A = 0.5  # Amplitude of oscillation
        T = 2  # Period of oscillation
        t_max = 5  # Maximum time to simulate

        # Pendulum and path
        pendulum = Circle(radius=0.1, color=RED).next_to(ORIGIN, UP, buff=0)
        path = VMobject(color=GREEN)

        # Graph
        graph = Axes(
            x_range=[0, t_max],
            y_range=[-A, A],
            x_axis_config={"include_tip": False},
            y_axis_config={"include_tip": False},
        )
        graph.set_width(0.8 * self.camera.frame_width)
        graph.to_edge(LEFT, buff=0.5)

        # Equation
        equation = MathTex(r"\theta(t) = \theta_0 \cos(\omega t)").to_corner(UP + RIGHT)

        # Initial conditions
        theta_0 = PI / 4
        omega = 2 * PI / T
        t = 0

        # Animations
        self.play(
            Write(pendulum),
            Write(graph),
            Write(equation),
            run_time=2,
        )
        while t <= t_max:
            theta = theta_0 * np.cos(omega * t)
            pendulum_new_pos = L * np.array([-np.sin(theta), -np.cos(theta), 0])
            pendulum_new = pendulum.copy().move_to(pendulum_new_pos)
            path_points = path.points
            path_points = np.vstack([path_points, pendulum_new_pos])
            path.set_points_smoothly(path_points)
            graph_dot = Dot([t, A * np.sin(omega * t), 0], color=BLUE)
            self.play(
                Transform(pendulum, pendulum_new),
                Create(graph_dot),
                Create(path),
                run_time=0.1,
            )
            t += 0.1

        # Final animations
        self.wait(2)
