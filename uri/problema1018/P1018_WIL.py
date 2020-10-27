entrada = input()

notas = [100, 50, 20, 10, 5, 2, 1]
qtdNotas = [0, 0, 0, 0, 0, 0, 0]


def fazTroco(valor, posicao):
    valorInteiro = int(valor / notas[posicao])
    qtdNotas[posicao] = valorInteiro
    sub = valorInteiro * notas[posicao]
    valor = valor - int(sub)
    return valor


valor = int(entrada)
for i in range(7):
    valor = fazTroco(valor, i)


def imprime():
    resultado = entrada + '\n'
    for i in range(7):
        resultado += str(qtdNotas[i]) + \
            ' nota(s) de R$ ' + str(notas[i]) + ',00\n'
    print(resultado)


imprime()
