import random

#FUNÇÕES BÁSICAS  
def fromCodeToMap(codigo):
    trechos = codigo.split(';')

    matriz = []
    for i in range(10):
        linha = []
        for j in range(10):
            linha.append(0)
        matriz.append(linha)

    for trecho in trechos:
        trecho_sem_espaco = trecho.strip()
        if trecho_sem_espaco:
            dados = trecho_sem_espaco.split()
            linha = int(dados[0])
            coluna = int(dados[1])
            custo = int(dados[2])
            matriz[linha][coluna] = custo

    return matriz


def printMap(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(matriz[i][j], end=" ")
        print()
    print()


def showWalkedPath(mapa, caminho):
    marcas = []
    for i in range(len(mapa)):
        linha = []
        for j in range(len(mapa[0])):
            linha.append('.')
        marcas.append(linha)

    x = len(mapa) - 1
    y = 0
    custo = mapa[x][y]
    marcas[x][y] = '*'
    passos = 0

    for mov in caminho:
        if mov == 0:
            y += 1
        else:
            x -= 1
        custo += mapa[x][y]
        marcas[x][y] = '*'
        passos += 1

        if passos % 5 == 0:
            printMap(marcas)


def calculaCusto(matriz, caminho):
    x = len(matriz) - 1
    y = 0
    custo = matriz[x][y]
    for mov in caminho:
        if mov == 0:
            y += 1
        else:
            x -= 1
        custo += matriz[x][y]
    return custo


# CAMINHADAS
def caminhadaFixa(matriz):
    print("=== Caminhada FIXA ===")
    caminho = []
    x = len(matriz) - 1
    y = 0
    while x > 0 or y < len(matriz[0]) - 1:
        if y < len(matriz[0]) - 1:
            caminho.append(0)
            y += 1
        if x > 0:
            caminho.append(1)
            x -= 1
    showWalkedPath(matriz, caminho)   #chamo a função de mostra a matriz
    print("Sequência:", end=" ")
    for n in caminho:
        print(n, end="")
    print()
    print("Custo Total:", calculaCusto(matriz, caminho))
    print()


def caminhadaAleatoria(matriz):
    print("=== Caminhadas ALEATÓRIAS ===")
    for k in range(10):
        caminho = []
        x = len(matriz) - 1
        y = 0
        while x > 0 or y < len(matriz[0]) - 1:
            if x == 0:
                mov = 0
            elif y == len(matriz[0]) - 1:
                mov = 1
            else:
                mov = random.randint(0, 1)
            caminho.append(mov)
            if mov == 0:
                y += 1
            else:
                x -= 1
        custo = calculaCusto(matriz, caminho)
        print("Caminhada", k + 1, ":", end=" ")
        for n in caminho:
            print(n, end="")
        print()
        print("Custo Total da Caminhada", k + 1, ":", custo)
    print()


def caminhadaGulosa(matriz):
    print("=== Caminhada GULOSA ===")
    caminho = []
    x = len(matriz) - 1     
    y = 0                  
    passos = 0

    while x > 0 or y < len(matriz[0]) - 1:
        if y < len(matriz[0]) - 1:
            custo_direita = matriz[x][y + 1]
        else:
            custo_direita = None   

        if x > 0:
            custo_cima = matriz[x - 1][y]
        else:
            custo_cima = None      

        if custo_direita is not None and custo_cima is not None:
            if custo_direita <= custo_cima:
                caminho.append(0)
                y += 1
            else:
                caminho.append(1)
                x -= 1
        elif custo_direita is not None:
            caminho.append(0)
            y += 1
        else:
            caminho.append(1)
            x -= 1

        passos += 1
        if passos % 5 == 0:
            showWalkedPath(matriz, caminho)

    print("Sequência:", end=" ")
    for n in caminho:
        print(n, end="")
    print()
    print("Custo Total:", calculaCusto(matriz, caminho))
    print()


# MAIN
def main():
    ilhas = [
        ("Ilha 1", "0 0 3; 0 1 25; 0 2 3; 0 3 8; 0 4 8; 0 5 1; 0 6 25; 0 7 1; 0 8 3; 0 9 8; 1 0 1; 1 1 3; 1 2 8; 1 3 3; 1 4 8; 1 5 1; 1 6 25; 1 7 3; 1 8 8; 1 9 1; 2 0 25; 2 1 1; 2 2 8; 2 3 1; 2 4 1; 2 5 1; 2 6 1; 2 7 25; 2 8 3; 2 9 1; 3 0 8; 3 1 25; 3 2 25; 3 3 25; 3 4 1; 3 5 3; 3 6 8; 3 7 8; 3 8 3; 3 9 25; 4 0 1; 4 1 1; 4 2 1; 4 3 25; 4 4 25; 4 5 3; 4 6 3; 4 7 25; 4 8 25; 4 9 8; 5 0 1; 5 1 25; 5 2 25; 5 3 1; 5 4 8; 5 5 8; 5 6 1; 5 7 3; 5 8 1; 5 9 8; 6 0 3; 6 1 8; 6 2 8; 6 3 3; 6 4 8; 6 5 3; 6 6 3; 6 7 3; 6 8 25; 6 9 8; 7 0 3; 7 1 25; 7 2 25; 7 3 3; 7 4 8; 7 5 1; 7 6 1; 7 7 8; 7 8 25; 7 9 3; 8 0 8; 8 1 1; 8 2 25; 8 3 3; 8 4 8; 8 5 8; 8 6 3; 8 7 3; 8 8 1; 8 9 25; 9 0 1; 9 1 25; 9 2 1; 9 3 1; 9 4 8; 9 5 25; 9 6 8; 9 7 3; 9 8 25; 9 9 1;"),
        ("Ilha 2", "0 0 8; 0 1 8; 0 2 3; 0 3 3; 0 4 25; 0 5 8; 0 6 25; 0 7 3; 0 8 8; 0 9 25; 1 0 1; 1 1 25; 1 2 8; 1 3 1; 1 4 8; 1 5 8; 1 6 8; 1 7 1; 1 8 8; 1 9 3; 2 0 1; 2 1 3; 2 2 3; 2 3 25; 2 4 8; 2 5 8; 2 6 1; 2 7 1; 2 8 8; 2 9 8; 3 0 25; 3 1 1; 3 2 3; 3 3 1; 3 4 8; 3 5 8; 3 6 25; 3 7 25; 3 8 25; 3 9 1; 4 0 25; 4 1 3; 4 2 3; 4 3 3; 4 4 3; 4 5 8; 4 6 8; 4 7 3; 4 8 25; 4 9 1; 5 0 8; 5 1 25; 5 2 1; 5 3 8; 5 4 3; 5 5 8; 5 6 8; 5 7 3; 5 8 3; 5 9 25; 6 0 25; 6 1 25; 6 2 3; 6 3 8; 6 4 1; 6 5 3; 6 6 25; 6 7 1; 6 8 25; 6 9 1; 7 0 1; 7 1 1; 7 2 1; 7 3 3; 7 4 8; 7 5 3; 7 6 1; 7 7 8; 7 8 25; 7 9 25; 8 0 3; 8 1 1; 8 2 3; 8 3 25; 8 4 3; 8 5 25; 8 6 8; 8 7 1; 8 8 8; 8 9 8; 9 0 8; 9 1 3; 9 2 8; 9 3 3; 9 4 25; 9 5 8; 9 6 1; 9 7 8; 9 8 3; 9 9 1;"),
        ("Ilha 3", "0 0 25; 0 1 1; 0 2 8; 0 3 25; 0 4 1; 0 5 25; 0 6 3; 0 7 3; 0 8 25; 0 9 25; 1 0 3; 1 1 25; 1 2 1; 1 3 3; 1 4 25; 1 5 25; 1 6 1; 1 7 1; 1 8 1; 1 9 25; 2 0 1; 2 1 8; 2 2 8; 2 3 8; 2 4 8; 2 5 25; 2 6 3; 2 7 25; 2 8 8; 2 9 3; 3 0 8; 3 1 8; 3 2 8; 3 3 1; 3 4 8; 3 5 8; 3 6 3; 3 7 3; 3 8 8; 3 9 3; 4 0 1; 4 1 8; 4 2 8; 4 3 1; 4 4 1; 4 5 3; 4 6 1; 4 7 8; 4 8 1; 4 9 1; 5 0 25; 5 1 8; 5 2 1; 5 3 8; 5 4 1; 5 5 1; 5 6 3; 5 7 25; 5 8 1; 5 9 25; 6 0 3; 6 1 8; 6 2 3; 6 3 1; 6 4 8; 6 5 1; 6 6 8; 6 7 3; 6 8 8; 6 9 8; 7 0 3; 7 1 3; 7 2 1; 7 3 8; 7 4 1; 7 5 3; 7 6 1; 7 7 3; 7 8 1; 7 9 25; 8 0 1; 8 1 3; 8 2 1; 8 3 8; 8 4 3; 8 5 3; 8 6 8; 8 7 1; 8 8 1; 8 9 25; 9 0 1; 9 1 1; 9 2 8; 9 3 8; 9 4 8; 9 5 1; 9 6 8; 9 7 8; 9 8 1; 9 9 8;")
    ]

    for nome, codigo in ilhas:
        print("#########################", nome, "#########################")
        ilha = fromCodeToMap(codigo)
        printMap(ilha)
        caminhadaFixa(ilha)
        caminhadaAleatoria(ilha)
        caminhadaGulosa(ilha)

main()
