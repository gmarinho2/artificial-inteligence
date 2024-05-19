import random

class Ambiente:
    def __init__(self, tamanho, taxa):
        self.taxa = taxa
        self.sala = []
        i = 0
        while i < tamanho:
            self.sala.append(random.randint(0,1))
            i = i + 1

    def sujar_sala(self, posicao):
        i = 0
        while i < self.getTamanho():
            sujar = (random.random() <= self.taxa)
            if sujar and i != posicao:
                self.sala[i] = 1
            i = i + 1

    def getTamanho(self):
        return len(self.sala)

class AgenteAspiradorReativo:
    def __init__(self, ambiente, posicao, tempo):

        direcao = 1 #comeca andando pra direita/starts going right
        self.pontuacao = 0

        for i in range(0, tempo):
            ambiente.sujar_sala(posicao)
            print("Iteração: ", i)
            print("Posição atual: ", posicao)
            if ambiente.sala[posicao] == 0:
                if direcao == 1 and posicao + direcao == ambiente.getTamanho(): 
                    direcao = -1                            #esses dois ifs testam pra ver se ta fora de range
                if direcao == -1 and posicao + direcao < 0: #both ifs check to see if its out of range
                    direcao = 1

                posicao = posicao + direcao

                print("Posição atual: ", posicao)
                print("Estado atual da sala:", meu_ambiente.sala)
                print("") #when it goes to other room, it doesnt clean, we can confirme that when printing
            else:
                ambiente.sala[posicao] = 0      #limpa a sala/cleans the room
                self.pontuacao = self.pontuacao + 1
                print("Estado atual da sala:", meu_ambiente.sala)
                print("")

    def getPonto(self):
        return self.pontuacao

#TESTS:

meu_ambiente = Ambiente(2, 0.2) #number of rooms and chance of getting dirty/quantidade de salas e chance de sujar
print("Estado inicial: ", meu_ambiente.sala)
print(" ")

meu_agente = AgenteAspiradorReativo(meu_ambiente, 0, 1000) #(ambiente, posicao, tempo)

print("Estado final: ", meu_ambiente.sala)
print("Pontuação final: ", meu_agente.getPonto())