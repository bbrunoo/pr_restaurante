Estrutura do MVC
Model: Representa os dados e a lógica de negócios.
View: Responsável pela interface com o usuário.
Controller: Intermediário que manipula a lógica entre o Model e a View.
Passo a Passo da Refatoração
1. Criar o Model
O Model representará o restaurante e suas operações.
python
# model.py
class Restaurante:
    def __init__(self, nome, tipo):
        self.nome = nome
        self.tipo = tipo
        self.cardapio_pratos = []
        self.cardapio_bebidas = []

    def incluir_prato_no_cardapio(self, item, preco, descricao):
        prato = {'item': item, 'preco': preco, 'descricao': descricao}
        self.cardapio_pratos.append(prato)

    def incluir_bebida_no_cardapio(self, item, preco, descricao):
        bebida = {'item': item, 'preco': preco, 'descricao': descricao}
        self.cardapio_bebidas.append(bebida)

    def listar_restaurantes(self):
        print(f'Restaurante: {self.nome}, Tipo: {self.tipo}')

    def listar_cardapio(self):
        print("Cardápio de Pratos:")
        for prato in self.cardapio_pratos:
            print(f"{prato['item']} - R${prato['preco']}: {prato['descricao']}")
        
        print("\nCardápio de Bebidas:")
        for bebida in self.cardapio_bebidas:
            print(f"{bebida['item']} - R${bebida['preco']}: {bebida['descricao']}")

2. Criar a View
A View será responsável pela interação com o usuário.
python
# view.py
class RestauranteView:
    def introduction_page(self):
        message = '''
            Sistema Restaurante

            * 1. Listar Restaurantes 
            * 2. Inserir Prato 
            * 3. Inserir Bebida
            * 4. Listar Cardápio
            * 5. Sair 
        '''
        print(message)
        command = int(input('Comando: '))
        return command

    def obter_detalhes_prato(self):
        item = input("Informe o nome do prato: ")
        preco = float(input("Informe o valor do prato: "))
        descricao = input("Informe a descrição do prato: ")
        return item, preco, descricao

    def obter_detalhes_bebida(self):
        item = input("Informe o nome da bebida: ")
        preco = float(input("Informe o valor da bebida: "))
        descricao = input("Informe a descrição da bebida: ")
        return item, preco, descricao

    def mostrar_resultado(self, resultado):
        print(resultado)

3. Criar o Controller
O Controller irá orquestrar as interações entre o Model e a View.
python
# controller.py
from model import Restaurante
from view import RestauranteView

class RestauranteController:
    def __init__(self):
        self.view = RestauranteView()
        self.loja = Restaurante("Pizzaria do Ze", "Pizzaria")

    def executar(self):
        while True:
            command = self.view.introduction_page()
            if command == 1:
                self.loja.listar_restaurantes()
            elif command == 2:
                item, preco, descricao = self.view.obter_detalhes_prato()
                self.loja.incluir_prato_no_cardapio(item, preco, descricao)
            elif command == 3:
                item, preco, descricao = self.view.obter_detalhes_bebida()
                self.loja.incluir_bebida_no_cardapio(item, preco, descricao)
            elif command == 4:
                self.loja.listar_cardapio()
            elif command == 5:
                exit()
            else:
                print('\n Comando não encontrado!! \n\n')

4. Executar o Programa
Por fim, criamos um arquivo principal para executar a aplicação.
python
# main.py
from controller import RestauranteController

if __name__ == "__main__":
    app = RestauranteController()
    app.executar()

Explicação da Refatoração
Model (model.py)
Classe Restaurante: Contém métodos para incluir pratos e bebidas no cardápio e listar informações sobre o restaurante e seu cardápio. A lógica de negócios está isolada aqui.
View (view.py)
Classe RestauranteView: Responsável por apresentar informações ao usuário e coletar entradas. Os métodos introduction_page, obter_detalhes_prato, e obter_detalhes_bebida separam claramente as interações com o usuário da lógica de negócios.
Controller (controller.py)
Classe RestauranteController: Atua como intermediário entre o Model e a View. O método executar gerencia o fluxo da aplicação chamando métodos apropriados do Model e atualizando a View com os dados necessários.
Execução (main.py)
Arquivo Principal: Este arquivo inicializa a aplicação criando uma instância do Controller e chamando seu método executar, que inicia todo o fluxo da aplicação.
Benefícios da Refatoração
Separação de Preocupações: Cada componente tem uma responsabilidade clara.
Facilidade de Manutenção: Alterações em uma parte do código não afetam as outras partes.
Reutilização de Código: O Model pode ser reutilizado em diferentes Views ou Controllers.
Testabilidade: Cada componente pode ser testado individualmente.
Essa estrutura não apenas melhora a organização do código mas também facilita futuras expansões e manutenções na aplicação. Se precisar de mais ajuda ou exemplos adicionais, sinta-se à vontade para perguntar!