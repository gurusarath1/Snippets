from manim import *

class drawing(Scene):

    def construct(self):

        c = Circle(radius=1, fill_color=RED, fill_opacity=0.5)

        self.play(DrawBorderThenFill(c), run_time=10)
        self.wait()