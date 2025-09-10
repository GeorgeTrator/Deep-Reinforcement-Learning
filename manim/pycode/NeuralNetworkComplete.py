from manim import *
# NOTA: vou trabalhar com menos neuronios nas camadas ocultas, só pra não encher tanto o saco na hora de redimensionar.


# I usually don't comment my codes in Portuguese :P

config.pixel_height = 1080
config.pixel_width = 1920
config.frame_height = 8  # altura padrão
config.frame_width = 14  # ajusta para 16:9
# Alternativa:
#manim -pql your_file.py NeuralNetwork --resolution 1920,1080
# O significado de algumas constantes. 1.0, 0.0 são valores relativos à resolução usada (só teste)
#RIGHT = np.array([1.0, 0.0, 0.0])
#LEFT = np.array([-1.0, 0.0, 0.0])
#UP = np.array([0.0, 1.0, 0.0])
#DOWN = np.array([0.0, -1.0, 0.0])
#OUT = np.array([0.0, 0.0, 1.0]) (towards the viewer)
#IN = np.array([0.0, 0.0, -1.0]) (into the screen)
#Por padrão, a câmera Manim vê um quadrado de -7 unidades a +7 unidades no eixo x, e -4 unidades a +4 unidades em y (se 16:9)
#Logo, a tela visível tem 14 unidades de comprimento e 8 de altura
# Cada "1.0 unidade" como vista no np.array é uma fração dessa tela. 


# OBS: o nome do arquivo mp4 é o nome da classe principal (se usado o comando manim -p main.py nomeClasse)

class NeuralNetworkComplete(Scene):
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
        horizontal_spacing = frame_width * 0.8 / (layer_count - 1)

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

        # Agrupar todos os neurônios
        network = VGroup(input_neurons, hidden1_neurons, hidden2_neurons, output_neurons)

        # Centralizar a rede neural
        network.move_to(ORIGIN)

        # Criar conexões
        connections = VGroup()

        # Conexão por camada

        # 1 - > 2
        for input_neuron in input_neurons:
            for hidden_neuron in hidden1_neurons:
                line = Line(input_neuron.get_right(), 
                            hidden_neuron.get_left(),
                            color = YELLOW, stroke_width=1)
                connections.add(line)

        # 2 - > 3
        for hidden_neuron in hidden1_neurons:
            for hidden2_neuron in hidden2_neurons:
                line = Line(hidden_neuron.get_right(),
                            hidden2_neuron.get_left(),
                            color = YELLOW, stroke_width= 1)
                connections.add(line)
        # 3 - > 4
        for hidden2_neuron in hidden2_neurons:
            for output_neuron in output_neurons:
                line = Line(hidden2_neuron.get_right(),
                            output_neuron.get_left(),
                            color = YELLOW, stroke_width = 1)
                connections.add(line)
        
        # Sequência de animação
        self.play(Create(input_neurons), run_time = 1)
        self.play(Create(hidden1_neurons), run_time = 1)
        self.play(Create(hidden2_neurons), run_time = 1)
        self.play(Create(output_neurons), run_time = 1)

        self.wait(0.5)

        # Animar conexões
        self.play(Create(connections), run_time = 3)
        self.wait(1)

    def create_layer(self, neuron_count, x_position, spacing, radius):
        layer = VGroup()
        total_height = (neuron_count - 1) * spacing
        start_y = total_height / 2  # Center vertically
        
        for i in range(neuron_count):
            neuron = Circle(radius=radius, color=WHITE, fill_opacity=0.8)
            neuron.set_fill(BLACK)
            y_position = start_y - i * spacing
            neuron.move_to(x_position * RIGHT + y_position * UP)
            layer.add(neuron)
        
        return layer
