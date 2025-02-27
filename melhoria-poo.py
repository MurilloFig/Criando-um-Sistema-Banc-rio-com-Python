import json

class ContaBancaria:
    def __init__(self, titular, saldo=0, limite_saque=500, saques_diarios=3):
        self.titular = titular
        self.saldo = saldo
        self.limite_saque = limite_saque
        self.saques_restantes = saques_diarios
        self.extrato = []

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: R$ {valor:.2f}")
            print(f"✅ Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("❌ Erro: O valor do depósito deve ser positivo.")

    def sacar(self, valor):
        if self.saques_restantes == 0:
            print("❌ Erro: Você já realizou o limite diário de saques.")
        elif valor > self.saldo:
            print("❌ Erro: Saldo insuficiente.")
        elif valor > self.limite_saque:
            print(f"❌ Erro: O limite de saque é de R$ {self.limite_saque:.2f} por operação.")
        elif valor > 0:
            self.saldo -= valor
            self.saques_restantes -= 1
            self.extrato.append(f"Saque: R$ {valor:.2f}")
            print(f"✅ Saque de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("❌ Erro: O valor do saque deve ser positivo.")

    def exibir_extrato(self):
        print("\n=== Extrato ===")
        if not self.extrato:
            print("Nenhuma movimentação registrada.")
        else:
            for operacao in self.extrato:
                print(operacao)
        print(f"💰 Saldo atual: R$ {self.saldo:.2f}")
        print("================\n")

    def salvar_dados(self):
        """Salva os dados da conta em um arquivo JSON."""
        dados = {
            "titular": self.titular,
            "saldo": self.saldo,
            "limite_saque": self.limite_saque,
            "saques_restantes": self.saques_restantes,
            "extrato": self.extrato
        }
        with open(f"{self.titular}_conta.json", "w") as file:
            json.dump(dados, file, indent=4)

    @classmethod
    def carregar_dados(cls, titular):
        """Carrega os dados da conta de um arquivo JSON."""
        try:
            with open(f"{titular}_conta.json", "r") as file:
                dados = json.load(file)
                return cls(dados["titular"], dados["saldo"], dados["limite_saque"], dados["saques_restantes"])
        except FileNotFoundError:
            print(f"📂 Nenhum dado encontrado para {titular}. Criando nova conta.")
            return cls(titular)

# Função principal do menu
def menu_banco():
    nome = input("Digite seu nome para acessar a conta: ")
    conta = ContaBancaria.carregar_dados(nome)

    while True:
        print("\n### 💰 Banco DIO ###")
        print("[1] Depositar")
        print("[2] Sacar")
        print("[3] Extrato")
        print("[4] Salvar e Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            try:
                valor = float(input("Digite o valor do depósito: R$ "))
                conta.depositar(valor)
            except ValueError:
                print("❌ Entrada inválida. Digite um valor numérico.")
        
        elif opcao == "2":
            try:
                valor = float(input("Digite o valor do saque: R$ "))
                conta.sacar(valor)
            except ValueError:
                print("❌ Entrada inválida. Digite um valor numérico.")

        elif opcao == "3":
            conta.exibir_extrato()
        
        elif opcao == "4":
            conta.salvar_dados()
            print("💾 Dados salvos. Obrigado por utilizar nosso sistema bancário. Até logo!")
            break
        
        else:
            print("❌ Opção inválida. Tente novamente.")

# Iniciar o sistema bancário
menu_banco()
