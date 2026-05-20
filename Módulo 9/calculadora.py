# Calculadora simples com tratamento de erros

print("=" * 40)
print("      CALCULADORA SIMPLES")
print("=" * 40)

while True:
    print("\nOperações:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")
    
    try:
        opcao = int(input("\nEscolha uma opção: "))
        
        if opcao == 5:
            print("Até logo!")
            break
        
        if opcao < 1 or opcao > 5:
            print("Opção inválida! Escolha 1, 2, 3, 4 ou 5.")
            continue
        
        # Pedindo os números
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        
        # Fazendo a operação escolhida
        if opcao == 1:
            resultado = num1 + num2
            print(f"\n{num1} + {num2} = {resultado}")
        
        elif opcao == 2:
            resultado = num1 - num2
            print(f"\n{num1} - {num2} = {resultado}")
        
        elif opcao == 3:
            resultado = num1 * num2
            print(f"\n{num1} x {num2} = {resultado}")
        
        elif opcao == 4:
            # Tratando divisão por zero!
            try:
                resultado = num1 / num2
                print(f"\n{num1} ÷ {num2} = {resultado}")
            except ZeroDivisionError:
                print("\n❌ ERRO: Não é possível dividir por zero!")
    
    except ValueError:
        print("\n❌ ERRO: Digite apenas números!")
    
    except Exception as erro:
        print(f"\n❌ ERRO inesperado: {erro}")