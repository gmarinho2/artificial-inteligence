class No():
    def __init__(self, filho):
        self.filho = filho

class Arvore():
    def __init__(self, no):
        self.inicio = no
        self.final = no

    def add_no(self, no):
        self.final.filho = no

def Up(posicao_do_vazio, No):

    no_atual = No
    #vazio representado por 0
    #para fazer a troca, faça apenas swap calculando a distancia necessaria entre o vetor 
    if(posicao_do_vazio>2):
        no_atual[posicao_do_vazio] = no_atual[posicao_do_vazio - 3]
        no_atual[posicao_do_vazio + 3] = 0

    return no_atual