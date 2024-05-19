import numpy as np

def prever(X, w, b):
    return X * w + b

def perda(X, Y, w, b):
    return np.average((prever(X, w, b) - Y) ** 2)

def treinamento(X, Y, iteracao, lr):
    w = b = 0
    for i in range(iteracao):
        perda_atual = perda(X, Y, w, b)
        if i % 300 == 0:
            print("Iteração %4d => perda: %.6f" % (i, perda_atual))

        if perda(X, Y, w + lr, b) < perda_atual: # atualizando o coeficiente angular(loss/perda), para mais ou menos
            w += lr
        elif perda(X, Y, w - lr, b) < perda_atual:
            w -= lr
        elif perda(X, Y, w, b + lr) < perda_atual: # atualizando o coeficiente linear (bias/viés), para mais ou menos
            b += lr
        elif perda(X, Y, w, b - lr) < perda_atual:
            b -= lr
        else:
            return w, b

    raise Exception("Não converge em %d iterações" % iteracao)


# Import the dataset
X, Y = np.loadtxt("pizza.txt", skiprows=1, unpack=True)

# treinamento the system
w, b = treinamento(X, Y, iteracao=10000, lr=0.01)
print("\nw = %.3f, b = %.3f" % (w, b))

# prever the number of pizzas
previsao = prever(20, w, b) 
print("Previsão: x = %d => y = %.2f" % (20, previsao))