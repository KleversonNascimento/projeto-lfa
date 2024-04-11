import random
from automathon import DFA

# imaginar a máquina vista de cima como um quadrado assim:
# 1  2  3  4  5
# 6  7  8  9  10
# 11 12 13 14 15
# 16 17 18 19 20
# 21 22 23 24 25

# posição 13 é definida como inicial da garra e 23 é definida como abertura para saída das pelúcias

# definindo estados
estados = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
          '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
          '21', '22', '23', '24', '25', '26'}

# definindo alfabeto
alfabeto = {'inserir credito', 'mover para esquerda', 'mover para direita',
            'mover para frente', 'mover para trás', 'descer garra'}

# estado ao iniciar a máquina, sem créditos inseridos
estado_inicial = '0'

# posições fixas em que há ursinhos:
possui_ursinho = ['5', '7', '24']

# estado final no qual um ursinho é pego
estados_finais = {'26'}

# função para aleatorizar a chance de pegar um ursinho (50%)
def randomize(number: str) -> str:
    n = random.randrange(0, 100)
    if n > 50:
        return number
    return '26'

# tabela de transição, no formato que a lib automathon espera
transicoes_formato_lib = {
    '0': { 'mover para esquerda': '0', 'mover para direita': '0', 'mover para trás': '0', 'mover para frente': '0', 'descer garra': '0', 'inserir credito': '13' },
    '1': { 'mover para esquerda': '1', 'mover para direita': '2', 'mover para trás': '6', 'mover para frente': '1', 'descer garra': '0' , 'inserir credito': '1' },
    '2': { 'mover para esquerda': '1', 'mover para direita': '3', 'mover para trás': '7', 'mover para frente': '2', 'descer garra': '0' , 'inserir credito': '2' },
    '3': { 'mover para esquerda': '2', 'mover para direita': '4', 'mover para trás': '8', 'mover para frente': '3', 'descer garra': '0' , 'inserir credito': '3' },
    '4': { 'mover para esquerda': '3', 'mover para direita': '5', 'mover para trás': '9', 'mover para frente': '4', 'descer garra': '0' , 'inserir credito': '4' },
    '5': { 'mover para esquerda': '4', 'mover para direita': '5', 'mover para trás': '10', 'mover para frente': '5', 'descer garra': '26' , 'inserir credito': '5' },
    '6': { 'mover para esquerda': '6', 'mover para direita': '7', 'mover para trás': '11', 'mover para frente': '1', 'descer garra': '0' , 'inserir credito': '6' },
    '7': { 'mover para esquerda': '6', 'mover para direita': '8', 'mover para trás': '12', 'mover para frente': '2', 'descer garra': '26' , 'inserir credito': '7' },
    '8': { 'mover para esquerda': '7', 'mover para direita': '9', 'mover para trás': '13', 'mover para frente': '3', 'descer garra': '0' , 'inserir credito': '8' },
    '9': { 'mover para esquerda': '8', 'mover para direita': '10', 'mover para trás': '14', 'mover para frente': '4', 'descer garra': '0' , 'inserir credito': '9' },
    '10': { 'mover para esquerda': '9', 'mover para direita': '10', 'mover para trás': '15', 'mover para frente': '5', 'descer garra': '0' , 'inserir credito': '10' },
    '11': { 'mover para esquerda': '11', 'mover para direita': '12', 'mover para trás': '16', 'mover para frente': '6', 'descer garra': '0' , 'inserir credito': '11' },
    '12': { 'mover para esquerda': '11', 'mover para direita': '13', 'mover para trás': '17', 'mover para frente': '7', 'descer garra': '0' , 'inserir credito': '12' },
    '13': { 'mover para esquerda': '12', 'mover para direita': '14', 'mover para trás': '18', 'mover para frente': '8', 'descer garra': '0' , 'inserir credito': '13' },
    '14': { 'mover para esquerda': '13', 'mover para direita': '15', 'mover para trás': '19', 'mover para frente': '9', 'descer garra': '0' , 'inserir credito': '14' },
    '15': { 'mover para esquerda': '14', 'mover para direita': '15', 'mover para trás': '20', 'mover para frente': '10', 'descer garra': '0' , 'inserir credito': '15' },
    '16': { 'mover para esquerda': '16', 'mover para direita': '17', 'mover para trás': '21', 'mover para frente': '11', 'descer garra': '0' , 'inserir credito': '16' },
    '17': { 'mover para esquerda': '16', 'mover para direita': '18', 'mover para trás': '22', 'mover para frente': '12', 'descer garra': '0' , 'inserir credito': '17' },
    '18': { 'mover para esquerda': '17', 'mover para direita': '19', 'mover para trás': '23', 'mover para frente': '13', 'descer garra': '0' , 'inserir credito': '18' },
    '19': { 'mover para esquerda': '18', 'mover para direita': '20', 'mover para trás': '24', 'mover para frente': '14', 'descer garra': '0' , 'inserir credito': '19' },
    '20': { 'mover para esquerda': '19', 'mover para direita': '20', 'mover para trás': '25', 'mover para frente': '15', 'descer garra': '0' , 'inserir credito': '20' },
    '21': { 'mover para esquerda': '21', 'mover para direita': '22', 'mover para trás': '21', 'mover para frente': '16', 'descer garra': '0' , 'inserir credito': '21' },
    '22': { 'mover para esquerda': '21', 'mover para direita': '23', 'mover para trás': '22', 'mover para frente': '17', 'descer garra': '0' , 'inserir credito': '22' },
    '23': { 'mover para esquerda': '22', 'mover para direita': '24', 'mover para trás': '23', 'mover para frente': '18', 'descer garra': '0' , 'inserir credito': '23' },
    '24': { 'mover para esquerda': '23', 'mover para direita': '25', 'mover para trás': '24', 'mover para frente': '19', 'descer garra': '26' , 'inserir credito': '24' },
    '25': { 'mover para esquerda': '24', 'mover para direita': '25', 'mover para trás': '25', 'mover para frente': '20', 'descer garra': '0' , 'inserir credito': '25' },
    '26': { 'mover para esquerda': '26', 'mover para direita': '26', 'mover para trás': '26', 'mover para frente': '26', 'descer garra': '26' , 'inserir credito': '13' },
}

