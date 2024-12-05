from funçoes import mostrar, filtrar_animal, filtrar_comida
from funçoes import Excluir_animal_Excluir, Excluir_comida
from main import loop_criar_animal_comida, limpar_terminal

def pergunta_mostrar():
    interacao = input('[D]eseja ver o arquivo.json? ').upper().strip()
    if interacao == 'D':
        limpar_terminal()
        mostrar()
    else:
        limpar_terminal()
        return print('Pulando\n.......')
def pergunta_filtrar():
    interagir = input('Deseja [F]iltrar? ').upper()
    limpar_terminal()
    if interagir == 'F':
        filtrar_pet_comida = input('Filtrar [A]nimal ou [C]omida? ').upper()
        limpar_terminal()
        if filtrar_pet_comida == 'A':
            animall = input(
                "Digite o nome do animal que"
                " você deseja filtrar: "
            ).strip()
            limpar_terminal()
            return filtrar_animal(animal= animall)
        if filtrar_pet_comida == 'C':
            comidaa = input('Digite a comida que deseja filtrar: ').strip()
            limpar_terminal()
            return filtrar_comida(comida= comidaa)
    else:
        limpar_terminal()
        return print('pulando\n........')
def pergunta_excluir():
    interacao = input('Deseja [E]xcluir dados? ').strip().upper()
    limpar_terminal()
    if interacao == 'E':
        alternativa = input(
            "Você deseja remover os dados"
            " de [A]nimais ou [C]omida? "
        ).strip().upper()
        limpar_terminal()
        if alternativa == 'A':
            Excluir_animal_Excluir()
        elif alternativa == 'C':
            Excluir_comida()
        else:
            try:
                raise ValueError('Valor inválido!')
            except ValueError as erro:
                print(f'{erro}')
    else:
        print('pulando.......')
def InicioPrograma():
    loop_criar_animal_comida()
    pergunta_mostrar()
    pergunta_filtrar()
    pergunta_excluir()
    pergunta_mostrar()
InicioPrograma()
