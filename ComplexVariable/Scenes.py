from manim import *
import random


class ComplexFunction(Scene):

    def construct(self):

        def f(z):
            return complex(z.real**2 - z.imag**2, 2*z.real*z.imag)

        # Initial Opening
        functionalFormText = Tex("$w = f(z)$", color=BLUE)
        transformation = Tex(r"$f$ acts like a transformation that converts\\ a complex number $z$ to another complex number $w$").next_to(
            functionalFormText, DOWN)
        self.add(functionalFormText, transformation)
        self.wait(4)
        self.remove(functionalFormText, transformation)

        # Z Plane configuration
        zPlane = ComplexPlane(
            x_range=[-5, 5, 1], y_range=[-5, 5, 1]).move_to([-3.55, 0, 0])

        aspectRatio = zPlane.width/zPlane.height
        zPlane.width = (config.frame_width-0.5)/2

        # W Plane configuration
        wPlane = ComplexPlane(x_range=[-50, 50, 5], y_range=[-50, 50, 5], **{
                              "background_line_style": {"stroke_color": GREEN}}).move_to([3.55, 0, 0])

        aspectRatio = wPlane.width/wPlane.height
        wPlane.width = (config.frame_width-0.5)/2

        # Add both planes on the screen
        self.add(zPlane, wPlane)

        zPlaneText = Tex('Z Plane').next_to(zPlane, DOWN).scale(0.8)
        wPlaneText = Tex('W Plane').next_to(wPlane, DOWN).scale(0.8)
        self.add(zPlaneText, wPlaneText)

        # Point on the z plane
        dot1 = Dot(point=zPlane.n2p(complex(1, 2)), color=GREEN)
        self.add(dot1)
        zText = Tex('$z$').next_to(dot1, UP)
        zText.add_updater(
            lambda mobject: mobject.next_to(dot1, UP))

        dot2 = Dot(point=wPlane.n2p(f(complex(1, 2))), color=BLUE)
        self.add(dot2)
        dot2.add_updater(
            lambda mobject: mobject.move_to(
                wPlane.n2p(f(zPlane.p2n(dot1.get_center()))))
        )
        wText = Tex('$w$').next_to(dot2, UP)
        wText.add_updater(
            lambda mobject: mobject.next_to(dot2, UP))

        arrow = always_redraw(lambda: Arrow(
            dot1.get_center(), dot2.get_center(), buff=0, color=RED))
        self.add(arrow)

        fz = Tex('$f$').next_to(arrow, UP, buff=0)
        fz.add_updater(
            lambda mobject: mobject.next_to(arrow, UP, buff=0))
        self.add(zText, wText, fz)

        for i in range(10):
            x = random.randint(-5, 4)
            y = random.randint(-5, 4)
            destination = zPlane.n2p(complex(x, y))
            self.play(dot1.animate.move_to(destination))
        self.wait(1)
