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
  if entrada[0].isupper():  # Valida se a entrada começa com letra maiúscula
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
    animal = input('Digite o nome do animal: ')  # Solicita o nome do animal para o usuário
    validar_entrada(entrada=animal)  # Valida a entrada do usuário
    comida = input('Digite o nome da comida: ')  # Solicita o nome da comida para o usuário
    validar_entrada(entrada=comida)  # Valida a entrada do usuário
    return {'pet': animal, 'food': comida}  # Retorna um dicionário com o animal e a comida
  except ValueError as e:  # Trata o erro caso a entrada seja inválida
    print(e)


def stop():
  """
  Função que para o loop.
  Args: Nenhum.
  Essa função cria argumentos para outras funções.
  Returns: True ou False
  Se o usuário digitar P o loop para, caso contrário o loop continua
  """
  go = input('[P]arar?').strip().upper()  # Solicita ao usuário se deseja parar o loop
  if go == 'P':  # Verifica se o usuário digitou 'P' se sim:
    return True  # Então Retorna True caso o usuário deseje parar o loop
  else:  # Caso contrário
    return False  # Retorna False para continuar o loop


def loop_criar_animal_comida():
  """
  Função que cria um loop para criar animais e comidas e salva em um arquivo json.
  Args: Nenhum.
  Essa função usa 3 funções: criar_animal_comida e stop dimiunuindo a quantidade de linhas de código.
  Returns: Nenhum.
  Essa função não retorna nada, apenas cria um loop para criar animais e comidas e salva em um arquivo json
  Depois vou criar uma função para ler o arquivo json e mostrar os animais e comidas criados.
  """
  while True:  # Cria um loop infinito
    try:  # Tenta executar o código abaixo
      criar = criar_animal_comida()  # Chama a função criar_animal_comida e armazena o retorno na variável criar
      global save  # Declara a variável save como global.
      save.append(criar)  # Adiciona o retorno da função criar_animal_comida na lista save
      df = pd.DataFrame(save)  # Cria um DataFrame com a lista save
      df.to_json('diretorio.json', orient='records')  # Salva o DataFrame em um arquivo json
      if stop() is True:  # Chama a função stop e verifica se o retorno é True
        break  # Se o retorno for True, sai do loop
      else:
        continue
    except ValueError as e:
      print(e)
      if stop() is True:
        break
      else:
        continue