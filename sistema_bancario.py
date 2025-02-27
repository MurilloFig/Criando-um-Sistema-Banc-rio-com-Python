# Sistema Bancário - Desafio DIO

saldo = 0
limite_saque = 500
saques_restantes = 3
extrato = []

def depositar(valor):
    global saldo
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}")
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Erro: O valor do depósito deve ser positivo.")

def sacar(valor):
    global saldo, saques_restantes
    if saques_restantes == 0:
        print("Erro: Você já realizou 3 saques hoje.")
    elif valor > saldo:
        print("Erro: Saldo insuficiente.")
    elif valor > limite_saque:
        print(f"Erro: O limite de saque é de R$ {limite_saque:.2f} por operação.")
    elif valor > 0:
        saldo -= valor
        saques_restantes -= 1
        extrato.append(f"Saque: R$ {valor:.2f}")
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Erro: O valor do saque deve ser positivo.")

def exibir_extrato():
    print("\n=== Extrato ===")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        for operacao in extrato:
            print(operacao)
    print(f"Saldo atual: R$ {saldo:.2f}")
    print("================\n")

while True:
    print("\n### Bem-vindo ao Banco DIO ###")
    print("[1] Depositar")
    print("[2] Sacar")
    print("[3] Extrato")
    print("[4] Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        valor = float(input("Digite o valor do depósito: R$ "))
        depositar(valor)
    elif opcao == "2":
        valor = float(input("Digite o valor do saque: R$ "))
        sacar(valor)
    elif opcao == "3":
        exibir_extrato()
    elif opcao == "4":
        print("Obrigado por utilizar nosso sistema bancário. Até logo!")
        break
    else:
        print("Opção inválida. Tente novamente.")
