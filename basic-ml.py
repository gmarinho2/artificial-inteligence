import numpy as np

def prever(X, w, b):
    return X * w + b

def perda(X, w, b, lr): #lr é learning rat, o quanto o peso aumenta ou diminui
    perda_total = np.average((preve(X, w, b) - y) ** 2)
    return perda_total

def treinamento(X, y, iteracoes,lr):
    w = 0
    b = 0
    perda = perda(X, Y, b, lr)
    for i in iteracoes:
        if perda(X, Y, w + lr, b) < perda: # Updating weight
            w += lr
        elif perda(X, Y, w - lr, b) < perda: # Updating weight
            w -= lr
        elif perda(X, Y, w, b + lr) < perda: # Updating bias
            b += lr
        elif perda(X, Y, w, b - lr) < perda: # Updating bias
            b -= lr
        else:
            return w, b

    raise Exception("Não converge.")