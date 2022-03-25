"""
Uma cartela de BINGO consiste em 5 colunas de 5 números que são rotulados com as letras B, I, N, G e O.
Atenção: Google it, para quem nunca viu uma cartela dessas!

Existem 15 números que podem aparecer sob cada letra respeitando a regra abaixo.
- B -> números variando de 1 a 15  (inclusos)
- I -> números variando de 16 a 30 (inclusos)
- N -> números variando de 31 a 45 (inclusos)
- ... e assim por diante

Passo número 0:
- Escreva uma função que crie uma cartela de BINGO aleatória. Dica(podemos usar um dicionário!). 
- As chaves serão as letras B, I, N, G e O. 
- Os valores serão as listas de cinco números aleatórios respeitando a regra dos intervalos de cada letra. 

Passo número 1: 
- Escreva uma segunda função que exiba a cartela de BINGO com as colunas rotuladas apropriadamente
- Formate a saída no terminal para que a cartela seja impressa em forma de colunas (letras e seus valores abaixo)

Passo número 2: 
- Sorteie uma letra e número aleatório (respeitando a regra) e veja se a cartela contém aquele número.

Passo número 3:
- Sorteie 50 (letras e) números e verifique se a cartela é vencedora ou não.
- Uma cartela é vencedora quando preencher uma linha ou coluna inteira com números sorteados.

Passo número desafio:
- Simule 1.000 jogos que sorteiam TODOS os números até que uma mesma cartela seja preenchida e contabilize:
    * O número mínimo de sorteio para que a cartela seja vencedora (não necessariamente preencher toda a cartela!)
    * A média do número de sorteios para que a cartela seja vencedora
    * O número máximo de sorteios para que a cartela seja vencedora
"""

from random import choice, randint, seed
import dia10_cartela

# Travando o gerador de números aleatórios
seed(1)

cartela_1 = dia10_cartela.gerar()

dia10_cartela.imprime(cartela_1)

letra_sorteada = choice(dia10_cartela.LETRAS)

minimo, maximo = dia10_cartela.min_max(letra_sorteada)

numero_sorteado = randint(minimo, maximo)

print(f"A combinação sorteada foi: {letra_sorteada} {numero_sorteado}")

if numero_sorteado in cartela_1[letra_sorteada]:

    indice = cartela_1[letra_sorteada].index(numero_sorteado)

    print(f'O número sorteado está na cartela!')
    cartela_1[letra_sorteada][indice] = '--'

cartela.imprime(cartela_1)