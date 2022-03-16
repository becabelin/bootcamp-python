aluno = input('Digite o nome do aluno: ')

notas = []
notas.append(float(input('Digite a primeira nota: ')))
notas.append(float(input('Digite a segunda nota: ')))
notas.append(float(input('Digite a terceira nota: ')))

media = sum(notas) / len(notas)
media_arred = round(media, 2)

nota_minima = 7
nota_minima_rec = 6

if media_arred >= nota_minima:
    status = "aprovado"
elif media_arred >= nota_minima_rec:
        status = "de recuperação"
else:
    status = "reprovado"

print(f"A média do(a) aluno(a) {aluno} é {media_arred} e ele(a) está {status}.")