# usa a função randomize para fazer com que o ursinho seja pego em 50% das vezes ao descer a garra na posição correta
def preparar_transicoes(transicoes):
    for i in possui_ursinho:
        tr = transicoes.get(i)
        tr['descer garra'] = randomize(i)

# criação do AFD
automata = DFA(estados, alfabeto, transicoes_formato_lib, estado_inicial, estados_finais)

# verifica se o AFD é válido
print('O AFD é valido? ' + str(automata.is_valid()))

# sequência para pegar um ursinho na posição 24 em 50% das vezes
preparar_transicoes(transicoes_formato_lib)
print('Tentativa de pegar um ursinho com a entrada [inserir credito, mover para direita, mover para trás, mover para trás, descer garra]: ' + str(automata.accept(['inserir credito', 'mover para direita', 'mover para trás', 'mover para trás', 'descer garra'])))

# sequência para a posição 19 que não pega ursinho
preparar_transicoes(transicoes_formato_lib)
print('Tentativa de pegar um ursinho com a entrada [inserir credito, mover para direita, mover para direita, mover para trás, mover para esquerda, descer garra]: ' + str(automata.accept(['inserir credito', 'mover para direita', 'mover para direita', 'mover para trás', 'mover para esquerda', 'descer garra'])))

# sequência sem inserir créditos que nunca pega ursinho
preparar_transicoes(transicoes_formato_lib)
print('Tentativa de pegar um ursinho com a entrada [mover para direita, mover para direita, mover para trás, mover para esquerda, descer garra]: ' + str(automata.accept(['mover para direita', 'mover para direita', 'mover para trás', 'mover para esquerda', 'descer garra'])))
