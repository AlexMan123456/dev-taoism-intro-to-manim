from manim import *

class AligningObjects(Scene):
    def construct(self):
        objects = VGroup(Circle().to_edge(UL), Square(), Star(), Triangle(), Circle())

        for i in range(1,5):
            objects[i].next_to(objects[i-1], RIGHT, aligned_edge=UP)

        self.add(objects)

# Run: manim mobject-attrs/2-aligning-objects.py -qm AligningObjects