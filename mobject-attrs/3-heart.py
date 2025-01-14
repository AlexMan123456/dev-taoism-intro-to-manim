from manim import *

class Heart(Scene):
    def construct(self):
        square = Square(color=RED).set_fill(RED).set_opacity(0.3).rotate(PI/4)
        circle = Circle(color=RED).set_fill(RED).set_opacity(0.3)

        circle_group = VGroup(circle.next_to(square, UL, aligned_edge=UP).shift(0.8*DOWN+1.85*RIGHT), circle.copy().next_to(square, UR, aligned_edge=UP).shift(0.8*DOWN+1.85*LEFT))

        self.add(circle_group, square)

# Run: manim mobject-attrs/3-heart.py -qm Heart