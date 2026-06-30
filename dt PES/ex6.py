#Lista 1, Exercício 6
player1=(input("Jogador 1, escolha pedra, papel ou tesoura: "))
player2=(input("Jogador 2, escolha pedra, papel ou tesoura: "))
if player1==player2:
    print("Empate!")
elif (player1=="pedra" and player2=="tesoura") or (player1=="papel" and player2=="pedra") or (player1=="tesoura" and player2=="papel"):
    print("Jogador 1 venceu!")
else:
    print("Jogador 2 venceu!")