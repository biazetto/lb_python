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
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor 
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou")

    elif opcao == "s":
        valor = float(input("Informe o valor do Saque: "))
        if numero_saques >= LIMITE_SAQUES:
            print("Operação atingiu o limite de saques")

        elif valor > saldo:
            print("Você não tem saldo suficiente")

        elif valor > 500:
            print("Você não pode fazer um saque maior que 500 reais")
        
        elif valor > 0:
            saldo -= valor 
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        
        else:
            print("Operação falhou")


    elif opcao == "e":
        print(f"Extrato {extrato}")
    
    elif opcao == "q":
        break

    else:
        print("Operaçao invalida, por favor digite novamente")