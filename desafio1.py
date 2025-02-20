menu = """
#########################################
        Bem vindo ao serviço de 
        autoatendimento do Banco

Favor selecionar a operação que deseja:
        
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

#########################################
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True: # loop infinito
    
    opção = input(menu)

    if opção == "d":
        valor = float(input("Informe o valor do depósito:"))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}    Saldo: R$ {saldo:.2f} \n"

        else:
            print("Falha na operação! Valor informado não é válido.")


    elif opção == "s":
        valor = float(input("Informe o valor do saque:"))

        excedeu_saldo = (valor > saldo)

        excedeu_limite = (valor > limite)

        excedeu_saques = (numero_saques >= LIMITE_SAQUES)

        if excedeu_saldo:
            print("Falha na operação! Saldo insuficiente.")

        elif excedeu_limite:
            print("Falha na operação! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Falha na operação! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}    Saldo: R$ {saldo:.2f}\n"
            numero_saques += 1

        else:
            print("Falha na operação! Valor informado não é válido.")

    
    elif opção == "e":
        print("\n################ EXTRATO ################\n")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo Atual: R$ {saldo:.2f}")
        print("\n#########################################")

    elif opção =="q":
        print("Obrigado por utilizar nossos serviços!")
        break

    else:
        print("Operação inválida.  Por favor selecione novamente a operação desejada.")
