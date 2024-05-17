import argparse
from collections import deque
from memory_profiler import profile
import time
import psutil


estado_inicial = list()
estado_objetivo = [0, 1, 2, 3, 4, 5, 6, 7, 8]
no_objetivo = None
tamanho_puzzle = 0
largura_puzzle = 0
nos_expandidos = 0
memoria_usada = 0

class Estado():
    def __init__(self, estado, pai, acao, profundidade, custo, chave=0):
        self.estado = estado
        self.pai = pai
        self.acao = acao
        self.profundidade = profundidade
        self.custo = custo
        self.chave = chave
        self.mapa = "".join(str(e) for e in self.estado) if self.estado else ""

def bfs(iniciar_estado):
    global no_objetivo
    explorado = set()
    fila = deque([Estado(iniciar_estado, None, None, 0, 0)])

    while fila:
        no = fila.popleft()
        explorado.add(no.mapa)

        if no.estado == estado_objetivo:
            no_objetivo = no
            return fila

        vizinhos = expandir(no)

        for vizinho in vizinhos:
            if vizinho.mapa not in explorado:
                fila.append(vizinho)
                explorado.add(vizinho.mapa)

def dfs_limitada(iniciar_estado, l):
    global no_objetivo
    explorado = set()
    pilha = deque([Estado(iniciar_estado, None, None, 0, 0)])

    while pilha:
        no = pilha.pop()
        explorado.add(no.mapa)

        if no.estado == estado_objetivo:
            no_objetivo = no
            return pilha

        vizinhos = reversed(expandir(no))

        for vizinho in vizinhos:
            if vizinho.mapa not in explorado and vizinho.profundidade <= l:
                pilha.append(vizinho)
                explorado.add(vizinho.mapa)

def dfs(iniciar_estado):
    return dfs_limitada(iniciar_estado, 362880)

def idfs(iniciar_estado):
    profundidade = 0
    pilha = None
    while no_objetivo is None:
        pilha = dfs_limitada(iniciar_estado, profundidade)
        profundidade += 1
    return pilha

def expandir(no):
    global nos_expandidos
    nos_expandidos += 1
    vizinhos = []
    vizinhos.append(Estado(mover(no.estado, 1), no, 1, no.profundidade + 1, no.custo + 1))
    vizinhos.append(Estado(mover(no.estado, 2), no, 2, no.profundidade + 1, no.custo + 1))
    vizinhos.append(Estado(mover(no.estado, 3), no, 3, no.profundidade + 1, no.custo + 1))
    vizinhos.append(Estado(mover(no.estado, 4), no, 4, no.profundidade + 1, no.custo + 1))
    nos = [vizinho for vizinho in vizinhos if vizinho.estado]
    return nos

def mover(estado, posicao):
    estado_novo = estado[:]
    indice = estado_novo.index(0)

    if posicao == 1: #subir
        novo_indice = indice - 3
        if novo_indice not in range(0, tamanho_puzzle):
            return None

    if posicao == 2: #descer
        novo_indice = indice + 3
        if novo_indice not in range(0, tamanho_puzzle):
            return None

    if posicao == 3: #esquerda
        novo_indice = indice - 1
        if indice % largura_puzzle == 0:
            return None

    if posicao == 4: #direita
        novo_indice = indice + 1
        if (indice + 1) % largura_puzzle == 0:
            return None

    estado_novo[indice], estado_novo[novo_indice] = estado_novo[novo_indice], estado_novo[indice]
    return estado_novo

def executar(fronteira):
    tempo_inicial = time.time()

    if no_objetivo is None:
        return

    caminho = []
    no = no_objetivo
    while no.pai is not None:
        if no.acao == 1:
            caminho.append('up')
        elif no.acao == 2:
            caminho.append('down')
        elif no.acao == 3:
            caminho.append('left')
        elif no.acao == 4:
            caminho.append('right')
        no = no.pai

    caminho.reverse()

    tempo_final = time.time()

    tempo_rodado = tempo_final - tempo_inicial
    memoria_usada = psutil.virtual_memory().used

    print("path_to_goal:", caminho)
    print("cost_of_path:", no_objetivo.custo)
    print("nodes_expanded:", nos_expandidos)
    print("fringe_size:", len(fronteira))
    print("search_depth:", no_objetivo.profundidade)
    print("max_search_depth:", no_objetivo.profundidade)
    print("running_time:", tempo_rodado)
    print("max_ram_usage in bytes:", memoria_usada)

mapeamento_funcoes = {
    'bfs': bfs,
    'dfs': dfs,
    'idfs': idfs,
}

def ler(config):
    global tamanho_puzzle, largura_puzzle
    dados = config.split(",")

    for elemento in dados:
        estado_inicial.append(int(elemento))

    tamanho_puzzle = len(estado_inicial)
    largura_puzzle = int(tamanho_puzzle ** 0.5)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('algoritmo')
    parser.add_argument('sequencia')
    args = parser.parse_args()

    ler(args.sequencia)
    function = mapeamento_funcoes[args.algoritmo]
    fronteira = function(estado_inicial)
    executar(fronteira)

if __name__ == '__main__':
    main()