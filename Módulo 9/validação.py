# Programa que valida as entradas do usuário

def validar_idade():
    while True:
        try:
            idade = int(input("Digite sua idade: "))
            
            if idade < 0:
                print("❌ Idade não pode ser negativa! Tente novamente.")
            elif idade > 150:
                print("❌ Idade muito alta! Digite uma idade realista.")
            else:
                print(f"✅ Idade válida! Você tem {idade} anos.")
                return idade
        
        except ValueError:
            print("❌ Por favor, digite um número inteiro!")

def validar_email():
    while True:
        email = input("Digite seu e-mail: ")
        
        if '@' not in email:
            print("❌ E-mail precisa ter @!")
        elif '.' not in email:
            print("❌ E-mail precisa ter ponto (.)!")
        elif len(email) < 5:
            print("❌ E-mail muito curto!")
        else:
            print(f"✅ E-mail válido: {email}")
            return email

def validar_telefone():
    while True:
        telefone = input("Digite seu telefone (apenas números): ")
        
        if not telefone.isdigit():
            print("❌ Digite apenas números!")
        elif len(telefone) < 8 or len(telefone) > 11:
            print("❌ Telefone deve ter entre 8 e 11 dígitos!")
        else:
            print(f"✅ Telefone válido: {telefone}")
            return telefone

def validar_nota():
    while True:
        try:
            nota = float(input("Digite uma nota (0 a 10): "))
            
            if nota < 0:
                print("❌ Nota não pode ser negativa!")
            elif nota > 10:
                print("❌ Nota não pode ser maior que 10!")
            else:
                print(f"✅ Nota válida: {nota}")
                return nota
        
        except ValueError:
            print("❌ Digite um número válido!")

# Programa principal
print("=" * 40)
print("    CADASTRO COM VALIDAÇÃO")
print("=" * 40)

print("\nVamos cadastrar seus dados:")
print("-" * 40)

idade = validar_idade()
email = validar_email()
telefone = validar_telefone()
nota = validar_nota()

print("\n" + "=" * 40)
print("       DADOS CADASTRADOS")
print("=" * 40)
print(f"Idade: {idade} anos")
print(f"E-mail: {email}")
print(f"Telefone: {telefone}")
print(f"Nota: {nota}")
print("\n Cadastro realizado com sucesso!")