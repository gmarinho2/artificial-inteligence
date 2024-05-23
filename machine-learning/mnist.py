import numpy as np
import gzip
import struct

def carrega_imagem(arquivo):
    with gzip.open(arquivo, 'rb') as f:
        _ignored, n_images, columns, rows = struct.unpack('>IIII', f.read(16))

        pixels = np.frombuffer(f.read(), dtype=np.uint8)

        X = pixels.reshape(n_images, columns * rows)
    return X

def carrega_label(arquivo):
    with gzip.open(arquivo, 'rb') as f:
        f.read(8) #pula o cabeçalho
        labels = f.read() #le os labels pra uma lista
        Y = np.frombuffer(labels, dtype=np.uint8).reshape(-1, 1) #coloca a lista no formato de uma matriz de uma coluna
    return Y

def add_bias(X):
    X = np.insert(X, 0, 1, axis=1)
    return X

def encode_number(Y, digit):
    encoded_Y = np.zeros_like(Y)
    n_labels = Y.shape[0]
    for i in range(n_labels):
        if Y[i] == digit:
            encoded_Y[i][0] = 1
    return encoded_Y


LABEL_TREINAMENTO = carrega_label("data/mnist/train-labels-idx1-ubyte.gz")
LABEL_TESTE = carrega_label("data/mnist/t10k-labels-idx1-ubyte.gz")


X_treino = add_bias(carrega_imagem("data/mnist/train-images-idx3-ubyte.gz"))
X_teste = add_bias(carrega_imagem("data/mnist/t10k-images-idx3-ubyte.gz"))

Y_treino = []
Y_teste = []

for algarismo in range(10):
    Y_treino.append(encode_number(LABEL_TREINAMENTO, algarismo))
    Y_teste.append(encode_number(LABEL_TESTE, algarismo))