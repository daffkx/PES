#Lista 4.5, Exercício 2

condutores = {
    "001": "Roberto Souza",
    "002": "João Graciano",
    "003": "Karine Silva",
    "004": "Pedro Luiz",
    "005": "Maria Catarina",
    "006": "Júlio Cardoso",
    "007": "Altivo Antônio",
    "008": "Jorge Gonçalves",
    "009": "Marcos Vinícius",
    "010": "Heleno Nunes",
    "011": "Mara Cristina",
    "012": "Otávio Rocha"
}

caminhoes = {
    "001": "Monobloco",
    "002": "Scania 112 HW",
    "003": "Volkswagen Express 4150",
    "004": "Volkswagen Express 6160",
    "005": "Volkswagen VW 17230 Worker",
    "006": "Volkswagen Express 9170",
    "007": "Iveco Daily 40s14",
    "008": "Iveco Tectro 310E28"
}

rotas = []

while True:
    print("\n=== EMPRESA ALPHA ENTREGAS ===")
    print("1 - Registrar saída")
    print("2 - Registrar retorno")
    print("3 - Consultar caminhão")
    print("4 - Listar caminhões")
    print("5 - Listar condutores")
    print("6 - Listar retornos por data")
    print("7 - Verificar entregas do dia")
    print("0 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        cod_cam = input("Código do caminhão: ")
        cod_con = input("Código do condutor: ")
        data_saida = input("Data da saída: ")
        hora_saida = input("Hora da saída: ")

        if cod_cam in caminhoes and cod_con in condutores:
            rota = {
                "caminhao": cod_cam,
                "condutor": cod_con,
                "data_saida": data_saida,
                "hora_saida": hora_saida,
                "data_retorno": "",
                "hora_retorno": ""
            }
            rotas.append(rota)
            print("Saída registrada!")
        else:
            print("Código inválido!")

    elif opcao == "2":
        cod_cam = input("Código do caminhão: ")

        encontrou = False

        for rota in rotas:
            if rota["caminhao"] == cod_cam and rota["data_retorno"] == "":
                rota["data_retorno"] = input("Data do retorno: ")
                rota["hora_retorno"] = input("Hora do retorno: ")
                encontrou = True
                print("Retorno registrado!")
                break

        if not encontrou:
            print("Caminhão não encontrado ou já retornou.")

    elif opcao == "3":
        cod_cam = input("Código do caminhão: ")
        encontrou = False

        for rota in rotas:
            if rota["caminhao"] == cod_cam:
                encontrou = True

        print("\nCaminhão:", caminhoes[cod_cam])
        print("Condutor:", condutores[rota["condutor"]])

        if rota["data_retorno"] == "":
            print("Status: NÃO RETORNOU")
        else:
            print("Status: RETORNOU")
            print("Data retorno:", rota["data_retorno"])
            print("Hora retorno:", rota["hora_retorno"])

    if not encontrou:
        print("Nenhum registro encontrado.")

    elif opcao == "4":
        print("\nLISTA DE CAMINHÕES")
        for codigo, nome in caminhoes.items():
            print(codigo, "-", nome)

    elif opcao == "5":
        print("\nLISTA DE CONDUTORES")
        for codigo, nome in condutores.items():
            print(codigo, "-", nome)

    elif opcao == "6":
        data = input("Informe a data: ")
        print("\nRETORNOS DA DATA", data)
        
        for rota in rotas:
            if rota["data_retorno"] == data:
                print(
                    rota["caminhao"],
                    "-",
                    caminhoes[rota["caminhao"]],
                    "-",
                    condutores[rota["condutor"]],
                    "-",
                    rota["hora_retorno"]
            )

    elif opcao == "7":
        todas = True

        for rota in rotas:
            if rota["data_retorno"] == "":
                todas = False

        if todas and len(rotas) > 0:
            print("Todas as entregas do dia foram realizadas.")
        else:
            print("Ainda existem caminhões em rota.")

    elif opcao == "0":
        print("Sistema encerrado.")
        break

    else:
        print("Opção inválida!")