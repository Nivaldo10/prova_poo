# Classe base Animal
class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def fazer_som(self):
        return "O animal faz um som."

    def mover(self):
        return "O animal se move."

    def alimentar(self):
        return f"O {self.nome} está se alimentando."


# Subclasse Mamifero que herda de Animal
class Mamifero(Animal):
    def __init__(self, nome, idade, tipo_de_pelo):
        super().__init__(nome, idade)
        self.tipo_de_pelo = tipo_de_pelo

    def fazer_som(self):
        return "O mamífero emite um som característico."

    def mover(self):
        return "O mamífero anda sobre quatro patas ou duas."


# Subclasse Ave que herda de Animal
class Ave(Animal):
    def __init__(self, nome, idade, cor_da_asas):
        super().__init__(nome, idade)
        self.cor_da_asas = cor_da_asas

    def fazer_som(self):
        return "A ave canta."

    def mover(self):
        return "A ave voa pelo céu."


# Subclasse Peixe que herda de Animal
class Peixe(Animal):
    def __init__(self, nome, idade, tipo_de_escama):
        super().__init__(nome, idade)
        self.tipo_de_escama = tipo_de_escama

    def fazer_som(self):
        return "Os peixes não fazem som, são silenciosos."

    def mover(self):
        return "O peixe nada nas águas."


# Função para exibir informações sobre o animal
def exibir_informacoes(animal):
    print(f"Nome: {animal.nome}")
    print(f"Idade: {animal.idade}")
    print(f"Som: {animal.fazer_som()}")
    print(f"Movimento: {animal.mover()}")
    print(f"Alimentação: {animal.alimentar()}")
    print("-" * 50)


# Programa principal para testar a implementação
def main():
    # Criando objetos de diferentes tipos de animais
    leao = Mamifero("Leão", 5, "denso")
    papagaio = Ave("Papagaio", 2, "verde")
    tubarao = Peixe("Tubarão", 8, "rugosa")

    # Exibindo informações dos animais
    exibir_informacoes(leao)
    exibir_informacoes(papagaio)
    exibir_informacoes(tubarao)


if __name__ == "__main__":
    main()
