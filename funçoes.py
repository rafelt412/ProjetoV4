import pandas as pd  # Importa a biblioteca pandas
from main import limpar_terminal

def ler():
  """
  Função que lê o arquivo json e o reutiliza em outras funções
  Args: Nenhum.
  Returns: Dicionário com a chave pet e o valor o animal e a chave food e o valor a comida
      exemplo:  {"pet": "cachorro", "food": "ração"}
  """
  df = pd.read_json('diretorio.json', orient='records')  # Lê o arquivo json
  return df  # Retorna o dicionário


def animal_filtro():
  """
  Função que filtra os animais com base na entrada do usuário
  Args: Nenhum.
  Returns: Nome de um animal
           animal: str
  """
  animal = input('Digite o nome do animal: ')
  return animal


def verificação(
    animal
):  # Verifica se a entrada do usuário é válida e pega o animal da função animal_filtro
  """
  Função que verifica se a entrada do usuário é válida e pega o animal da função animal_filtro
  Args: return da função animal_filtro
        animal: str
  Retorns: True se a entrada for válida, e False se for inválida
  """
  df = ler()  # Lê o arquivo json
  if animal in df['pet'].values:  # Verifica se o animal está no arquivo json
    return True  # Retorna True se a entrada for válida
  else:
    return False  # Retorna False se a entrada for inválida


def filtrar_animal(animal):  # Filtra os animais com base na entrada do usuário(função animal_filtro))
  """
  Esta Fução filtra os animais com base na entrada do usuário(função animal_filtro)
  Args: return da função animal_filtro
        animal: str
  Returns: Retorna uma lista com os animais que contém o mesmo nome da entrada do usuário
          exemplo: ['cachorro'] ['cachorro', 'gato']']
          filtrar_animal(cachorro)
          ['cachorro','cachorro']
  """
  verificar = verificação(animal= animal)  # Verifica se a entrada do usuário é válida
  if verificar is True:  # Se a entrada for válida
    df = ler()  # Lê o arquivo json
    df_animal = df[df['pet'] == animal]  # Filtra os animais com base na entrada do usuário
    return print(df_animal)
  else:
    raise KeyError('Animal não encontrado')


def filtrar_animal_completo(
):  #Melhorar essa função encapsulando outras funções para que fique mais limpo e robusto
  animal = animal_filtro()
  filtrar_animal(animal=animal)


def comida_filtro():
  comida = animal_filtro()
  return comida


def verificação_comida(comida):
  df = ler()
  if comida in df['food'].values:
    return True
  else:
    raise ValueError('Comida não encontrada')


def filtrar_comida(comida):
  verificar = verificação_comida(comida)
  if verificar is True:
    df = ler()
    df_comida = df[df['food'] == comida]
    return print(df_comida)


def mostrar():
  """
  Função que mostra os dados do diretorio.json
  Args:  nenhum.
  Returns:  Retorna os dados do arquivo json de forma ordenada
  """
  df = ler()
  for _, dados in df.iterrows():
    print(f'Animal: {dados["pet"]} Comida: {dados["food"]}\n')



def solicitar_animal_excluir():
  """
  Função que pede o nome do animal que o usuário deseja excluir.
  Args:  nenhum.
  Returns:  (animal): str
  """
  animal = input(
    "Digite o nome de um animal"
    " que queira excluir: "
  ).strip()
  return animal


def animal_verificar_Excluir(animal):
  """
  Função que verifica se o animal que o usuário
  digitou, existe no Dataframe/diretorio
  Args:  (animal): nome de um animal que o usuário escolheu
  Returns:  (bool): retorna um valor booleano
  se o animal existir, retorna True caso contrário retorna False
  """
  df = ler()
  df_animal = df[df["pet"] == animal]
  return not df_animal.empty


def Excluir_animal_Excluir():
  """
  Função que engloba todas as funções criadas para
  excluir o nome de um animal dentro do Dataframe
  Args:  nenhum.
  Returns:  não retorna nada, porém exclui uma chave
  do DataFrame caso contrário um erro aparece :)
  """
  animal = solicitar_animal_excluir()
  limpar_terminal()
  verificar = animal_verificar_Excluir(animal= animal)
  if verificar is True:
    df = ler()
    df = df[df["pet"] != animal]
    df.to_json('diretorio.json', orient="records")
    print(f'O animal: ({animal}) foi excluido!')
  else:
    try:
      raise KeyError(
        f"O animal: ({animal})"
        " não foi encontrado."
      )
    except KeyError as erro:
      print(f'{erro}')


def solicitar_comida_excluir():
  comida = input(
    "Digite o nome da comida que"
    " queira excluir: "
  ).strip()
  return comida


def verificar_comida_excluir(comida):
  df = ler()
  df_comida = df[df["food"] == comida]
  return not df_comida.empty


def Excluir_comida():
  comida = solicitar_comida_excluir()
  verificar = verificar_comida_excluir(comida= comida)
  if verificar is True:
    df = ler()
    df = df[df["food"] != comida]
    df.to_json('diretorio.json', orient="records")
    limpar_terminal()
    print(
      f"A comida: ({comida}) foi deletada com sucesso!"
    )
  else:
    try:
      raise KeyError(
        f"Erro: a comida: ({comida})"
        " não foi encontrada no diretório!"
      )
    except KeyError as erro:
      print(f'{erro}')
