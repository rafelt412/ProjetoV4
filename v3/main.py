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
    animal = input("Digite o nome de um animal: ")
    validar_entrada(entrada= animal)
    comida = input("Digite o nome de uma comida: ")
    return animal,comida


def validar_entrada(entrada):
    """
    Função que valida a entrada de dados do usuário
    na parte de "criação" do animal e a comida
    Args=
        (entrada):str 
    Returns=
        (animal):str e (comida):str
    """
    while True:
        if not entrada:
            clear()
            print(f'Não deixe o nome do(a) {entrada} em branco!')
            continue
        if len(entrada) < 3:
            ...
        ...
salve