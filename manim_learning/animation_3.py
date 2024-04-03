from manim import *

class test(Scene):

    def construct(self):

        math_text = MathTex("\\frac{1}{2}")
        box = always_redraw(lambda: SurroundingRectangle(math_text, color=BLUE, fill_color=RED, fill_opacity=0.5, buff=0.5))
        title_text = Tex("Title Goes here").next_to(box, DOWN, buff=0.25)

        self.play(Create(VGroup(math_text, box)), run_time=3)
        self.play(Write(title_text), run_time=3)
        self.play(math_text.animate.shift(UP * 3), run_time=3)

