from manim import *
config.pixel_height = 1080  # Altura em pixels
config.pixel_width = 1920   # Largura em pixels
config.frame_height = 8.0   # Altura do espaço cartesiano
config.frame_width = 14.0   # Largura do espaço cartesiano

class Operation1(Scene):
    def construct(self):
        # Posição inicial centralizada
        start_pos = LEFT * 3 + UP * 1  
        
        # Criar os neurônios da camada 0 (input)
        input_neurons = VGroup()
        input_labels = VGroup()
        
        for i in range(4):
            neuron = Circle(radius=0.4, color=WHITE, fill_opacity=1)
            neuron.set_fill(BLACK)  # 
            neuron.move_to(start_pos + DOWN * i * 1.0)
            input_neurons.add(neuron)
            # Criar rótulo LaTeX
            label = MathTex(f"a_{i}^{0}", font_size = 28)
            label.move_to(neuron.get_center()) # Centrar no neurônio
            input_labels.add(label)
        
        # Criar neurônio da camada 1 (hidden)
        hidden_neuron = Circle(radius=0.4, color=WHITE, fill_opacity=1)
        hidden_neuron.set_fill(BLACK)
        hidden_neuron.move_to(input_neurons.get_center() + RIGHT * 4)

        # Rótulo do hidden neuron
        hidden_label = MathTex(r"a_{0}^{1}", font_size = 28)
        hidden_label.move_to(hidden_neuron.get_center())
        bias = MathTex(r"b^{1}_{0}", font_size = 28)
        bias.move_to(hidden_label.get_center() + RIGHT * 1.0)
        
        # Adicionar títulos
        input_title = Text("INPUT", font_size=24).next_to(input_neurons, UP, buff=0.3)
        layer0_text = Text("l = 0", font_size=20).next_to(input_title, UP, buff= 0.3)
        
        hidden_title = Text("CAMADA OCULTA", font_size=24).next_to(input_title, RIGHT, buff= 2.0)
        layer1_text = Text("l = 1", font_size=20).next_to(hidden_title, UP, buff= 0.3)

        # Adicionar conexões
        connections = VGroup()
        for neuron in input_neurons:
            line = Line(neuron.get_right(), hidden_neuron.get_left(), color=WHITE, stroke_width=1.0)
            connections.add(line)

        # Rótulo das conexões
        weight_labels = VGroup()
        for i, connection in enumerate(connections):
            weight_label = MathTex(f"w^{1}_{{{0,{i}}}}", font_size = 28)
            midpoint = connection.get_center()
            weight_label.move_to(midpoint + UP * 0.2) 
            weight_labels.add(weight_label)

        
        # Mostrar neurônios 
        self.play(Create(input_neurons), Create(hidden_neuron))
        self.play(Write(input_title), Write(hidden_title))
        self.play(Write(layer0_text), Write(layer1_text))
        # Mostrar conexões
        self.play(Create(connections), run_time = 1.0)
        # Mostrar rótulos
        self.play(Write(input_labels), Write(hidden_label))
        self.play(Write(weight_labels), run_time = 0.5)
        self.play(Write(bias), run_time = 0.1)

        clrs = [YELLOW, BLUE, GREEN, RED]
        for i, connection in enumerate(connections): 
            self.play(
                ShowPassingFlash(
                    input_neurons[i].copy().set_stroke(color=clrs[i]),
                    time_width=0.5
                ),
                run_time = 0.5
            )
            self.play(
                ShowPassingFlash(
                    hidden_neuron.copy().set_fill(color=PURPLE),
                    time_width=0.5
                ),
                run_time = 1
            )
            self.play(
                ShowPassingFlash(
                    connection.copy().set_stroke(color=clrs[i]),
                    time_width= 0.5,
                ),
                run_time = 0.5
            )


        self.wait(0.5)
        # Agrupando tudo
        network = VGroup(
            input_neurons, hidden_neuron, connections,
           input_labels, hidden_label, weight_labels,
           input_title, hidden_title, layer0_text, layer1_text, bias
        )
        # Movendo o conjunto agrupado
        #network.scale(0.3)
        self.play(network.animate.shift(LEFT * 2), run_time = 0.3)

        # Montando a fórmula explicitamente
        equal_sign = MathTex("=", font_size = 28)
        self.play(bias.animate.shift(UP * 1), run_time = 0.3)
        self.play(hidden_label.animate.shift(RIGHT * 1), run_time = 0.3)
        self.play(Write(equal_sign.move_to(hidden_label.get_right() + RIGHT * 0.5)))
        # É idêntico para os weights, vou reusar por preguiça
        self.play(input_labels[0].animate.move_to(equal_sign.get_right() + RIGHT * 0.5), run_time = 0.3)
        self.play(weight_labels[0].animate.move_to(input_labels[0].get_right() + RIGHT*0.3), run_time = 0.3)


        for i, input_label in enumerate(input_labels):
            if(i == 0):
                continue
            target_pos = input_labels[i-1].get_right() + RIGHT * 1.3
            self.play(input_label.animate.move_to(target_pos), run_time = 0.3)
            self.play(weight_labels[i].animate.move_to(input_label.get_right() + RIGHT*0.3), run_time = 0.3)

        plus_group = VGroup()
        for i, weight_label in enumerate(weight_labels):
            plus_sign = MathTex("+", font_size = 28)

            self.play(Write(plus_sign.move_to(weight_label.get_right() + RIGHT*0.3)))
            plus_group.add(plus_sign)
        self.play(bias.animate.move_to(plus_group[3].get_right() + RIGHT*0.1))
        explicit_sum = VGroup()
        explicit_sum.add(input_labels)
        explicit_sum.add(weight_labels)
        explicit_sum.add(plus_group)
        explicit_sum.add(bias)


        # Função de ativação rigorosamente escrita
        activation_formula = MathTex(
            r"a^{1}_{0} = ReLU(\left(\sum_{i=0}^{3} w^{1}_{0,i} a^{0}_{i} + b^{1}_{0}\right))",
            font_size = 36
        )

        activation_formula.move_to(explicit_sum.get_center() - DOWN * 1.0)

        #Renderizar fórmula 
        self.play(Write(activation_formula))
        self.wait(1.0)
