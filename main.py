class Carro:
    def __init__(self, marca, cor, n_portas, modelo, ano):
        self.marca = marca
        self.cor = cor
        self.n_porta = n_portas
        self.modelo = modelo
        self.ano = ano

uno = Carro('fiat', 'cinza', 2, 'fiat uno', 2012)
print(uno.modelo)