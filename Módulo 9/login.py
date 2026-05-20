# Sistema de login com múltiplas tentativas

import time

# Dados do usuário (simulando um banco de dados)
USUARIOS = {
    "joaozinho": "123456",
    "mariazinha": "abc123",
    "pedrinho": "senha123"
}

def fazer_login(tentativas_maximas=3):
    """
    Função que tenta fazer login com 3 tentativas
    """
    tentativas = 0
    
    print("=" * 40)
    print("       SISTEMA DE LOGIN")
    print("=" * 40)
    
    while tentativas < tentativas_maximas:
        print(f"\n🔐 Tentativa {tentativas + 1} de {tentativas_maximas}")
        
        usuario = input("Usuário: ")
        senha = input("Senha: ")
        
        try:
            # Verificando se o usuário existe
            if usuario not in USUARIOS:
                raise KeyError("Usuário não encontrado!")
            
            # Verificando se a senha está correta
            if USUARIOS[usuario] != senha:
                raise ValueError("Senha incorreta!")
            
            # Se chegou aqui, login foi bem sucedido!
            print("\n✅ Login realizado com sucesso!")
            print(f"👋 Bem-vindo, {usuario}!")
            return True
        
        except KeyError as erro:
            print(f"❌ ERRO: {erro}")
            tentativas += 1
        
        except ValueError as erro:
            print(f"❌ ERRO: {erro}")
            tentativas += 1
        
        if tentativas < tentativas_maximas:
            print(f"Restam {tentativas_maximas - tentativas} tentativas...")
            time.sleep(1)  # Pequena pausa para não parecer robô
    
    print("\n" + "=" * 40)
    print("🔒 NÚMERO MÁXIMO DE TENTATIVAS ATINGIDO!")
    print("🔒 ACESSO BLOQUEADO!")
    print("=" * 40)
    return False

def menu_principal():
    """
    Menu principal após o login
    """
    print("\n" + "=" * 40)
    print("        PAINEL PRINCIPAL")
    print("=" * 40)
    print("1 - Ver perfil")
    print("2 - Sair")
    
    opcao = input("\nEscolha: ")
    
    if opcao == "1":
        print("\n📱 Perfil do usuário logado")
        print("   ...carregando informações...")
    else:
        print("Saindo do sistema...")

# Programa principal
if __name__ == "__main__":
    if fazer_login():
        menu_principal()
    else:
        print("\nPor favor, contate o administrador para desbloquear sua conta.")