from manim import *

class GridWithDots(Scene):
    def construct(self):
        grid = NumberPlane()
        dots = VGroup()

        for y in range(-3,4):
            for x in range(-6,7):
                dots.add(Dot().move_to([x,y,0]))
        
        self.add(grid, dots)
