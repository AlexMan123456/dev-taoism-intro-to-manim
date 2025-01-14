from manim import *

class YinYang(Scene):
    def construct(self):
        big_semi_circle_left = self.create_semi_circle(radius=3, color=WHITE, fill_color=BLACK).rotate(PI/2, about_point=[0,0,0])
        big_semi_circle_right = big_semi_circle_left.copy().rotate(PI, about_point=[0,0,0]).set_fill(WHITE).set_opacity(1)

        small_top_semi_circle = self.create_semi_circle(radius=1.5, color=WHITE, fill_color=BLACK).set_opacity(1).rotate(-PI/2, about_point=[0,0,0]).shift(1.5*UP)
        small_bottom_semi_circle = small_top_semi_circle.copy().set_fill(WHITE).set_opacity(1).shift(1.5*DOWN).rotate(PI, about_point=[0,0,0]).shift(1.5*DOWN)

        small_top_circle = Circle(radius=0.25, color=WHITE, fill_color=WHITE).set_opacity(1).shift(1.5*UP)
        small_bottom_circle = small_top_circle.copy().set_color(BLACK).set_fill(BLACK).set_opacity(1).shift(3*DOWN)

        full_circle = VGroup(big_semi_circle_left, big_semi_circle_right)
        semi_circles = VGroup(small_top_semi_circle, small_bottom_semi_circle)

        self.add(full_circle, semi_circles, small_top_circle, small_bottom_circle)
    
    def create_semi_circle(self, radius, **fig_kwargs):
        big_circle = Circle(radius)
        semi_circle = VMobject(**fig_kwargs).set_points(
            big_circle.points[:int(len(big_circle.points)/2)]
        )

        return semi_circle


# Run: manim mobject-attrs/5-yin-yang.py -qm YinYang