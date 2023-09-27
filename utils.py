#from utils import valida_cpf
from validate_docbr import CPF
import re
from datetime import datetime
import requests

def valida_cpf(cpf_input):
  cpf = CPF()
  while True:
    cpf_input = re.sub('[-.]','',cpf_input) #substitui - ou . por <vazio>
    resultado = cpf.validate(cpf_input)
    if resultado == True:
      cpf_formatado = f"{cpf_input[0:3]}.{cpf_input[3:6]}.{cpf_input[6:9]}-{cpf_input[9:]}" #insere o CPF no padrao correto
      return cpf_input
    else:
      cpf_input = input("CPF inválido. Digite novamente: ")
    
# pra pular o laço: CONTINUE, BREAK, RETURN, ALTERAÇAO CONDICAO

def valida_rg(rg_input):
  padrao_rg = r'^\d{2}\.\d{3}\.\d{3}-[0-9A-Za-z]$' #Formato 11.111.111-1
  
  while True:

    rg_input = re.sub('[-.]','', rg_input)
    rg_input = f'{rg_input[0:2]}.{rg_input[2:5]}.{rg_input[5:8]}-{rg_input[8:]}'
    if re.match(padrao_rg, rg_input):
      return rg_input
    else:
      rg_input = input("RG inválido. Digite novamente: ")


def valida_data_nascimento():

  while True: #enquanto -> condicao verdadeira
    data_nascimento_input = input("Digite a data de nascimento: ")
    try:
      data_convertida = datetime.strptime(data_nascimento_input, '%Y-%m-%d').date() #transforma em data
      data_atual = datetime.now().date()
      
      if data_convertida < data_atual:
        return data_convertida.strftime("%Y-%m-%d") #transforma em string com o padrao de data
      
      else:
        print("Data inválida. A sua data de nascimento deve ser menor que a data atual ")
        # data_nascimento_input = input ("Data de Nascimento inválida. A data de nascimento deve ser menor que a atual. Pressione ENTER")
        # return data_nascimento_input

    except  ValueError as e:
      print("Formato de data inválido. Você recebeu o erro: ", e, "  Tente novamente.")
      #data_nascimento_input = input ("Data de Nascimento inválida. Digite novamente: ")

  # print(data_atual)
  # print(data_convertida)
  # print(type(data_convertida))

  # data_string = data_convertida.strftime("%d/%m/%Y") #transforma em string
  # print(data_string)
  # print(type(data_string))

def busca_cep(cep_input):
  url = f'https://viacep.com.br/ws/{cep_input}/json'

  response = requests.get(url, verify=False)

  if response.status_code == 200:
    data=response.json()

    endereco = {
      "CEP": data['cep'],
      "Logradouro": data['logradouro'],
      "Bairro": data['bairro'],
      "Cidade": data['localidade'],
      "Estado": data['uf']
    }

    return endereco

  print(response)
  print("******************************")
  print(response['CEP'])
  print(response['bairro'])
  print(type(response))