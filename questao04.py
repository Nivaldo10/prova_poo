import random

# Função para gerar uma matriz quadrada de tamanho n com números aleatórios
def gerar_matriz(n):
    matriz = []
    for i in range(n):
        linha = [random.randint(1, 10) for _ in range(n)]  # Gerando números aleatórios de 1 a 10
        matriz.append(linha)
    return matriz


# Função para exibir uma matriz
def exibir_matriz(matriz):
    for linha in matriz:
        print(linha)


# Função para multiplicar duas matrizes quadradas
def multiplicar_matrizes(matriz_a, matriz_b):
    n = len(matriz_a)
    # Inicializando a matriz resultado com zeros
    resultado = [[0] * n for _ in range(n)]

    # Realizando a multiplicação de matrizes
    for i in range(n):
        for j in range(n):
            for k in range(n):
                resultado[i][j] += matriz_a[i][k] * matriz_b[k][j]

    return resultado


# Função principal para controlar o fluxo do programa
def main():
    # Recebe o tamanho da matriz do usuário
    n = int(input("Digite o tamanho das matrizes quadradas (n x n): "))

    # Gerando duas matrizes quadradas aleatórias
    matriz_a = gerar_matriz(n)
    matriz_b = gerar_matriz(n)

    # Exibindo as matrizes geradas
    print("\nMatriz A:")
    exibir_matriz(matriz_a)

    print("\nMatriz B:")
    exibir_matriz(matriz_b)

    # Multiplicando as matrizes
    resultado = multiplicar_matrizes(matriz_a, matriz_b)

    print("\nResultado da multiplicação A * B:")
    exibir_matriz(resultado)


# Chama a função principal
if __name__ == "__main__":
    main()
