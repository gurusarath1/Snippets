from manim import *

class test(Scene):

    def construct(self):

        ax = Axes()

        rect = Rectangle(width=5, height=2)
        circ = Circle(radius=1).to_edge(RIGHT)
        arrow = always_redraw(lambda: Line(start = rect.get_bottom(), end=circ.get_center(), buff=0.1).add_tip())

        self.play(Create(ax))
        self.play(Create(VGroup(rect, circ, arrow)), run_time=2)
        self.play(circ.animate.to_edge(LEFT))
        self.play(circ.animate.to_edge(UR), rect.animate.scale(2))
        self.wait()