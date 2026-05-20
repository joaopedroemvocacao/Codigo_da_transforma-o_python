# DESAFIO EXTRA - AGENDA DE CONTATOS

def desafio_extra_agenda():
    """Desafio Extra: Agenda de contatos"""
    
    print("\n" + "="*50)
    print("DESAFIO EXTRA: AGENDA DE CONTATOS")
    print("="*50)
    
    agenda = {}
    
    while True:
        print("\n--- Agenda ---")
        print("1. Adicionar contato")
        print("2. Remover contato")
        print("3. Buscar contato")
        print("4. Ver contatos")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            nome = input("Nome: ")
            telefone = input("Telefone: ")
            
            agenda[nome] = telefone
            print(f"✓ {nome} adicionado!")
        
        elif opcao == "2":
            nome = input("Nome para remover: ")
            
            if nome in agenda:
                del agenda[nome]
                print(f"✓ {nome} removido!")
            else:
                print("❌ Contato não encontrado!")
        
        elif opcao == "3":
            nome = input("Nome para buscar: ")
            
            if nome in agenda:
                print(f"📞 {nome}: {agenda[nome]}")
            else:
                print("❌ Contato não encontrado!")
        
        elif opcao == "4":
            if agenda:
                print("\n📒 CONTATOS:")
                
                for nome, telefone in agenda.items():
                    print(f"{nome}: {telefone}")
            else:
                print("📒 Agenda vazia!")
        
        elif opcao == "5":
            print("Saindo da agenda...")
            break
        
        else:
            print("❌ Opção inválida!")


desafio_extra_agenda()