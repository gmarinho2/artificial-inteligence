import numpy as np


ARQUIVO = "life-expectancy-without-country-names.txt"
y = np.loadtxt(ARQUIVO, skiprows=1, unpack=True)

dimensoes = input('Quantas variáveis serão utilizadas: ')
print(dimensoes)