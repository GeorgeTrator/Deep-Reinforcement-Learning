document.addEventListener('DOMContentLoaded', function() {
    const mainContainer = document.getElementById('main-container');
    // Definindo o autômato
    const automaton = {
        states: ['Sumário', 'Contexto Geral', 'Redes Neurais', 'MDP', 'Q-Learning', 'DQN', 'Outros Exemplos', 'RESUMO'],
        currentState: 'Sumário',
        initial: 'Sumário',
        accepting: 'RESUMO',
        transitions: {
            'Sumário': {
                'próximo': 'Contexto Geral',
                'pular_para_Contexto Geral': 'Contexto Geral',
                'pular_para_Redes Neurais': 'Redes Neurais',
                'pular_para_MDP': 'MDP',
                'pular_para_Q-Learning': 'Q-Learning',
                'pular_para_DQN [Deep-Q-Network]': 'DQN',
                'pular_para_Outros Exemplos': 'Outros Exemplos'
            },
            'Contexto Geral': {
                'próximo': 'Redes Neurais',
                'anterior': 'Sumário'
            },
            'Redes Neurais': {
                'próximo': 'MDP',
                'anterior': 'Contexto Geral'
            },
            'MDP': {
                'próximo': 'Q-Learning',
                'anterior': 'Redes Neurais'
            },
            'Q-Learning': {
                'próximo': 'DQN',
                'anterior': 'MDP'
            },
            'DQN': {
                'próximo': 'Outros Exemplos',
                'anterior': 'Q-Learning'
            },
            'Outros Exemplos': {
                'próximo': 'RESUMO',
                'anterior': 'DQN'
            },
            'RESUMO': {
                'próximo': 'Sumário',
                'anterior': 'Outros Exemplos'
            }
        }
    };

    // Função para mudar de estado
    function changeState(action) {
        const nextState = automaton.transitions[automaton.currentState][action];
        if (nextState) {
            // Direção da animação <- ou ->
            const direction = (action == 'próximo') ? 'slide-left' : 'slide-right';
            animateTransition(nextState, direction);
        }
    }

    function animateTransition(nextState, direction){
        // classe de saída
        mainContainer.classList.add(direction, 'fade-out');

        // Espera animação terminar antes de trocar o conteúdo

        setTimeout(() => {
            automaton.currentState = nextState;
            renderState();

            // Remove classes de saída e adiciona de entrada
            mainContainer.classList.remove('fade-out', 'slide-left', 'slide-right');
            mainContainer.classList.add('fade-in');

            // Remove a animação de entrada
            setTimeout(() => {
                mainContainer.classList.remove('fade-in');
            }, 300);


        }, 300);
    }

    // Função principal de renderização
    function renderState() {
        mainContainer.innerHTML = '';
        
        switch(automaton.currentState) {
            case 'Sumário':
                renderSummary();
                break;
            case 'Contexto Geral':
                renderContextoGeral();
                return;
            case 'Redes Neurais':
                renderRedesNeurais();
                break;
            case 'MDP':
                renderMDP();
                break;
            case 'Q-Learning':
                renderQLearning();
                break;
            case 'DQN':
                renderDQN();
                break;
            case 'Outros Exemplos':
                renderOutrosExemplos();
                break;
            case 'RESUMO':
                renderResumo();
                break;
        }
        
        // Adicionar botões de navegação
        addNavigationButtons();
    }

    // Função para adicionar botões de navegação
    function addNavigationButtons() {
        // Botão próximo (avançar)
        const nextButton = document.createElement('div');
        nextButton.className = 'nav-button next-button';
        nextButton.innerHTML = '<i class="fas fa-chevron-right"></i>';
        nextButton.addEventListener('click', () => changeState('próximo'));
        
        // Botão anterior (voltar)
        const prevButton = document.createElement('div');
        prevButton.className = 'nav-button prev-button';
        prevButton.innerHTML = '<i class="fas fa-chevron-left"></i>';
        prevButton.addEventListener('click', () => changeState('anterior'));
        
        mainContainer.appendChild(prevButton);
        mainContainer.appendChild(nextButton);
    }

    // Renderização do Sumário (já existente)
    function renderSummary() {
        mainContainer.style.justifyContent = 'flex-start';
        mainContainer.style.padding = '30px 0';
        
        const title = document.createElement('h1');
        title.className = 'summary-title';
        title.textContent = 'SUMÁRIO';
        
        const topics = [
            'Contexto Geral',
            'Redes Neurais',
            'MDP',
            'Q-Learning',
            'DQN [Deep-Q-Network]',
            'Outros Exemplos'
        ];
        
        const topicsContainer = document.createElement('div');
        topicsContainer.className = 'topics-container';
        
        topics.forEach((topic, index) => {
            const topicItem = document.createElement('div');
            topicItem.className = 'topic-item';
            topicItem.textContent = `${index + 1}) ${topic}`;
            
            // Adicionar eventos de clique para pular para seções
            topicItem.addEventListener('click', () => {
                const action = `pular_para_${topic}`;
                if (automaton.transitions['Sumário'][action]) {
                    changeState(action);
                }
            });
            
            topicsContainer.appendChild(topicItem);
        });
        
        mainContainer.appendChild(title);
        mainContainer.appendChild(topicsContainer);
    }

    // Funções de renderização para outros estados (placeholders por enquanto)

    function renderContextoGeral() {
    const internalAutomaton = {
        states: ['McCarthy', 'Rosenblatt', 'InvernoIA', 'Ressurgimento'],
        currentState: 'McCarthy',
        transitions: {
            'McCarthy': {
                'próximo': 'Rosenblatt',
                'anterior': null
            },
            'Rosenblatt': {
                'próximo': 'InvernoIA',
                'anterior': 'McCarthy'
            },
            'InvernoIA': {
                'próximo': 'Ressurgimento',
                'anterior': 'Rosenblatt'
            },
            'Ressurgimento': {
                'próximo': null,
                'anterior': 'InvernoIA'
            }
        }
    };

    function renderInternalState() {
        mainContainer.innerHTML = '';
        
        switch(internalAutomaton.currentState) {
            case 'McCarthy':
                renderMcCarthy();
                break;
            case 'Rosenblatt':
                renderRosenblatt();
                break;
            case 'InvernoIA':
                renderInvernoIA();
                break;
            case 'Ressurgimento':
                renderRessurgimento();
                break;
        }
        
        addInternalNavigationButtons();
    }

    function changeInternalState(action) {
        const nextState = internalAutomaton.transitions[internalAutomaton.currentState][action];
        if (nextState === null && action === 'próximo') {
            // Avançar para o próximo estado macro
            animateTransition('Redes Neurais', 'slide-left');
        } else if (nextState) {
            const direction = (action === 'próximo') ? 'slide-left' : 'slide-right';
            animateInternalTransition(nextState, direction);
        }
    }

    function animateInternalTransition(nextState, direction) {
        mainContainer.classList.add(direction, 'fade-out');

        setTimeout(() => {
            internalAutomaton.currentState = nextState;
            renderInternalState();

            mainContainer.classList.remove('fade-out', 'slide-left', 'slide-right');
            mainContainer.classList.add('fade-in');

            setTimeout(() => {
                mainContainer.classList.remove('fade-in');
            }, 300);
        }, 300);
    }

    function addInternalNavigationButtons() {
        const nextButton = document.createElement('div');
        nextButton.className = 'nav-button next-button';
        nextButton.innerHTML = '<i class="fas fa-chevron-right"></i>';
        nextButton.addEventListener('click', () => changeInternalState('próximo'));
        
        const prevButton = document.createElement('div');
        prevButton.className = 'nav-button prev-button';
        prevButton.innerHTML = '<i class="fas fa-chevron-left"></i>';
        prevButton.addEventListener('click', () => changeInternalState('anterior'));
        
        mainContainer.appendChild(prevButton);
        mainContainer.appendChild(nextButton);
    }

    function renderMcCarthy() {
        const container = document.createElement('div');
        container.className = 'contexto-geral-container';

        const title = document.createElement('h1');
        title.className = 'contexto-geral-title';
        title.textContent = 'Contexto Geral: McCarthy e a IA';
        container.appendChild(title);

        const content = document.createElement('div');
        content.className = 'contexto-geral-content';

        const leftSide = document.createElement('div');
        leftSide.className = 'contexto-geral-left';

        const text1 = document.createElement('div');
        text1.className = 'mccarthy-text-item';
        text1.textContent = 'Modelo Estatístico Multivariável?';
        const xIcon = document.createElement('i');
        xIcon.className = 'fas fa-times mccarthy-icon mccarthy-icon-times';
        text1.appendChild(xIcon);

        const text2 = document.createElement('div');
        text2.className = 'mccarthy-text-item';
        text2.textContent = 'Inteligência Artificial';
        const checkIcon = document.createElement('i');
        checkIcon.className = 'fas fa-check mccarthy-icon mccarthy-icon-check';
        text2.appendChild(checkIcon);

        leftSide.appendChild(text1);
        leftSide.appendChild(text2);

        const rightSide = document.createElement('div');
        rightSide.className = 'mccarthy-image-container';
        const image = document.createElement('img');
        image.className = 'mccarthy-image';
        image.src = 'imgs/McCarthy.jpg';
        image.alt = 'John McCarthy';
        rightSide.appendChild(image);

        content.appendChild(leftSide);
        content.appendChild(rightSide);

        container.appendChild(content);

        const footer = document.createElement('div');
        footer.className = 'contexto-geral-footer';
        footer.textContent = 'Não é inteligente nem artificial';
        container.appendChild(footer);

        mainContainer.appendChild(container);
    }

    function renderRosenblatt() {
        mainContainer.innerHTML = '<h1>Rosenblatt: Perceptron</h1><p>Conteúdo sobre Rosenblatt e o perceptron</p>';
    }

    function renderInvernoIA() {
        mainContainer.innerHTML = '<h1>Inverno da IA</h1><p>Conteúdo sobre o inverno da IA</p>';
    }

    function renderRessurgimento() {
        mainContainer.innerHTML = '<h1>Ressurgimento da IA</h1><p>Conteúdo sobre o ressurgimento da IA por volta de 2013</p>';
    }

    renderInternalState();
}

  
    function renderRedesNeurais() {
        mainContainer.innerHTML = '<h1>Redes Neurais</h1><p>Conteúdo sobre Redes Neurais</p>';
    }

    function renderMDP() {
        mainContainer.innerHTML = '<h1>MDP (Processo de Decisão Markov)</h1><p>Conteúdo sobre MDP</p>';
    }

    function renderQLearning() {
        mainContainer.innerHTML = '<h1>Q-Learning</h1><p>Conteúdo sobre Q-Learning</p>';
    }

    function renderDQN() {
        mainContainer.innerHTML = '<h1>DQN (Deep Q-Network)</h1><p>Conteúdo sobre DQN</p>';
    }

    function renderOutrosExemplos() {
        mainContainer.innerHTML = '<h1>Outros Exemplos</h1><p>Conteúdo sobre outros exemplos</p>';
    }

    function renderResumo() {
        mainContainer.innerHTML = '<h1>Resumo</h1><p>Conteúdo do resumo da apresentação</p>';
    }

    // Inicializar a aplicação
    renderState();
});
