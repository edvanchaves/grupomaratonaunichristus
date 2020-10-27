import math

linha1 = input()
linha2 = input()

ponto1 = linha1.split(' ')
ponto2 = linha2.split(' ')


def logica(param1, param2):
    return (float(param2) - float(param1)) ** 2


primeiraParte = logica(ponto1[0], ponto2[0])
segundaParte = logica(ponto1[1], ponto2[1])

resultado = math.sqrt(primeiraParte + segundaParte)

print('{:.4f}'.format(resultado))
