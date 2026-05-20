# Classe Carro 
class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def exibir_info(self):
        print(f"✨ Um belo {self.marca} {self.modelo}, puro luxo.")

    def __str__(self):
        return f"{self.marca} {self.modelo} 💎"