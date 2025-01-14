from manim import *

class RustLogo(Scene):
    def construct(self):
        background_circle = Circle(3, WHITE).set_fill(WHITE).set_opacity(1)
        big_triangle = Triangle(color="#2FA673").set_fill("#2FA673").set_opacity(1).scale(2)
        medium_triangle = big_triangle.copy().set_color("#2A3C4E").set_fill("#2A3C4E").scale(0.6).next_to(big_triangle, DOWN, aligned_edge=DOWN).shift(1.16*UP)
        small_triangle = medium_triangle.copy().set_color(WHITE).set_fill(WHITE).scale(1.1).next_to(medium_triangle, DOWN, aligned_edge=DOWN)

        triangles = VGroup(big_triangle, medium_triangle, small_triangle).rotate(PI).move_to(background_circle.get_center()).shift(0.4*UP)

        self.add(background_circle, triangles)

# Run: manim mobject-attrs/4-rust-logo.py -qm RustLogo