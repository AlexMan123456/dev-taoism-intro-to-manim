from manim import *

class Chessboard(Scene):
    def construct(self):
        board = VGroup(*[
            VGroup(*[
                Square(1, color=WHITE, fill_color=WHITE if i%2 == j%2 else BLACK).set_opacity(1).move_to([-4+i, -4+j, 0]) for i in range(8)
            ]) 
        for j in range(8)]).scale(0.75)

        self.add(board)

# manim groups-and-vgroups/1-chessboard.py -qm Chessboard