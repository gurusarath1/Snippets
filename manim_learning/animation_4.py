from manim import *

class test(Scene):

    def construct(self):

        val = ValueTracker(4)
        num = always_redraw(lambda: DecimalNumber().set_value(val.get_value()))

        self.play(FadeToColor(num, color=RED))
        self.wait()
        self.play(val.animate.set_value(0), run_time=5, rate_func=linear)
        self.play(num.animate.set_value(5), run_time=3, rate_func=smooth)