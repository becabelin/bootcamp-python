aluno = "Rebeca Belin Alves Sousa"
notas = [7, 8, 9, 10]

media = sum(notas) / len(notas)

media_arred = round(media, 2)
print(f"A média do aluno {aluno} é:", media_arred)

print(f"A primeira letra do nome é {aluno[0]}") # 0 é o primeiro caractere
print(f"A última letra do nome é {aluno[-1]}") # -1 é o último caractere
print(f"A primeira palavra do nome é {aluno.split()[0]}") # split() separa a string em uma lista

