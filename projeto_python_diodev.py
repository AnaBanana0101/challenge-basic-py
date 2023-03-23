#Menu do usuário

menu = """

    [D] Depositar 
    [S] Sacar 
    [E] Extrato
    [Q] Sair

"""

#Parâmetros
saldo = 0
limite = 500
extrato = ""
numero_saques = 0 
LIMITE_SAQUES = 3 

#Looping das condicionais das opções para o cliente
while True:

    opcao = input(menu)

    if opcao == "d": #Condicional de depósito
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito R${valor:.2f}\n"
        else:
            print("Operação falhou. O Valor informado não é válido.")


    elif opcao == "s": #Condicional de saque
        valor = float(input("Informe o valor de saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo: 
            print("Operação falhou! Saldo insuficiente.")
        elif excedeu_limite: 
            print("Operação falhou! Limite excedido.")
        elif excedeu_saques:
            print("Operação falhou! Limite de saques diários atingido")
        elif valor > 0: 
            saldo -= valor
            extrato += f"Saque: R${valor:.2f}\n"
            numero_saques += 1 
        else: 
            print("Operação falhou! Valor informado inválido.")

    elif opcao == "e": #Condicional de extrato
        print("=" * 6, "EXTRATO", "=" * 6)
        print("Não foram realizados movimentações" if not extrato else extrato)
        print(f"Saldo: R${saldo:.2f}")
        print("=" * 20)

    elif opcao == "q": #Condicional de saída
        break

    else:
        print("Operação Inválida, por favor selecione uma operação válida.")

        


