# Criando uma exceção personalizada
class SaldoInsuficienteError(Exception):
    """Essa exceção acontece quando o saldo não é suficiente"""
    pass

# Classe da conta bancária
class ContaBancaria:
    def __init__(self, nome, saldo_inicial=0):
        self.nome = nome
        self.saldo = saldo_inicial
        print(f"Conta criada para {self.nome} com R$ {self.saldo:.2f}")
    
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"✅ Depósito de R$ {valor:.2f} realizado!")
            print(f"   Novo saldo: R$ {self.saldo:.2f}")
        else:
            print("❌ Valor de depósito inválido!")
    
    def sacar(self, valor):
        try:
            if valor <= 0:
                print("❌ Valor de saque inválido!")
                return
            
            if valor > self.saldo:
                # Levantando nossa exceção personalizada
                raise SaldoInsuficienteError(f"Saldo insuficiente! Você tem R$ {self.saldo:.2f} e quer sacar R$ {valor:.2f}")
            
            self.saldo -= valor
            print(f"✅ Saque de R$ {valor:.2f} realizado!")
            print(f"   Novo saldo: R$ {self.saldo:.2f}")
        
        except SaldoInsuficienteError as erro:
            print(f"\n❌ ERRO: {erro}")
    
    def ver_saldo(self):
        print(f"\n💰 Saldo atual de {self.nome}: R$ {self.saldo:.2f}")

# Programa principal
print("=" * 40)
print("     BANCO DO MENINO")
print("=" * 40)

# Criando uma conta
nome = input("Digite seu nome: ")
conta = ContaBancaria(nome, 100)  # Começa com R$ 100

while True:
    print("\n" + "=" * 40)
    print("O que você quer fazer?")
    print("1 - Ver saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Sair")
    
    try:
        opcao = int(input("\nOpção: "))
        
        if opcao == 1:
            conta.ver_saldo()
        
        elif opcao == 2:
            valor = float(input("Quanto depositar? R$ "))
            conta.depositar(valor)
        
        elif opcao == 3:
            valor = float(input("Quanto sacar? R$ "))
            conta.sacar(valor)
        
        elif opcao == 4:
            print("Obrigado por usar nosso banco!")
            break
        
        else:
            print("Opção inválida!")
    
    except ValueError:
        print("❌ Digite um número válido!")