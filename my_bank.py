menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        depositoString = input("Digite o valor do seu depósito: R$ ")
        depositoFloat = float(depositoString)
        saldo += depositoFloat
        extrato += f"depósito: R$ {depositoFloat:2f}\n"
        print(depositoFloat)

    elif opcao == "s":
        saqueString = input("Digite o valor do seu saque: R$ ")
        saqueFloat = float(saqueString)
        saldo -= saqueFloat
        extrato += f"saque: R$ -{saqueFloat:2f}\n"
        print("saque")

    elif opcao == "e":
        print(extrato)

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")