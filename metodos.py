class carro:
    def __init__(self, nome, velocidade=0):
        self.nome = nome
        self.velocidade = velocidade

    def acelera(self):
        self.velocidade += 10
        return f'Velocidade atual: {self.velocidade}km/h'
    
    def desacelerar(self):
        self.velocidade -= 10
        return f'Velocidade atual: {self.velocidade}km/h'
    
palio = carro('palio')

print(palio.acelera())
print(palio.acelera())
print(palio.acelera())
print(palio.acelera())
print(palio.desacelerar())
print(palio.desacelerar())