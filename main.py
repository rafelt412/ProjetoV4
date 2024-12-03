import pandas as pd

save = []


def validar_entrada(entrada):
  """
  Função que valida a entrada do usuário, para a validação do animal e comida
  Ela recebe uma entrada do usuário e retorna True se a entrada for válida, e False se for inválida
  Args:
    entrada (str): entrada do usuário (animal ou comida)
    Obs: Uso uma função para pedir os dados do usuário e validar a entrada
  Returns:
    bool: True se a entrada for válida, e Retorna um erro caso seja inválida
    Obs: Aqui tem muitas mensagens de erro, podendo reaprovei-las para o usuário
  Exemplo De Uso:
    >>> def função():  # Função que recebe a entrada do usuário
    >>> animal = 'cachorro' # "Entrada do usuário"
    >>> validar_entrada(entrada= animal)  # Valida a entrada do usuário
    >>> return True  # Retorna True se a entrada for válida
    >>> except Valueerror as e: # Caso a entrada seja inválida, retorna um erro
    >>> print(e)
  """
  if len(entrada) < 3:  # Valida se a entrada é menor que 3 caracteres
    raise ValueError(
        'Entrada inválida, o número de caracteres deve ser maior ou igual a 3')
  if entrada[0] == ' ':  # Valida se a entrada começa com um espaço
    raise ValueError(
        'Entrada inválida, o primeiro caractere não pode ser um espaço')
  if entrada[-1] == ' ':  # Valida se a entrada termina com um espaço
    raise ValueError(
        'Entrada inválida, o último caractere não pode ser um espaço')
  if entrada.count(' ') > 3:  # Válida se a entrada possui mais de 3 espaços
    raise ValueError(
        'Espaços inválidos, a entrada deve conter no máximo 3 espaços')
  if entrada[0].isuper():  # Valida se a entrada começa com letra maiúscula
    raise ValueError(
        'Entrada inválida, o primeiro caractere deve ser minúsculo')
  if isinstance(entrada, int):  # Valida se a entrada é um número
    raise ValueError('Entrada inválida, o valor deve ser uma string')
  return True


def criar_animal_comida():
  """
  Função que cria um animal e sua comida
  Args: Nenhum.
  Essa função cria argumentos para outras funções.
  Returns: Dicionário com a chave pet e o valor o animal e a chave food e o valor a comida
  E erro caso a entrada seja inválida seja aniaml ou comida
  """
  try:
    animal = input('Digite o nome do animal: ')
    validar_entrada(entrada=animal)
    comida = input('Digite o nome da comida: ')
    validar_entrada(entrada=comida)
    return {'pet': animal, 'food': comida}
  except ValueError as e:
    print(e)


def stop():
  go = input('[P]arar?').strip().upper()
  if go == 'P':
    return True
  else:
    return False


def loop_criar_animal_comida():
  while True:
    try:
      criar = criar_animal_comida()
      global save
      save.append(criar)
      df = pd.DataFrame(save)
      df.to_json('diretorio.json', orient='records')
      if stop() is True:
        break
      else:
        continue
    except ValueError as e:
      print(e)
      if stop() is True:
        break
      else:
        continue
validar_entrada(entrada=' cachorro')