import random
import math

def jogo_adivinhacao():
    print("=== JOGO DE ADIVINHAÇÃO ===")
    print("Tente adivinhar o número entre 1 e 100!")
    
    # Gerar número aleatório
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    max_tentativas = 10
    
    # Calcular log2 do intervalo para dica de tentativas
    tentativas_ideais = math.ceil(math.log2(100))
    
    print(f"\n💡 Dica: O número ideal de tentativas seria {tentativas_ideais}")
    print(f"Você tem {max_tentativas} tentativas!\n")
    
    while tentativas < max_tentativas:
        try:
            palpite = int(input(f"Tentativa {tentativas + 1}/{max_tentativas}: "))
            
            if palpite < 1 or palpite > 100:
                print("⚠️ Por favor, digite um número entre 1 e 100!")
                continue
            
            tentativas += 1
            
            if palpite == numero_secreto:
                print(f"\n🎉 PARABÉNS! Você acertou em {tentativas} tentativas!")
                print(f"🌟 Pontuação: {math.ceil((1 - tentativas/max_tentativas) * 100)} pontos")
                break
            elif palpite < numero_secreto:
                print("📈 Tente um número MAIOR!")
                # Dica baseada em porcentagem
                diferenca = numero_secreto - palpite
                if diferenca <= 10:
                    print("🔥 Você está muito perto!")
                elif diferenca <= 30:
                    print("👍 Está chegando perto...")
            else:
                print("📉 Tente um número MENOR!")
                diferenca = palpite - numero_secreto
                if diferenca <= 10:
                    print("🔥 Você está muito perto!")
                elif diferenca <= 30:
                    print("👍 Está chegando perto...")
            
            # Dica do número de tentativas restantes
            tentativas_restantes = max_tentativas - tentativas
            print(f"Restam {tentativas_restantes} tentativas\n")
            
        except ValueError:
            print("❌ Por favor, digite um número válido!")
    
    if tentativas == max_tentativas and palpite != numero_secreto:
        print(f"\n💀 GAME OVER! O número era {numero_secreto}")

if __name__ == "__main__":
    jogo_adivinhacao()