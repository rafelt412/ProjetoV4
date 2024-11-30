import pandas as pd

save = []


def validar_entrada(entrada):
  if len(entrada) < 3:
    raise ValueError(
        'Entrada inválida, o número de caracteres deve ser maior ou igual a 3')
  if entrada[0] == ' ':
    raise ValueError(
        'Entrada inválida, o primeiro caractere não pode ser um espaço')
  if entrada[-1] == ' ':
    raise ValueError(
        'Entrada inválida, o último caractere não pode ser um espaço')
  if entrada.count(' ') <= 3:
    raise ValueError(
        'Entrada inválida, o número de espaços deve ser menor ou igual a 3')
  if entrada[0].isuuper():
    raise ValueError(
        'Entrada inválida, o primeiro caractere deve ser minúsculo')
  if not isinstance(entrada, int):
    ...


def criar_animal_comida():
  """
  Função que cria um animal e sua comida
  Args: Nenhum.
  Returns: Dicionário com a chave pet e o valor o animal e a chave food e o valor a comida.
  """
  animal = input('Digite o nome do animal: ')
  comida = input('Digite o nome da comida: ')
  ...
