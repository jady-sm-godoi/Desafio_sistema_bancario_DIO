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
msn = ""
asterisc = 100 - len(msn)

while True:

    opcao = input(menu)

    if opcao in "dD":
        depositoString = input("Digite o valor do seu depósito: R$ ")
        depositoFloat = float(depositoString)
        if(depositoFloat > 0):
            saldo += depositoFloat
            extrato += f"depósito: R$ {depositoFloat:.2f}\n"
            print(depositoFloat)
        else:
            msn = "ERROR: Apenas valores positivos"
            print(msn.center(asterisc, "*"))

    elif opcao in "sS":
        if(numero_saques > 2):
            msn = "Número máximo de saque diário exedido."
            print(msn.center(asterisc, "*"))
        else:
            saqueString = input("Digite o valor do seu saque: R$ ")
            saqueFloat = float(saqueString)
        if(saqueFloat > 500):
            msn = "Valor máximo para saque diário é de R$500.00"
            print(msn.center(asterisc, "*"))
        elif(saqueFloat > saldo):
            msn = "saldo insuficiente!"
            print(msn.center(asterisc, "*"))
        else:
            saldo -= saqueFloat
            extrato += f"saque:    R$ -{saqueFloat:.2f}\n"
            numero_saques += 1         

    elif opcao in "eE":
        if(extrato == ""):
            msn = "Não foram realizadas movimentações"
            print(msn.center(asterisc, "*"))
        else:
            print(
f"""
EXTRATO BANCÁRIO
*******************
{extrato}
-------------------
SALDO:    R$ {saldo:.2f}
"""
            )

    elif opcao in "qQ":
        break

    else:
        print("Operação inválida! Selecione novamente a operação desejada.".center(90, "*"))