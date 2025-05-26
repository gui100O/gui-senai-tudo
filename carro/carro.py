class Carro:
    def __init__(self, modelo):
        self.modelo = modelo
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 10

    def frear(self):
        self.velocidade = max(0, self.velocidade - 10)

    def mostrar_velocidade(self):
        print(f"Velocidade atual do {self.modelo}: {self.velocidade} km/h")
