import pandas as pd  # Importa a biblioteca pandas


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
  verificar = verificação(animal)  # Verifica se a entrada do usuário é válida
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
