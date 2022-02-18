'''
Introdução à sintaxe e tipos de dados
'''

# Desafio 1
aluno = input("Digite o nome do aluno: ")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))    

media = (nota1 + nota2 + nota3) / 3
media_arred = round(media, 2)

print(f"\nO(a) aluno(a) {aluno} teve a média {media_arred}")

# Desafio 2
nome = input("Digite o seu nome: ")
letra = input("Digite uma letra: ")

print(f"Seu nome é {nome}, nele existem {len(nome)} letras e {nome.count(letra)} delas são '{letra}'")