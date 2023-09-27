from utils import valida_cpf, valida_rg, valida_data_nascimento, busca_cep
from banco_dados import insert_banco_dados, select_banco_dados, delete_banco_dados, update_banco_dados, lista_banco_dados

def menu_cliente():
  validador_menu = True
  #lista_cliente = []
  
  while validador_menu:
    print("\n"
      "\n******************************************************************************************" 
      "\n**********************************MENU CLIENTES*******************************************"
      "\n******************************************************************************************"
      "\n"
      "\n Selecione uma das opções abaixo:"
      "\n 1 - Cadastrar Cliente"
      "\n 2 - Alterar Cliente"
      "\n 3 - Buscar Cliente"
      "\n 4 - Deletar Cliente"
      "\n 5 - Listar Clientes"
      "\n 6 - Voltar ao menu anterior")
    opcao = int(input("Digite a opção desejada do menu cliente: "))
    if opcao == 1:
      cliente_dicionario = {
        "Nome": input("Digite o Nome: "),
        "CPF": valida_cpf(input("Digite o CPF: ")),
        "RG": valida_rg(input("Digite o RG: ")),
        "Nascimento": valida_data_nascimento(),
        "CEP": busca_cep(input("Digite o CEP: ")),
        "Complemento": input("Complemento: "),
        "Numero": input("Digite o Número da casa: ")
      }
      insert_banco_dados(cliente_dicionario)
      return cliente_dicionario
      # print(cliente_dicionario)
      # print(cliente_dicionario["CEP"]["CEP"])
      # insert_banco_dados(cliente_dicionario)
    elif opcao == 2:
      print("Atualização de Cliente")
      update_banco_dados(input("Digite o CPF do cliente que deseja alterar: "))
      # cliente= {
      #   "Nome": input("Digite o Nome: "),
      #   "RG": valida_rg(input("Digite o RG: ")),
      #   "Nascimento": valida_data_nascimento(),
      #   "CEP": busca_cep(input("Digite o CEP: ")),
      #   "Numero": input("Digite o Número da casa: ")
      # }
      # print(cliente)
      # update_banco_dados(cliente)
      # input("Digite o CPF do registro a ser atualizado: ") -
      # update_banco_dados(cliente) -
      # print("Pressione Enter para retornar ao menu principal...") -
      # print("Atualizar cadastro de banco de dados") --
      # cliente=int(input("Digite o CPF de quem deseja atualizar: ")) --
      # update_banco_dados(cliente) --
    elif opcao == 3:
      select_banco_dados(input("Digite o CPF do cliente que deseja buscar: "))
      # print("Busca registro através do numero do CPF:")
      # cpf=int(input("Digite o numero do CPF para buscar informacoes: "))
      # select_banco_dados(cpf)
    elif opcao == 4:
      print("Excluir registro de banco de dados")
      cpf=input("Digite o CPF para excluir: ")
      delete_banco_dados(cpf)
    elif opcao == 5:
      print("Listar Banco de dados")
      lista_banco_dados()
    elif opcao == 6:
      print("Encerrando a execução do programa.")
      validador_menu = False
    else:
      print("Opção inválida.")