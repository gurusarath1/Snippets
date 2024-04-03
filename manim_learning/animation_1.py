from manim import *


class test(Scene):

    def construct(self):

        name = Tex("Testing Text").to_edge(DL, buff=0.5)
        sq = Square(side_length=0.5, fill_color=RED, fill_opacity=1).to_corner(UL)
        tri = Triangle(fill_color=BLUE, fill_opacity=1).scale(0.5)

        self.play(Create(VGroup(name, sq)), run_time=2)
        self.play(DrawBorderThenFill(tri))
        self.wait() # 1 sec wait
        self.play(name.animate.to_corner(UL), tri.animate.scale(2))
        self.play(tri.animate.rotate(90))