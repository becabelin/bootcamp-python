'''
Introdução à sintaxe e tipos de dados
'''

aluno = input("Digite o nome do aluno: ")

nota1 = float(input("Digite a primeira nota: "))

nota2 = float(input("Digite a segunda nota: "))

nota3 = float(input("Digite a terceira nota: "))    

media_float = (nota1 + nota2 + nota3) / 3

media_int = round(media_float)

print(f"\nO(a) aluno(a) {aluno} teve a média {media_int}")