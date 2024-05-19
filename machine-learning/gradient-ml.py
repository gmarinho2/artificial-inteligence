import numpy as np

def prever(X, w, b):
    return X * w + b

def perda(X, Y, w, b):
    return np.average((prever(X, w, b) - Y) ** 2)

def gradiente(X, Y, w, b):
    w_gradiente =  2 * np.average(X * (prever(X, w, b) - Y))    #derivada parcial de w
    b_gradiente =  2 * np.average((prever(X, w, b) - Y))        #derivada parcial de b
    return w_gradiente, b_gradiente

def treinamento(X, Y, iteracao, lr):
    w = b = 0
    for i in range(iteracao):
        perda_atual = perda(X, Y, w, b)

        print("Iteração %4d => perda: %.6f" % (i, perda_atual))

        w_gradiente, b_gradiente = gradiente(X, Y, w, b)
        w = w - w_gradiente * lr
        b = b - b_gradiente * lr
    
    return w, b

#importanto os dados 
X, Y = np.loadtxt("pizza.txt", skiprows=1, unpack=True)

# treinamento do sistema
w, b = treinamento(X, Y, iteracao=20000, lr=0.001)
print("\nw = %.3f, b = %.3f" % (w, b))

# prever numero de pizzas
previsao = prever(20, w, b) 
print("Previsão: x = %d => y = %.2f" % (20, previsao))