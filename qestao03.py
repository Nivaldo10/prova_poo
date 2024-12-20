def main():
    numeros = []  # Lista que armazenará os números informados pelo usuário.

    while True:  # Laço principal que mantém o programa em execução até o usuário decidir sair.
        print("\nMenu:")
        print("1. Adicionar número")
        print("2. Remover número")
        print("3. Exibir números")
        print("4. Calcular média")
        print("5. Sair")

        escolha = input("Escolha uma opção (1-5): ")

        # Condicional para tratar cada escolha do menu.
        if escolha == "1":
            num = int(input("Digite o número para adicionar: "))
            numeros.append(num)  # Adiciona o número à lista.
            print(f"Número {num} adicionado!")

        elif escolha == "2":
            if numeros:  # Verifica se a lista não está vazia.
                num = int(input("Digite o número para remover: "))
                if num in numeros:  # Verifica se o número existe na lista.
                    numeros.remove(num)  # Remove o número da lista.
                    print(f"Número {num} removido!")
                else:
                    print("Número não encontrado na lista.")
            else:
                print("A lista está vazia, não há números para remover.")

        elif escolha == "3":
            if numeros:  # Verifica se a lista contém elementos.
                print("Números na lista:")
                for numero in numeros:  # Itera sobre os números na lista.
                    print(numero)
            else:
                print("A lista está vazia.")

        elif escolha == "4":
            if numeros:  # Certifica-se de que a lista não está vazia antes de calcular a média.
                media = sum(numeros) / len(numeros)  # Calcula a média.
                print(f"A média dos números é: {media:.2f}")
            else:
                print("A lista está vazia, não é possível calcular a média.")

        elif escolha == "5":
            print("Progama finalizado!")
            break  # Encerra o laço while e o programa.

        else:
            print("Opção inválida. Tente novamente.")
print(main())