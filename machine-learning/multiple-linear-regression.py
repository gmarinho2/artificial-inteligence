import numpy as np

def prever(X, w):
    return np.matmul(X, w)

def loss(X, Y, w):
    return np.average((prever(X, w) - Y) ** 2)

def gradiente(X, Y, w):
    return 2 * np.matmul(X.T, (prever(X, w) - Y)) / X.shape[0]

def treinamento(X, Y, iteracao, lr):
    w = np.zeros((X.shape[1], 1))
    for i in range(iteracao):
        w -= gradiente(X, Y, w) * lr
    return w


ARQUIVO = "life-expectancy-without-country-names.txt"
x1, x2, x3, y = np.loadtxt(ARQUIVO, skiprows=1, unpack=True)
X = np.column_stack((np.ones(x1.size), x1, x2, x3))
Y = y.reshape(-1, 1)
w = treinamento(X, Y, iteracao=1000, lr=0.000001)

print("\nPesos encontrados com o treinamento: \n", w)
print("\nPrevenedo de 1 a 10:")
for i in range(167):
    print("Estimativa %d : %.4f (Dados real: %d) \n" % (i+1, prever(X[i], w), Y[i]))


