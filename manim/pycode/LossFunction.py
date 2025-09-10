from manim import *

config.pixel_height = 1080
config.pixel_width = 1920
config.frame_height = 8.0
config.frame_width = 14.0
config.frame_rate = 60

class LossFunction(Scene):
    
    def construct(self):
        # Dimensões da tela para posicionamento dinâmico
        frame_width = config.frame_width 
        frame_height = config.frame_height

        # Parâmetros da rede 
        input_count = 4
        hidden1_count = 16
        hidden2_count = 16
        output_count = 2

        # Calculando distância na camada com base no limite de neurônios visualizáveis
        # Defini desta forma para poder recilar o código
        max_neurons = max(input_count, hidden1_count, hidden2_count, output_count)
        
        # Espaço vertical
        vertical_spacing = min(0.8, frame_height * 0.8 / max_neurons)
        # Espaço horizontal 
        layer_count = 4 # input, hidden1, hidden2, output
        horizontal_spacing = frame_width * 0.5 / (layer_count - 1)

        # Posição inicial (centralizado)
        start_x = -frame_width / 2 + frame_width * 0.1

        layer_positions = [
            start_x,
            start_x + horizontal_spacing,
            start_x + 2 * horizontal_spacing,
            start_x + 3 * horizontal_spacing
        ]

        # O tamanho dos neurônios depende do espaço disponível na tela
        neuron_radius = min(0.3, vertical_spacing * 0.4)

        # Criar neurônios
        input_neurons = self.create_layer(input_count, layer_positions[0], 
                                         vertical_spacing, neuron_radius)
        hidden1_neurons = self.create_layer(hidden1_count, layer_positions[1], 
                                           vertical_spacing, neuron_radius * 0.7)
        hidden2_neurons = self.create_layer(hidden2_count, layer_positions[2], 
                                           vertical_spacing, neuron_radius * 0.7)
        output_neurons = self.create_layer(output_count, layer_positions[3], 
                                          vertical_spacing, neuron_radius)

        # Criar conexões
        connections = VGroup()

        # Conexão por camada

        # 1 - > 2
        for input_neuron in input_neurons:
            for hidden_neuron in hidden1_neurons:
                line = Line(input_neuron.get_right(), 
                            hidden_neuron.get_left(),
                            color = WHITE, stroke_width= 1)
                connections.add(line)

        # 2 - > 3
        for hidden_neuron in hidden1_neurons:
            for hidden2_neuron in hidden2_neurons:
                line = Line(hidden_neuron.get_right(),
                            hidden2_neuron.get_left(),
                            color = WHITE, stroke_width= 1)
                connections.add(line)
        # 3 - > 4
        for hidden2_neuron in hidden2_neurons:
            for output_neuron in output_neurons:
                line = Line(hidden2_neuron.get_right(),
                            output_neuron.get_left(),
                            color = WHITE, stroke_width = 1)
                connections.add(line)
        

        # Adicionando sem animar
        network = VGroup(input_neurons, hidden1_neurons, hidden2_neurons, output_neurons,
                         connections)
        self.add(network)
        self.play(network.animate.scale(0.5).to_corner(UL))

        # Começamos do final do feedforward
        # Mudamos as cores das conexões para sinalizar o feedback (backpropagation)

        feedback = []
        colrs = [RED, BLUE, GREY, GREEN, YELLOW, PURPLE, PINK, LIGHT_PINK, LIGHTER_GRAY, LIGHT_BROWN, LIGHTER_GREY]
        for i, connection in enumerate(reversed(connections)):
            feedback.append(connection.animate.set_color(colrs[i % len(colrs)]))
        
        self.play(LaggedStart(*feedback, lag_ratio=0.1, run_time=2))
        self.wait(1)

        # Função de custo 

        std_formula = MathTex(
            "a^{(l)}  = ReLU\\left(W^{(l)} a^{(l-1)} + b^{(l)}\\right)" # \\left e \\right fazem o () proporcional
        )
        # "vetor em treinamento"
        output_vector = Matrix(
            [[f"a^{{(3)}}_{{{i}}}"] for i in range(2)],
            left_bracket="[" , right_bracket="]"
        )
        output_vector.move_to(LEFT * 2)
        self.play(Create(output_vector))

        # "vetor verdade"
        target_vector = Matrix(
            [[f"Q_{i}"] for i in range(2)],
            left_bracket = "[", right_bracket="]"
        )
        target_vector.move_to(RIGHT * 2)
        #self.play(Create(target_vector))

        
        minus_sign = MathTex("-")
        #self.play(Create(minus_sign))

        pl = MathTex(r"\left(").match_height(output_vector)
        pl.move_to(output_vector.get_left() + LEFT * 0.1)
        pr = MathTex(r"\right)").match_height(target_vector)
        pr.move_to(target_vector.get_right() + RIGHT * 0.1)

        self.play(
            Create(pl),
            output_vector.animate.move_to(LEFT * 2.5),
            target_vector.animate.move_to(RIGHT * 2.5),
            minus_sign.animate.move_to(ORIGIN),
            Create(pr),
            run_time =1
        )
                # Informa que só pegamos um valor de cada vetor
        a0 = MathTex(f"a^{3}_{0}")
        q0 = MathTex(f"Q_{0}")

        a0.move_to(output_vector.center())
        a0.move_to(LEFT * 1.0)
        q0.move_to(target_vector.get_center())
        q0.move_to(RIGHT * 1.0)

        self.play(
            Transform(
                output_vector,
                a0
            ),
            run_time = 1
        )
        self.play(
            Transform(
                target_vector,
                q0
            ),
            run_time = 0.3
        )

        # Adiciona o quadrado e 1/2
        squared = MathTex("^2").next_to(pr, UP, buff=0.1)
        one_half = MathTex(r"\frac{1}{2}").next_to(pl, LEFT, buff=0.2)

        self.play(Create(squared), Create(one_half)) 

        
        exp = VGroup(one_half, pl, output_vector, target_vector, minus_sign, squared, pr)
        # Agora eu aplico um "transform" no conjunto "exp" e mostro, no lugar, uma função de custo possível.
        # Por simplificação, vou tomar a MSE, então tudo isso vai virar (NN - ALVO)²

        mse_formula = MathTex(r"\text{MSE} = \frac{1}{2n}\sum_{i=1}^{n}(a_i - Q_i)^2")

        # Esclarecimentos sobre a MSE
        simplified = Text("n = número de estados do BATCH", font_size = 24, color= WHITE)

        mse_formula.move_to(exp.get_center())
        simplified.move_to(mse_formula.get_center() + DOWN * 2)
        
        self.play(Transform(exp, mse_formula))
        self.play(Write(simplified))
        self.wait(2)
   
    def create_layer(self, neuron_count, x_position, spacing, radius):
        layer = VGroup()
        total_height = (neuron_count - 1) * spacing
        start_y = total_height / 2  # Center vertically
        
        for i in range(neuron_count):
            neuron = Circle(radius=radius, color=WHITE, fill_opacity=0.4)
            neuron.set_fill(BLACK)
            y_position = start_y - i * spacing
            neuron.move_to(x_position * RIGHT + y_position * UP)
            layer.add(neuron)
        
        return layer
