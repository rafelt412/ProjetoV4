import pandas as pd
import os

save = []

def clear():
    os.system('clear')

def criar_animal_comida():
    animal = input("Digite o nome de um animal: ")
    validar_entrada(entrada= animal)
    comida = input("Digite o nome de uma comida: ")
    return animal,comida
def validar_entrada(entrada):
    while True:
        if not entrada:
            clear()
            print(f'Não deixe o nome do(a) {entrada} em branco!')
            continue
        if len(entrada) < 3:
            ...
        return True
