# ATIVIDADE 1 - LISTA DE COMPRAS

def atividade1_lista_compras():
    """Atividade 1: Lista de compras"""
    print("\n" + "="*50)
    print("ATIVIDADE 1: LISTA DE COMPRAS")
    print("="*50)
    
    lista = []
    
    while True:
        print("\n--- Lista de Compras ---")
        print("1. Adicionar item")
        print("2. Remover item")
        print("3. Visualizar lista")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            item = input("Digite o item para adicionar: ")
            lista.append(item)
            print(f"✓ {item} adicionado!")
            
        elif opcao == "2":
            if lista:
                for i, item in enumerate(lista, 1):
                    print(f"{i}. {item}")
                
                try:
                    indice = int(input("Digite o número do item: "))
                    
                    if 1 <= indice <= len(lista):
                        removido = lista.pop(indice - 1)
                        print(f"✓ {removido} removido!")
                    else:
                        print("❌ Número inválido!")
                        
                except ValueError:
                    print("❌ Digite um número válido!")
            else:
                print("❌ Lista vazia!")
                
        elif opcao == "3":
            if lista:
                print("\n📝 LISTA DE COMPRAS:")
                
                for i, item in enumerate(lista, 1):
                    print(f"{i}. {item}")
            else:
                print("📝 Lista vazia!")
                
        elif opcao == "4":
            print("Saindo da atividade...")
            break
            
        else:
            print("❌ Opção inválida!")


atividade1_lista_compras()