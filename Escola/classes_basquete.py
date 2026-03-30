class Esporte:
    def __init__(self, nome, uniforme):
        self.nome = nome
        self.uniforme = uniforme
    def apresentar(self):
        return f'O {self.uniforme} é do time {self.nome}'

esporte1 = Esporte('', '')
print(esporte1.apresentar())

class Basquete(Esporte):
    def __init__(self, nome, uniforme, bola):
        super().__init__(nome,uniforme)
        self.bola = bola
    def apresentar(self):
        return f'No basquete o {self.uniforme} joga com a {self.bola}'
    
basquete1 = Basquete('', 'boston', 'laranja')
print(basquete1.apresentar())