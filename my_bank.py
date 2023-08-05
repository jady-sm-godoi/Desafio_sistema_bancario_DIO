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
        valueString = input("Digite o valor do seu depósito: R$ ")
        valueFloat = float(valueString)
        saldo += valueFloat
        extrato += f"depósito: R$ {valueFloat}"
        print(valueFloat)

    elif opcao == "s":
        print("saque")

    elif opcao == "e":
        print(extrato)

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")