from itemcardapio import Itemcardapio

class Bebida(Itemcardapio):
    def __init__(self, nome, preco, tamanho):
        super().__init__(nome, preco)
        self._tamanho = tamanho



    def aplicar_desconto(self):
       self._valor -= ( self._valor * 0.5) 
