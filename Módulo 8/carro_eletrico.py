# Classe CarroEletrico
class CarroEletrico(Carro):
    def __init__(self, marca, modelo, autonomia_bateria):
        super().__init__(marca, modelo)
        self.autonomia_bateria = autonomia_bateria

    def exibir_info(self):
        print(f"⚡ {self.marca} {self.modelo} - luxo sustentável com {self.autonomia_bateria}km de autonomia.")

    def __str__(self):
        return f"{self.marca} {self.modelo} ⚡ ({self.autonomia_bateria}km)"


# Meus carros 😌
carro1 = Carro("Chevrolet", "Camaro")
carro2 = CarroEletrico("Tesla", "Model 3", 550)

# Exibindo
carro1.exibir_info()
carro2.exibir_info()

print(carro1)
print(carro2)