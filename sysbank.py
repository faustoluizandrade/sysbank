## Sistem bancrio - desafio 01 do bootcamp de python da DIO

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite_diario = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    if opcao == 'd':
        valor = float(input("Informe o valor do deposito:"))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == 's':
        valor = float(input("Informe o valor do saque:"))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite_diario
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operacao falhou! Voce nao tem saldo suficiente")
        elif excedeu_limite:
            print("Operacao falhou! O valor do saque excede o limite diario.")
        elif excedeu_saques:
            print("Operacao falhou! Numero maximo de saques excedido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("Operacao falhou! O valor informado é invalido.")
    
    elif opcao == 'e':
        print("\n ***************INICIO EXTRATO***************")
        print("Nao foram realizadas movimentacoes." if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}")
        print("***************FIM EXTRATO***************")
    
    elif opcao == 'q':
        break

    else:
        print("Opcao inválida, favor selecionar novamente a opcao desejada.")
      
