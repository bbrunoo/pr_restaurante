from services.restaurante import Restaurante

def introduction_page():   
   message = '''
        Sistema Restaurante

        * 1. Listar Restaurantes 
        * 2. Inserir Prato 
        * 3 .Inserir Bebida
        * 4. Utilitarios
        * 5. Sair 
    '''
   print(message)
   command = int(input('Comando: '))
   return command

def menu() -> None:
    loja = Restaurante("Pizzaria do Ze", "Pizzaria")
    while True:
        command = introduction_page()
        if command == 1:             
            loja.listarRestaurantes()
        elif command == 2: 
            item = str(input("informe o nome do prato: " ))
            preco = float(input("informe o valor do prato: " ))
            descricao = str(input("informe a descrição do prato: " ))
            loja.incluir_prato_no_cardapio(item, preco, descricao)
        elif command == 3: 
            item = str(input("informe o nome do prato: " ))
            preco = float(input("informe o valor do prato: " ))
            descricao = str(input("informe a descrição do prato: " ))
            loja.incluir_bebida_no_cardapio(item, preco, descricao)
        elif command == 4: 
            loja.listar_cardapio
        elif command == 5: 
            exit()
        else: 
            print('\n Comando nao encontrado!! \n\n')

