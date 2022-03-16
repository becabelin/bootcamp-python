import dia6

# pedir o número de alunos
numero_alunos = int(input("Digite o número de alunos: "))
# pedir o número de notas
numero_notas = int(input("Digite o número de notas: "))

# para cada aluno, pedir as notas e calcular a média
for i in range(numero_alunos):
    # nome do aluno
    aluno = input(f"\nDigite o nome do {i+1}º aluno: ")

    # para cada nota, pedir a nota e somar
    notas = []
    for j in range(numero_notas):
        nota = float(input(f"Digite a {j+1}º nota: "))
        notas.append(nota)

    # calcular a média com a função calcula_media
    media = dia6.calcula_media(notas)

    # dizer se foi aprovado ou não
    if media >= 7:
        status = "aprovado"
    elif media >= 6:
        status = "de recuperação"
    else:
        status = "reprovado"

    # mostrar a média
    print(f"\nA média do aluno {aluno} é {media} e ele está {status}")