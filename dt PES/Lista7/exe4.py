#Lista 7, Exercício 4

class ContratoDeTrabalho:
    def __init__(self, salario_bruto, percentual_impostos):
        self.salario_bruto = salario_bruto
        self.percentual_impostos = percentual_impostos

    def valor_impostos(self):
        return self.salario_bruto * self.percentual_impostos


class Funcionario:
    def __init__(self, nome, cargo, salario_bruto, percentual_impostos):
        self.nome = nome
        self.cargo = cargo
        self.contrato = ContratoDeTrabalho(
            salario_bruto, percentual_impostos
        )

    def salario_liquido(self):
        return self.contrato.salario_bruto - self.contrato.valor_impostos()

    def mostrar_dados(self):
        print("\n=== DADOS DO FUNCIONÁRIO ===")
        print("Nome:", self.nome)
        print("Cargo:", self.cargo)
        print("Salário Bruto: R$", self.contrato.salario_bruto)
        print("Impostos: R$", self.contrato.valor_impostos())
        print("Salário Líquido: R$", self.salario_liquido())

nome = input("Nome do funcionário: ")
cargo = input("Cargo: ")
salario = float(input("Salário bruto: R$ "))
imposto = float(input("Percentual de impostos (ex: 0.11): "))

funcionario = Funcionario(nome, cargo, salario, imposto)

while True:
    print("\n===== MENU =====")
    print("1 - Mostrar dados do funcionário")
    print("2 - Mostrar valor dos impostos")
    print("3 - Mostrar salário líquido")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        funcionario.mostrar_dados()

    elif opcao == "2":
        print("Valor dos impostos: R$",
              funcionario.contrato.valor_impostos())

    elif opcao == "3":
        print("Salário líquido: R$",
              funcionario.salario_liquido())

    elif opcao == "0":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida!")