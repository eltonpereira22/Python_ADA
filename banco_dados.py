import pyodbc
from utils import valida_cpf, valida_rg, valida_data_nascimento, busca_cep

def retornar_cursor_banco_dados():
  connection = pyodbc.connect(retorna_string_conexao_banco_dados())
  cursor = connection.cursor()
  return cursor, connection
  # cursor.execute("select * from cliente_python;")
  # clientes = cursor.fetchall()
  # print(clientes)

def retorna_string_conexao_banco_dados():
    return(
        "DRIVER={SQL Server};"
        "SERVER=HOESQL633;"
        "DATABASE=SkillUp_ERPEREI;"
        "Trusted_connection=yes"
    )

def select_banco_dados(cpf):
   cursor, connection = retornar_cursor_banco_dados()
   query_select = "SELECT * FROM cliente_exercicio WHERE cpf = '" + cpf + "';"
   cursor.execute(query_select)
   cliente=cursor.fetchall()
   for i in cliente:
         print("Cliente ID: "+str(i[0]))
         print("Nome: "+ str(i[1]))
         print("CPF: "+ str(i[2]))
         print("RG: "+ str(i[3]))
         print("Data de Nascimento: "+str(i[4]))
         print("CEP: "+str(i[5]))
         print("Logradouro: "+str(i[6]))
         print("Complemento: "+str(i[7]))
         print("Bairro: "+str(i[8]))
         print("Cidade: "+str(i[9]))
         print("Estado: "+str(i[10]))
         print("Número da residência: "+str(i[11]))
   opcao = input("Pressione Enter")
   connection.commit()


   # cursor, connection = retornar_cursor_banco_dados()
   # cursor.execute('''select * from cliente_python where cpf = '''+cliente['CPF']+''';''')
   # clientes = cursor.fetchall()
   # print(clientes)
   # connection.commit()

def lista_banco_dados():
   cursor, connection = retornar_cursor_banco_dados()
   list_query = "SELECT * FROM cliente_exercicio;"
   cursor.execute(list_query)
   clientes = cursor.fetchall()
   print(clientes)
   connection.commit() 

def update_banco_dados (cpf):
   cliente_update = {
        "Nome": input("Digite o Nome: "),
        "CPF": valida_cpf(input("Digite o CPF: ")),
        "RG": valida_rg(input("Digite o RG: ")),
        "Nascimento": valida_data_nascimento(),
        "CEP": busca_cep(input("Digite o CEP: ")),
        "Complemento": input("Digite o complemento: "),
        "Numero": input("Digite o Número da casa: ")
   }
   cursor, connection = retornar_cursor_banco_dados()
   update_query = "UPDATE cliente_exercicio SET nome = ?, cpf = ?, rg = ?, data_nascimento = ?, cep = ?, numero_residencia = ? WHERE cpf = '" + cpf + "';"
   values = (cliente_update['Nome'],
             cliente_update['CPF'],
             cliente_update['RG'],
             cliente_update['Nascimento'],
             cliente_update["CEP"]["CEP"],
             cliente_update['Numero'])
   cursor.execute(update_query,values)
   connection.commit()
   # cursor, connection = retornar_cursor_banco_dados()
   # #update_query = "UPDATE cliente_python SET nome = ?, cpf = ?, rg = ?, data_nascimento = ?, cep = ?, numero_residencia = ? WHERE cpf = " + int(cliente['CPF']) + ";"
   # update_query = "UPDATE cliente_python SET nome = ?, cpf = ?, rg = ?, data_nascimento = ?, cep = ?, numero_residencia = ? WHERE cpf = 22507582049;"
   # #set = (cliente['Nome'], cliente['CPF'], cliente['RG'],cliente['Nascimento'], cliente['CEP'],cliente['Numero'])
   # set = cliente['Nome'], cliente['RG'],cliente['Nascimento'], cliente['CEP'],cliente['Numero']
   # cursor.execute(update_query,set)
   # connection.commit()

def insert_banco_dados(cliente_dicionario):
   cursor, connection = retornar_cursor_banco_dados()
   insert_query='''
   INSERT INTO Cliente_exercicio (Nome, CPF, RG, data_nascimento, cep, logradouro,complemento,bairro,cidade,estado, numero_residencia)
   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
   '''
   values = (cliente_dicionario['Nome'], cliente_dicionario['CPF'],cliente_dicionario['RG'],cliente_dicionario['Nascimento'], cliente_dicionario["CEP"]["CEP"], cliente_dicionario['CEP']['Logradouro'], 
              cliente_dicionario['Complemento'], cliente_dicionario['CEP']['Bairro'], cliente_dicionario['CEP']['Cidade'], cliente_dicionario['CEP']['Estado'], cliente_dicionario['Numero'])
   cursor.execute(insert_query, values)
   connection.commit()

def delete_banco_dados(cpf):
  cursor, connection = retornar_cursor_banco_dados()
  delete_query = "DELETE FROM cliente_exercicio WHERE cpf = '" + cpf + "';"
  cursor.execute(delete_query)
  connection.commit()
