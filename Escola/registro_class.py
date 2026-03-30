class Loja:
    def __init__(self, preco, nome):
        self.preco = preco
        self.nome = nome

    def descricao(self):
        return f'{self.nome} custa {self.preco}'
    
class Livro(Loja):
    def __init__(self, preco, nome, pagina):
        super().__init__(preco, nome)
        self.pagina = pagina
    
    def descricao(self):
        return f'O livro {self.nome} tem {self.pagina} páginas e custa {self.preco}'
    
class Eletronico(Loja):
    def __init__(self, preco, nome, tipo):
        super().__init__(preco, nome)
        self.tipo = tipo

    def descricao(self):
        return f'O {self.nome} é {self.tipo} e custa {self.preco}'
    

class Alimento(Loja):
    def __init__(self, preco, nome, tipo):
        super().__init__(preco, nome)
        self.tipo = tipo

    def descricao(self):
        return f'O {self.nome} é {self.tipo} e custa {self.preco}'
    
livro1 = Livro('19,99', 'O pequeno principe', '30')
print (livro1.descricao())

eletronico1 = Eletronico('3.500', 'Notebook', 'Dell')
print (eletronico1.descricao())

alimento1 = Alimento('15.00', 'Salgadinho', 'Ruffles')
print (alimento1.descricao())