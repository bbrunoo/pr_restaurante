from abc import ABC, abstractmethod

class Itemcardapio:
    def __init__(self, nome, preco ):
        self._nome = nome
        self._preco = preco

    def __str__( self ):
        return  f' - {self._nome} - {self._preco}'
    
    @property
    def preco(self):
        preconew = str( self._preco).replace( ".", ",")
        # preconew = preconew.replace( ".", "*")
        return preconew
    
    @abstractmethod
    def aplicar_desconto(self):
      pass