"""
A palavra secreta é representada por uma linha de traços em cada letra da palavra. 
Esta pode vir de uma variável ou arquivo, como achar melhor.
Se o jogador que adivinha sugerir uma letra que ocorre na palavra, o programa a escreve em todas as posições corretas. 
Se a letra sugerida for incorreta, o programa deve mostrar isso de alguma forma (desenho, mensagem, etc.).
As tentativas (acertos e erros) são definidas em variáveis.
Quando se esgotarem as tentativas, o programa finaliza dizendo que o jogador perdeu e mostra a palavra correta.
Algumas funções, importações e variáveis foram pré-definidas para auxiliá-los!
"""

from random import choice
from dia12_palavras import WORDS, STATUS

def get_secret_word(words: list) -> str:

    # Devolve uma palavra aleatória de uma lista.

    return choice(words)

def print_game_board(secret_word: str, correct_letters: list, wrong_letters: list) -> None:
    # Imprime a situação atual do jogo.

    encoded_word = ""

    for letter in secret_word:
        if letter not in correct_letters:
           encoded_word += "_"
        else:
            encoded_word += letter

    if error <= attempts:
        print(STATUS[error])
        print(encoded_word)

    print(f"\n Letras corretas: {', '.join(correct_letters)}")
    print(f" Letras erradas: {', '.join(wrong_letters)}")

    return None

def read_input_player() -> str:
    # Lê uma letra do usuário.

    player_letter = str(input("\nJogador, digite uma letra: ").toLowerCase())
    return player_letter

def guess_letter(player_letter: str, secret_word: str, correct_letters: list, wrong_letters: list) -> bool:
    
    """
    Verifica se uma letra está na palavra secreta ou já foi jogada, seja certa ou errada.
    Se a letra estiver na palavra secreta, ela deve ser adicionada a lista de letras corretas.
    Se a letra não estiver na palavra secreta, ela deve ser adicionada a lista de letras erradas.
    Se a letra já foi jogada, ela deve ser adicionada a lista de letras erradas.
    """

    if player_letter in secret_word and player_letter not in correct_letters:
        correct_letters.append(player_letter)
        return True

    elif player_letter not in secret_word and player_letter not in wrong_letters:
        wrong_letters.append(player_letter)
        return False

    else:
        print("Essa letra já foi jogada, por favor, escolha outra!")
        return False

def game_continue(secret_word: str, correct_letters: list, wrong_letters: list, error: int, attempts: int) -> bool:
    # Função que decide se jogo já encerrou ou não.
    
    if set(correct_letters) == set(secret_word):
        print("\nParabéns, você ganhou! A palavra secreta era:", secret_word)
        return False

    elif error >= attempts:
        print(STATUS[error])
        print("\nVocê perdeu! A palavra era:", secret_word)
        return False    

secret_word = get_secret_word(WORDS) # variável para palavra secreta
correct_letters = []  # variável que armazena as letras corretas já jogadas
missed_letters = []  # variável que armazena as letras incorretas já jogadas
error = 0  # erro inicial
attempts = 6  # tentativas

while game_continue(correct_letters, secret_word, error, attempts, STATUS):
    
    print_game_board(secret_word, correct_letters, missed_letters, error, attempts, STATUS)
    
    player_letter = read_input_player()

    if not guess_letter(player_letter, secret_word, correct_letters, missed_letters):
        error += 1
        print("\nVocê errou! Tente novamente!")