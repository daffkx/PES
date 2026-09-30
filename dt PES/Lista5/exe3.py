#Lista 5, Exercício 3

def volume(cilindro):
    pi = 3.14159
    return pi * (cilindro["raio"] ** 2) * cilindro["altura"]

cilindro = {}  

cilindro["raio"] = float(input("Digite o raio do cilindro (em metros): "))
cilindro["altura"] = float(input("Digite a altura do cilindro (em metros): "))

resultado = volume(cilindro)
print(f"O volume do cilindro é: {resultado:.2f} metros cúbicos")