# A estrutura do site é conforme o autômato abaixo:

#states
Sumário
ContextoGeral
RedesNeurais
MDP
QLearning
DQN
OutrosExemplos
RESUMO

#initial
Sumário

#accepting
RESUMO

#alphabet
próximo
anterior
pular_para_ContextoGeral
pular_para_RedesNeurais
pular_para_MDP
pular_para_QLearning
pular_para_DQN
pular_para_OutrosExemplos

#transitions
Sumário:próximo>ContextoGeral
Sumário:pular_para_ContextoGeral>ContextoGeral
Sumário:pular_para_RedesNeurais>RedesNeurais
Sumário:pular_para_MDP>MDP
Sumário:pular_para_QLearning>QLearning
Sumário:pular_para_DQN>DQN
Sumário:pular_para_OutrosExemplos>OutrosExemplos

ContextoGeral:próximo>RedesNeurais
ContextoGeral:anterior>Sumário

RedesNeurais:próximo>MDP
RedesNeurais:anterior>ContextoGeral

MDP:próximo>QLearning
MDP:anterior>RedesNeurais

QLearning:próximo>DQN
QLearning:anterior>MDP

DQN:próximo>OutrosExemplos
DQN:anterior>QLearning

OutrosExemplos:próximo>RESUMO
OutrosExemplos:anterior>DQN

RESUMO:próximo>Sumário
RESUMO:anterior>OutrosExemplos



Note que podemos construir outros autômatos, com base na relação (que ainda está sendo construída) abaixo: 
Apresentação (difícil)

APRESENTAÇÃO DRL (Muito difícil)
  - Contexto Geral (médio)
      - Histórico (fácil)
          - Frank Rosenblatt: o perceptron (fácil)
          - Inverno da IA (trivial)
          - Revolução do DeepMind (fácil)
      - Exemplo (1) Jogos Atari (2013~2014) DeepMind (trivial)
      - Exemplo (2) Drones (trivial)
      - Exemplo (3) Robótica (trivial)
  - Redes Neurais (Difícil)
  - MDP (médio)
  - Q-Learning (médio)
  - DQN (médio+)
  - Outros Exemplos (Fácil)
  - RESUMO (trivial)

