import numpy as np

def prever(X, w, b):
    return X * w + b

def perda(X, w, b, lr): #lr é learning rat, o quanto o peso aumenta ou diminui
    perda_total = np.average((preve(X, w, b) - y) ** 2)
    return perda_total
