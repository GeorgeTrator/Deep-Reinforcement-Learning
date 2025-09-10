from manim import *

config.pixel_height = 1080
config.pixel_width = 1920
config.frame_height = 8.0
config.frame_width = 14.0

class MatrixStandardization2(Scene):
    
    def construct(self):
        # Matrix 4x4 dos pesos
        W = Matrix(
            [[f"w_{{{i},{j}}}" for j in range(4)] for i in range(3)] + [["\\vdots" for _ in range(4)]],
            left_bracket="[" , right_bracket="]"
        )
        # Vetor de ativação
        a0 = Matrix(
            [[f"a^{{(0)}}_{{{i}}}"] for i in range(3)] + [["\\vdots"]],
            left_bracket="[" , right_bracket="]"
        )
        # Vetor dos bias
        b = Matrix(
            [[f"b_{{{i}}}"] for i in range(3)] + [["\\vdots"]],
            left_bracket="[" , right_bracket="]"
        )
        # Agrupamento: W * a0 + b
        expr = VGroup(W, a0, b).arrange(RIGHT, buff=1)

        # Colocar no centro
        expr.move_to(ORIGIN)

        # Adicionar multiplicação e soma
        mult = MathTex("*")
        plus = MathTex("+")
        symbols = VGroup(mult, plus).arrange(RIGHT, buff=1)
        symbols.next_to(W, RIGHT, buff=0.5)
        a0.next_to(mult, RIGHT, buff=0.5)
        plus.next_to(a0, RIGHT, buff=0.5)
        b.next_to(plus, RIGHT, buff=0.5)

        # Função de ativação Rectificed Linear Unit(...)
        relu = MathTex("ReLU(")
        close_paren = MathTex(")")
        relu.next_to(W, LEFT, buff=0.5)
        close_paren.next_to(b, RIGHT, buff=0.5)

        # Grupo final
        full_expr = VGroup(relu, W, mult, a0, plus, b, close_paren)
        full_expr.move_to(ORIGIN)

        self.play(Write(full_expr))
        self.wait(2)

        # Fórmula padrão
        std_formula = MathTex(
            "a^{(l)}  = ReLU\\left(W^{(l)} a^{(l-1)} + b^{(l)}\\right)" # \\left e \\right fazem o () proporcional
        )
        std_formula.move_to(ORIGIN)
        self.play(Transform(full_expr, std_formula))
        self.wait(2)
