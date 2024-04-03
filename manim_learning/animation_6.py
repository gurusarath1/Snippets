from manim import *
import math


class test(Scene):

    def construct(self):

        slope_line_x_val = ValueTracker(0.1)

        ax = Axes(x_range=[-1,15,1], y_range=[-1,10,1], x_length=10, y_length=10).to_edge(DL).add_coordinates().set_color(WHITE)

        func = ax.plot(lambda x: 3*x**2 - x**3, x_range=[0,10], color=RED)

        slop_line = always_redraw(lambda:
                                  ax.get_secant_slope_group(x=slope_line_x_val.get_value(), graph=func, dx=0.01, secant_line_color=GREEN, secant_line_length=3)
                                  )

        pt = always_redraw(lambda:
                           Dot().move_to(ax.c2p(slope_line_x_val.get_value(), func.underlying_function(slope_line_x_val.get_value())))
                           )

        self.add(ax, func, slop_line, pt)
        self.wait()
        self.play(slope_line_x_val.animate.set_value(4), run_time=5)
        self.wait()