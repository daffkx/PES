ano = int(input("Digite o ano: "))

if (ano % 4 == 0 or ano % 400 == 0) and ano % 100 != 0:
	print (f"O ano {ano} é bissexto!")
else:
	print(f"O ano {ano} não é bissexto!") 

# ===========================================

# ano = int(input("Digite o ano: "))

# if (ano % 400 == 0 or ano % 4 == 0) and ano % 100 != 0:
# 	print(f"O ano {ano} é bissexto")
# else:
# 	print(f"O ano {ano} não é bissexto")

# class Carro:
# 	velocidade = 2000
# 	marcha = "manual"

# 	def acelerar():
# 		print("Vrum Vrum")
# 		print("Vrum Vrum")
# 		print("Vrum Vrum")

# print ("Início")

# carro_tyler = Carro()
# carro_tyler.marcha = "auto"

# if (carro_tyler.marcha == "Manual"):
# 	print("Esse carro é manual")
# else:
# 	print("Esse carro é automático")

# class Pessoa:
# 	nome = ""
# 	cpf = "" 
# 	idade = 0

# 	def ano_que_nasceu(self):
# 		ano = 2026 - self.idade

# tyler = Pessoa()
# tyler.nome = "Tyler Joseph"
# tyler.cpf = "123.45\6.789-10"
# tyler.idade = 38

# class Aluno:
# 	def __init__(self, nome, idade):
# 		self.nome = nome
# 		self.idade = idade

# 	def apresentar(self):
# 		print("Sou o(a)", self.nome, "e tenho", self.idade)		

# Luis = Aluno("Luis Shalata", 16)
# Vitoria = Aluno("Vitoria Garcia", 17)
# Vitor = Aluno("Vitor Roberto", 16)

# alunos = [Luis, Vitoria, Vitor]

# for aluno in alunos:
# 	print("Aluno:", aluno.nome, "Idade:", aluno.idade)

# Luis.apresentar()