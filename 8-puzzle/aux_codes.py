class Arvore():
    def __init__(self, info):
        self.info = info
        self.filhos = []
        self.pai = None

    def add_no(self, no):
        no.pai = self
        self.filhos.append(no)

class Puzzle():
    def __init__(self):
        self.estadoObjetivo = [0,1,2,3,4,5,6,7,8]
        self.caminho = []

    def Up(posicao_do_vazio, Arvore):
        no_atual = Arvore.filho[0] #definindo filho 1 como 'up'
        #vazio representado por 0
        #para fazer a troca, faça apenas swap calculando a distancia necessaria entre o vetor 
        if(posicao_do_vazio>2):
            no_atual[posicao_do_vazio] = no_atual[posicao_do_vazio - 3]
            no_atual[posicao_do_vazio + 3] = 0
            return Arvore.filho[0]

    def Down(posicao_do_vazio, Arvore):
        no_atual = Arvore.filho[1] #definindo 1 como 'down'
        if(posicao_do_vazio<6):
            no_atual[posicao_do_vazio] = no_atual[posicao_do_vazio + 3]
            no_atual[posicao_do_vazio - 3] = 0
            return Arvore.filho[1]

    def Left(posicao_do_vazio, Arvore):
        no_atual = Arvore.filho[2] #definindo 2 como 'left'
        if(posicao_do_vazio!= 0 and posicao_do_vazio!=3 and posicao_do_vazio!=6):
            no_atual[posicao_do_vazio] = no_atual[posicao_do_vazio + 1]
            no_atual[posicao_do_vazio - 1] = 0
            return Arvore.filho[2]

    def Right(posicao_do_vazio, Arvore):
        no_atual = Arvore.filho[3] #definindo 3 como 'right'
        if(posicao_do_vazio!= 2 and posicao_do_vazio!=5 and posicao_do_vazio!=8):
            no_atual[posicao_do_vazio] = no_atual[posicao_do_vazio - 1]
            no_atual[posicao_do_vazio + 1] = 0
            return Arvore.filho[3]

    def verificaObjetivo(no_atual):
        if no_atual.info == self.estadoObjetivo:
            return salvaCaminho()
