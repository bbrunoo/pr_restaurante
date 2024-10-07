from .avaliacao import Avaliacao
from .itemcardapio import Itemcardapio
from .bebida import Bebida
from .prato import Prato

class Restaurante:
    lista = []
    # constructor
    def __init__(self, Nome, Categoria):
        self._nome = Nome
        self._categoria = Categoria
        # 07/05
        self._status = False
        self._avaliacao = []
        self._cardapio = []
        # insert
        Restaurante.lista.append(self)

    # get all - bruto
    def __str__(self):
        return f'{self.nome} | {self.categoria}'
    
    # 07/05
    # decorator
    @property
    def status(self):
        return 'X' if self._status else 'O'
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def categoria(self):
        return self._categoria

    @classmethod
    def listarRestaurantes(cls):
        print(f'{'nome do restaurante'.ljust(25)} | {'categoria'.ljust(15)} | {'avaliação'.ljust(10)}| {'status'}')
        print('----------------------------------------------------------------')
        for data in cls.lista:
            nome = data.nome
            categoria = data.categoria
            # status =  'Ativo' if data.status else 'Desativado'
            status = data.status
            nota  = data.media_avaliacoes
            print(f'{nome.ljust(25)} | {categoria.ljust(15)} | {nota.ljust(10)}| {status}')
        print('----------------------------------------------------------------')
        
    def desativarAtivar(Indice):
        for data in Restaurante.lista:
            nome = data._nome
            if ( nome == Indice):
                data._status = not data._status

    def statusRestaurante(self):
        self._status = not self._status
            

    def update(Indice, NovoNome, NovaCategoria):
        for data in Restaurante.lista:
            nome = data._nome
            if ( nome == Indice):
                data._categoria = NovaCategoria
                data._nome = NovoNome
                
            
    def delete(Indice):
        id = -1
        for data in Restaurante.lista:
            if ( data._nome == Indice):
                break;
            id = + 1
        if id != -1:
            del Restaurante.lista[id]

    def receber_avaliacao(self, cliente , nota ):
        # para bloquear o informe da nota entre 0 e 5
        if ( 0 < nota <= 5 ):
            data = Avaliacao(cliente, nota)
            self._avaliacao.append(data)

    @property
    def media_avaliacoes(self):
        # para caso de não aver nenhuma avalição, vamos devolver um sinal somente
        if not self._avaliacao:
            return '-'
        soma_das_notas = sum( avaliacao._nota for avaliacao in self._avaliacao)
        # soma = 0
        # for data in  self._avaliacao:
        #     soma = soma + data._nota

        quantidade_de_notas = len(self._avaliacao)

        media = round( soma_das_notas / quantidade_de_notas,1)
        return media
    
    def incluir_bebida_no_cardapio(self,nome, preco, tamanho):
        data = Bebida(nome, preco, tamanho)
        self._cardapio.append(data)

    def incluir_prato_no_cardapio(self,nome, preco, descricao):
        data = Prato( nome, preco, descricao)
        self._cardapio.append(data)

    @property
    def listar_cardapio(self):
        print(f'Cardapio do Restaurante {self.nome} \n')
        print('----------------------------------------------------------------')
        print(f'{'Nome'.ljust(25)} | {' Preço'.ljust(10)}')
        print('----------------------------------------------------------------')
        
        for i, item in enumerate(self._cardapio, start=1):
            
            if hasattr(item, '_descricao'):
                Prato.aplicar_desconto(item)
                mensagem_prato = f'{i} | {item._nome.ljust(25)} | {item._preco} | {item._descricao} |'
                print(mensagem_prato)
            else:
               Bebida.aplicar_desconto(item)
               mensagem_bebida = f'{i} | {item._nome.ljust(25)} | {item._preco} | {item._tamanho} |'
               print(mensagem_bebida) 
               

            print('----------------------------------------------------------------')        
       
        