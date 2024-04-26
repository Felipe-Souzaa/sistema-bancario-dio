menu = """
--------------
[0] Depositar
[1] Sacar
[2] Extrato
[3] Sair
--------------
"""

saldo = 0
limite = 500
extrato=[]
numero_saques = 1
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "0":
        print(40*"-")
        dep = float(input("Deposite o valor: R$ ")) 

        if dep >= 0:
            saldo += dep
            deposito = f"Deposito - R$ {dep:.2f}"
            extrato.append(deposito)
        else:
            print("Seu valor está incorreto, digite novamente!")

    elif opcao == "1":
        print(40*"-")
        if numero_saques <= LIMITE_SAQUES:
            saq = float(input("Digite quanto quer sacar: R$ "))
            
            if saq <= limite and saq >=0:

                if saldo >= saq:
                    saldo = saldo - saq
                    saque = f"Saque - R$ {saq:.2f}"
                    extrato.append(saque)
                    numero_saques += 1
                else:
                    print("Saldo insuficiente")
            else:
                print(f"Valor tem que ser positivo e o limite de saque é de R$ {limite}")
        else:
            print("Você já atingiu o limite de saques diários, volte amanhã <3")

    elif opcao == "2":
        print(40*"-")
        if not extrato:
            print("Não foram realizadas movimentações")
            
        else:
            for index, valor in enumerate(extrato):
                print(f"{index+1}º - {valor}")
            print(40*"-")
            print(f"Saldo atual R$ {saldo:.2f}")
    elif opcao == "3":
        print("Sair")
        break

    else:
        print("Houve um erro, responda novamente...")
