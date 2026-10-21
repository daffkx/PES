#Lista 7, Exercício 3

class Carro:
    def __init__(self, placa, modelo):
        self.placa = placa
        self.modelo = modelo

class Vaga_do_estacionameto:
    def __init__(self, numero_vaga):
        self.numero_vaga = numero_vaga
        self.carro_estacionado = None

    def estacionar_carro(self, carro):
        if self.carro_estacionado is None:
            self.carro_estacionado = carro
        else:
            print("A vaga já está ocupada.")

    def liberar_vaga(self):
        if self.carro_estacionado is not None:
            self.carro_estacionado = None
        else:
            print("A vaga está livre.")

vaga = Vaga_do_estacionameto("A-101")

while True:
    print("\nMenu:")
    print("1. Estacionar carro")
    print("2. Liberar vaga")
    print("3. Verificar vaga")
    print("4. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        placa = input("Digite a placa do carro: ")
        modelo = input("Digite o modelo do carro: ")

        carro = Carro(placa, modelo)

        if vaga.estacionar_carro(carro):
            print("Vaga ocupada com sucesso!")
        else:
            print("A vaga já está ocupada!")

    elif opcao == "2":
        vaga.liberar_vaga()
        print("Vaga liberada!")

    elif opcao == "3":
        print("Vaga:", vaga.id_vaga)

        if vaga.carro_estacionado is None:
            print("Vaga livre.")
        else:
            print("Placa:", vaga.carro_estacionado.placa)
            print("Modelo:", vaga.carro_estacionado.modelo)

    elif opcao == "4":
        print("Programa encerrado!")
        break

    else:
        print("Opção inválida!")