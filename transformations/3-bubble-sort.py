from manim import *

class BubbleSort(Scene):
    def construct(self):
        self.bubble_sort([5,9,3,1,8,6,4,2,7])
    
    def bubble_sort(self, array):
        array_length = len(array)
        array_object = VGroup(*[VGroup(Square(0.7), MathTex(str(number))) for number in array]).arrange(buff=0)
        indexes = VGroup(*[MathTex(i).scale(0.7).next_to(array_object[i], UP, buff=0.15) for i in range(array_length)])

        self.add(array_object, indexes)

        i_pointer = VGroup()
        j_pointer = VGroup()
        reference_rectangle = Rectangle(width=1.4, height=0.7, color=RED)
        self.add_foreground_mobject(reference_rectangle)
        original_position = VGroup()
        end_pointer = VGroup()

        for i in range(array_length):
            i_pointer.add(VGroup(Triangle(color=BLUE, fill_color=BLUE, fill_opacity=1).scale(0.2), MathTex("i=" + str(i))).arrange(DOWN).next_to(array_object[i],DOWN))
            end = array_length - i - 1
            end_pointer.add(VGroup(i_pointer[0][0].copy().rotate(PI), MathTex(str(end)), Tex("(end)").scale(0.5)).arrange(UP).next_to(array_object[end], UP, buff=0.5))
            if i == 0:
                self.add(i_pointer[0], end_pointer[0])
            else:
                self.play(ReplacementTransform(end_pointer[i-1], end_pointer[i]), ReplacementTransform(i_pointer[i-1], i_pointer[i]))

            for j in range(end):
                j_pointer.add(VGroup(i_pointer[0][0].copy(), MathTex("j=" + str(j))).arrange(DOWN).next_to(array_object[j], DOWN, buff=1.3))
    
                if j == 0:
                    self.add(j_pointer[0], reference_rectangle.next_to(j_pointer[0], UP, buff=1.3).shift(RIGHT*0.35))
                    self.remove(original_position)
                    original_position = j_pointer[0].copy()
                else:
                    self.play(ReplacementTransform(j_pointer[j-1], j_pointer[j]), reference_rectangle.animate.next_to(j_pointer[j], UP, buff=1.3).shift(RIGHT*0.35))
                
                if array[j] > array[j+1]:
                    array[j], array[j+1] = array[j+1], array[j]
                    filled_rectangle = reference_rectangle.copy().set_fill(color=RED, opacity=0.3)
                    self.play(Transform(reference_rectangle, filled_rectangle, rate_func=there_and_back))

                    self.animate_swap(array_object, j, j+1)
                
                if j == end-1:
                        self.play(ReplacementTransform(j_pointer[j], original_position), reference_rectangle.animate.next_to(original_position, UP, buff=1.3).shift(RIGHT*0.35))
                        j_pointer = VGroup()
        
        self.wait()
        self.remove(reference_rectangle)
        self.wait(3)
        
    def animate_swap(self, array_object, lower_index, upper_index):
        smaller_number = array_object[upper_index].copy()
        bigger_number = array_object[lower_index].copy()

        self.add(smaller_number, bigger_number)
        self.remove(array_object[upper_index], array_object[lower_index])

        self.play(smaller_number.animate.move_to(array_object[lower_index]), bigger_number.animate.move_to(array_object[upper_index]))

        array_object[lower_index] = smaller_number.copy()
        array_object[upper_index] = bigger_number.copy()

        self.remove(smaller_number, bigger_number)
        self.add(array_object[lower_index], array_object[upper_index])

                
        



                


        
        


# Run: manim transformations/3-bubble-sort.py -qm BubbleSort