from datetime import datetime

def valida_opcao(lista, frase):
    opcao = input(frase)
    while opcao not in lista:
        print("Digite uma opção válida.")
        opcao = input(frase)
    return opcao


def valida_opcao_numerica(frase):
    escolha = input(frase)
    while not escolha.isnumeric():
        escolha = input(frase)

    return int(escolha)


def calcula_validade(dia_validade, mes_validade, ano_validade):
    data_atual = datetime.now()
    dia_atual = data_atual.day
    mes_atual = data_atual.month
    ano_atual = data_atual.year

    data_atual_dias = dia_atual + (mes_atual * 30) + (ano_atual * 365)
    data_validade_dias = dia_validade + (mes_validade * 30) + (ano_validade * 365)

    validade = data_validade_dias - data_atual_dias

    return validade


def printar_lista(alimentos, validade):
    for i in range(len(alimentos)):
        print(f"{i + 1}: {alimentos[i]} ({validade[i]} dias para validade)")
    return


def fazer_pedido(alimentos, validade):
    printar_lista(alimentos, validade)
    solicitacao = valida_opcao(alimentos, "Qual alimento você quer solicitar? ")
    return solicitacao


alimentos = ["manteiga", "leite", "queijo", "arroz", "feijão"]
validades = [
    calcula_validade(6, 10, 2023),
    calcula_validade(22, 9, 2023),
    calcula_validade(15, 8, 2023),
    calcula_validade(1, 9, 2023),
    calcula_validade(13, 12, 2023)
]

lista_de_pedidos = []
validade_lista_pedidos = []

print("Bem vindo ao Share a Bite!")
while True:

    persona = valida_opcao(["1", "2", "3"], ''' 
[1] Fornecedor de alimentos
[2] Organização de caridade
[3] Encerrar sessão

Digite o número com base no que você é ou encerre sua sessão: ''')

    if persona == "1":
        cadastro = valida_opcao(["S", "N"], "Você deseja cadastrar um alimento na nossa plataforma? (S/N) ")

        while cadastro == "S":
            alimento = input("Digite o nome do alimento: ")
            dia = valida_opcao_numerica("Digite o dia de vencimento do alimento (DD): ")
            while dia > 31:
                print("Dia inválido.")
                dia = valida_opcao_numerica("Digite o dia de vencimento do alimento (DD): ")
            mes = valida_opcao_numerica("Digite o mês de vencimento do alimento (MM): ")
            while mes > 12:
                print("Mês inválido.")
                mes = valida_opcao_numerica("Digite o mês de vencimento do alimento (MM): ")
            ano = valida_opcao_numerica("Digite o ano de vencimento do alimento (AAAA): ")

            validade = calcula_validade(dia, mes, ano)

            if validade < 0:
                print("Esse produto já está vencido e não pode ser compartilhado na nossa plataforma.")

            else:
                if validade >= 0 and validade < 30:
                    print("A data de vencimento desse produto está próxima, então daremos prioridade para que ele seja trocado o quanto antes.")
                alimentos.append(alimento)
                validades.append(validade)

            cadastro = valida_opcao(["S", "N"], "Deseja cadastrar mais um alimento? (S/N) ")

    elif persona == "2":
        solicitar = valida_opcao(["S", "N"], "Você deseja solicitar um alimento? (S/N) ")

        while solicitar == "S":

            if len(alimentos) == 0:
                print("Sentimos muito, mas não temos mais alimentos disponíveis. ")
                break

            pedido = fazer_pedido(alimentos, validades)
            for i in range(len(alimentos)):
                if pedido == alimentos[i]:
                    lista_de_pedidos.append(alimentos[i])
                    validade_lista_pedidos.append(validades[i])
            alimentos.remove(pedido)
            solicitar = valida_opcao(["S", "N"], "Quer solicitar outro alimento? (S/N) ")

    else:
        print("Obrigada por utilizar o Share a Bite!")
        if lista_de_pedidos != []:
            print("Os seus pedidos foram:")
            printar_lista(lista_de_pedidos, validade_lista_pedidos)
        break
