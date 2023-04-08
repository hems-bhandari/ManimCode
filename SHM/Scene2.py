from manim import *

class RotateDisk(Scene):
    def construct(self):
        disk = Circle(radius=2, color=WHITE).set_fill(BLACK, opacity=1)
        ball = Circle(radius=0.2, color=YELLOW).move_to(disk.get_top())
        disk.add(ball)
        disk.rotate(TAU, about_point=ORIGIN, about_edge=ORIGIN)
        self.play(Rotating(disk, radians=TAU, about_point=ORIGIN, run_time=2))

class ShadowOnWall(Scene):
    def construct(self):
        disk = Circle(radius=2, color=WHITE).set_fill(BLACK, opacity=1)
        ball = Circle(radius=0.2, color=YELLOW).move_to(disk.get_top())
        disk.add(ball)
        light_source = Dot(ORIGIN, color=WHITE)
        wall = Line(start=FRAME_X_RADIUS*LEFT+2*DOWN, end=FRAME_X_RADIUS*RIGHT+2*DOWN, color=WHITE)
        self.play(
            FadeIn(disk),
            FadeIn(light_source),
            FadeIn(wall)
        )
        self.wait()
        self.play(
            Create(disk.copy().set_color(BLACK).set_opacity(0.2).scale(2).move_to(wall))
        )
        self.wait()
        self.play(
            Transform(disk.copy(), ball.copy().set_color(BLACK).set_opacity(0.2).scale(2).move_to(wall))
        )
        self.wait()

class SyncOscillatingPendulum(Scene):
    def construct(self):
        disk = Circle(radius=2, color=WHITE).set_fill(BLACK, opacity=1)
        ball = Circle(radius=0.2, color=YELLOW).move_to(disk.get_top())
        disk.add(ball)
        light_source = Dot(ORIGIN, color=WHITE)
        wall = Line(start=FRAME_X_RADIUS*LEFT+2*DOWN, end=FRAME_X_RADIUS*RIGHT+2*DOWN, color=WHITE)
        pendulum = Line(start=ball.get_center(), end=ball.get_center() + 2*DOWN, color=RED)
        self.play(
            FadeIn(disk),
            FadeIn(light_source),
            FadeIn(wall)
        )
        self.wait()
        self.play(
            Create(disk.copy().set_color(BLACK).set_opacity(0.2).scale(2).move_to(wall))
        )
        self.wait()
        self.play(
            Transform(disk.copy(), ball.copy().set_color(BLACK).set_opacity(0.2).scale(2).move_to(wall))
        )
        self.wait()
        self.play(
            FadeIn(pendulum),
            Rotate(disk, TAU/4, about_point=ORIGIN, run_time=1.5, rate_func=linear)
        )
        self.play(
            pendulum.animate.become(Line(start=ball.get_center(), end=ball.get_center() + 2*DOWN, color=GREEN)),
            Rotate(disk, TAU/4, about_point=ORIGIN, run_time=1.5, rate_func=linear)
        )

class SyncMovingSineWave(Scene):
    def construct(self):
        disk = Circle(radius=2, color=WHITE).set_fill(BLACK, opacity=1)
        ball = Circle(radius=0.2, color=YELLOW).move_to(disk.get_top())
        disk.add(ball)
        light_source = Dot(ORIGIN, color=WHITE)
        wall = Line(start=FRAME)
class Shadow(Scene):
    def construct(self):
        disk = Circle(radius=2, color=WHITE)
        ball = Dot(radius=0.2, color=YELLOW).move_to(disk.get_top())

        self.add(disk, ball)

        # Shadow
        shadow = ball.copy().set_fill(opacity=0.5).scale(0.6)
        shadow.add_updater(lambda m: m.move_to(ball.get_center() + np.array([0, -2, 0])))
        self.add(shadow)

        # Wall
        wall = Line(np.array([-FRAME_WIDTH/2 + 1, -FRAME_HEIGHT/2 + 1, 0]), 
                    np.array([-FRAME_WIDTH/2 + 1, FRAME_HEIGHT/2 - 1, 0]), 
                    color=WHITE)
        self.add(wall)

        # Oscillating pendulum
        pendulum = Pendulum()
        pendulum.move_to(np.array([FRAME_WIDTH/2 - 2, FRAME_HEIGHT/2 - 2, 0]))
        self.add(pendulum)

        # Sync oscillating shadow with pendulum
        self.play(
            shadow.animate.add_updater(lambda m: m.move_to(pendulum.get_end() + np.array([0, -2, 0])))
        )

        # Sine wave
        sine_wave = FunctionGraph(lambda x: np.sin(5*x), x_min=-5, x_max=5)
        sine_wave.move_to(np.array([FRAME_WIDTH/2 - 2, -FRAME_HEIGHT/2 + 2, 0]))
        self.add(sine_wave)

        # Sync oscillating shadow with sine wave
        self.play(
            shadow.animate.add_updater(lambda m: m.move_to(np.array([sine_wave.underlying_function(pendulum.get_theta()), 
                                                                     -FRAME_HEIGHT/2 + 1.5, 
                                                                     0])))
        )

        self.wait(2)
