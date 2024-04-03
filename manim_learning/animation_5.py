from manim import *
import math


class test(Scene):

    def construct(self):
        plane = NumberPlane(x_range=[-10, 10, 1], x_length=10, y_range=[-10, 10, 1], y_length=10).to_edge(DOWN).add_coordinates()
        labels = plane.get_axis_labels(x_label="x", y_label="f(x)")
        sin_wave = plane.plot(lambda x: math.sin(x), x_range=[-10, 10], color=RED)
        area = plane.get_riemann_rectangles(graph=sin_wave, x_range=[-5,5], stroke_width=0.1, stroke_color=RED)

        self.play(FadeIn(VGroup(plane, labels)))
        self.play(Create(sin_wave))
        self.play(Create(area))
