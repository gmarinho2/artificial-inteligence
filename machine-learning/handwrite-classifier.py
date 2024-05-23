import numpy as np
import mnist as data
import matplotlib.pyplot as plt

def sigmoide(z):
    return 1 / (1 + np.exp(-z))

def propagacao(X, w):
    somatorio = np.matmul(X, w)
    return sigmoide(somatorio)

def classificar(X, w):
    probabilidades = propagacao(X, w)
    return np.round(probabilidades)

def perda(X, w, Y): #diferença entre previsao e realidade, USA-SE log loss
    previsoes = propagacao(X,w)
    primeiro = Y * np.log(propagacao)
    segundo = (1 - Y) * np.log(1 - propagacao)
    return (-1/Y.size) * (primeiro + segundo)

def gradiente(X, w, Y):                                  #usamos propagação aqui pois representa a curva suave,
    return np.matmul(X.T, (propagacao(X, w) - Y)) / X.shape[0] #variando de 0 a 1, o que permite utilizar a tecnica do gradiente

def treinamento(X, Y, iteracao, lr):
    w = np.zeros((X.shape[1], 1))
    for i in range (iteracao):
        w -= gradiente(X,w,Y) * lr
    return w

def teste(X, Y, w, algarismo):
    num_total = X.shape[0]
    resultados_corretos = np.sum(classificar(X, w) == Y)
    porcentagem_sucesso = resultados_corretos * 100 / num_total
    print("Taxa de sucesso para o digito %d: %d/%d (%.2f%%)" % (algarismo, resultados_corretos, num_total, porcentagem_sucesso))

#testando:
for algarismo in range(10):
    w = treinamento(data.X_treino, data.Y_treino[algarismo], iteracao=100, lr=1e-5) #lr=1e-5
    teste(data.X_teste, data.Y_teste[algarismo], w, algarismo)