class Carro:
    def __init__(self, marca, cor, n_portas, modelo, ano):
        self.marca = marca
        self.cor = cor
        self.n_portas = n_portas
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0
        self.ligado = False

    def ligar(self):
        if self.ligado:
            print('O carro já está ligado')
        else:
            print('Ligando carro...')
            self.ligado = True
    
    def desligar(self):
        if not self.ligado:
            print('O carro está desligado')
        else:
            print('Desligando o carro...')
            self.ligado = False

    def acelerar(self):
        if self.ligado:
            self.velocidade += 10
            print(f'Velocidade atual do carro {self.velocidade}')
        else:
            print('O carro não esta ligado')
        

uno = Carro('fiat', 'cinza', 2, 'fiat uno', 2012)
uno.ligar()
uno.ligar()
uno.desligar()
uno.desligar()
uno.acelerar()
uno.ligar()
uno.acelerar()
uno.acelerar()
uno.acelerar()











# # class Carro:
# #     def __init__(self, marca, cor, n_portas, modelo, ano):
# #         self.marca = marca
# #         self.cor = cor
# #         self.n_porta = n_portas
# #         self.modelo = modelo
# #         self.ano = ano
# #         self.ligado = False
# #         self.acelarando = False



# # def ligar(self):
# #     if self.ligado:
# #         print('O carro já está ligado!')
# #     else: 
# #         print('Ligando carro...')
# #         self.ligado = True
    

# # uno = Carro('fiat', 'cinza', 2, 'fiat uno', 2012)
# # uno.ligar()
# # uno.ligar()



    
# class Carro:
#     def __init__(self, marca, cor, n_portas, modelo, ano):
#         self.marca = marca
#         self.cor = cor
#         self.n_portas = n_portas
#         self.modelo = modelo
#         self.ano = ano
#         self.velocidade = 0
#         self.acelerando = False
#         self.ligado = False

        

#     # def ligar(self):
#     #     if self.ligado:
#     #         print('O carro ja esta ligado')
#     #     else:
#     #         print('Ligando carro...')
#     #         self.ligado = True
        

#     # def ligar(self):
#     #     if not self.ligado:
#     #         print('O carro ja esta ligado')
#     #     else:
#     #         print('Desligando o carro...')
#     #         self.ligado = True

#     # def acelerar(self):
#     #     if self.acelerando:
#     #         print('O carro nao esta acelerando...')
#     #     else:
#     #         print('O carro esta acelerando')
#     #         self.acelerando = True
        


# uno = Carro('fiat', 'cinza', 2, 'fiat uno', 2012)
# uno.ligar()
# uno.ligar()

# uno.acelerar()
# uno.acelerar()
