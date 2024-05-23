import numpy as np

def prever(X, w):
    return np.matmul(X, w)

def perda(X, Y, w):
    return np.average((prever(X, w) - Y) ** 2)

def gradiente(X, Y, w):
    return (2 / X.shape[0]) * np.matmul(X.T, (prever(X, w) - Y)) 

def treinamento(X, Y, iteracao, lr):
    w = np.zeros((X.shape[1], 1))
    for i in range(iteracao):
        w -= gradiente(X, Y, w) * lr
    return w

ARQUIVO = "dados/life-expectancy-without-country-names.txt"
x1, x2, x3, y = np.loadtxt(ARQUIVO, skiprows=1, unpack=True)
X = np.column_stack((np.ones(x1.size), x1, x2, x3))
Y = y.reshape(-1, 1)
w = treinamento(X, Y, iteracao=1000, lr=0.000001)

print("Previsões: ")
for i in range(Y.size):
    print("Nível de poluição: %.4f " % (X[i][1]))
    print("Nível de sistema de saúde: %.4f " % (X[i][2]))
    print("Nível de qualidade de água: %.4f "% (X[i][3]))
    print("Expectativa de vida prevista: %.3f \nExpectativa real: %d\n" % (prever(X[i], w), Y[i]))