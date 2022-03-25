from collections import defaultdict
from random import randint

LETRAS = ('B', 'I', 'N', 'G', 'O')

def min_max(letra:str) -> tuple[int]:

    intervalo = {"B": (1, 15), "I": (16, 30), "N": (31, 45), "G": (46, 60), "O": (61, 75)}

    # Retorna o número mínimo e máximo de cada letra
    minimo, maximo = intervalo[letra][0], intervalo[letra][1]
    return minimo, maximo

# Passo número 0:
def gerar() -> defaultdict[str, list[int]]:

    cartela = defaultdict(list)

    for letra in LETRAS:

        # Pegando o número mínimo e máximo de cada letra
        minimo, maximo = min_max(letra)

        while len(cartela[letra]) < 5:
            # Gerando os números aleatórios
            num_aleatorio = randint(minimo, maximo)

            # Verificando se o número já existe na lista
            if num_aleatorio in cartela[letra]:
                continue
            
            # Coloca os números aleatórios na lista
            cartela[letra].append(num_aleatorio)

            # Ordena em ordem crescente    
            cartela[letra].sort()

    return cartela

# Passo número 1:
def imprime(cartela: dict[str, list[int]]) -> None:
    # Formata a cartela para imprimir na tela

    print("B   I   N   G   O")
    print("-" * 10)

    for linha in range(5):

        # Para cada linha, ele imprime os elementos daquela linha na tela
        lista_str = [str(lista[linha]).zfill(2) for lista in cartela.values()]
        
        #Formata a string para imprimir
        string = ",".join(lista_str)
        
        print(string)

# Passo número 2: