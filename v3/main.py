import pandas as pd
import os

save = []


def clear():
    """
    Função que limpa o terminal
    Args=
        nenhum.
    Returns=
        limpa o terminal
    """
    os.system('clear')


def criar_animal_comida():
    """
    Função que pede o nome de um animal e de uma
    comida para o usuário.
    Args=
        nenhum.
    Returns=
        Tupla (animal,comida):str
    """
    while True:
        animal = input("Digite o nome de um animal: ")
        if validar_entrada(entrada=animal, tipo='animal') is False:
            continue
        else:
            break
    while True:
        comida = input('Digite o nome de uma comida para o animal descrito: ')
        if validar_entrada(entrada=comida, tipo='comida') is False:
            continue
        else:
            break
    return animal, comida


def validar_entrada(entrada, tipo):
    """
    Função que valida a entrada de dados do usuário
    na parte de "criação" do animal e a comida
    Args=
        (entrada):str
    Returns=
        (animal):str e (comida):str
    """
    while True:
        try:
            if not isinstance(entrada, str):
                clear()
                raise ValueError('erro: digite somente letras')
            if isinstance(entrada, str) and not entrada.strip():
                clear()
                raise NameError(
                    f'Erro: não deixe espaços em branco no(a) {tipo}')
            try:
                float_entrada = float(entrada)
                if float_entrada == 0:
                    clear()
                    print(f'Erro: não digite 0 no(a) {tipo}')
                    return False
                if float_entrada != 0:
                    clear()
                    print(f'Erro: não digite numeros no(a) {tipo}')
                    return False
            except ValueError:
                return True
        except NameError as e:
            clear()
            print(f'{e}')
            return False
        except ValueError as e:
            clear()
            f'{e}'
            return False
a = criar_animal_comida()
print(a)