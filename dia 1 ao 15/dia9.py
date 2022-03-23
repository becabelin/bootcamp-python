from math import radians, acos, sin, cos

print("Primeiro ponto")
t1 = radians(float(input("Digite a latitude em graus: ")))
g1 = radians(float(input("Digite a longitude em graus: ")))

print("\nSegundo ponto")
t2 = radians(float(input("Digite a latitude em graus: ")))
g2 = radians(float(input("Digite a longitude em graus: ")))

distancia = 6371.01 * acos(sin(t1) * sin(t2) + cos(t1) * cos(t2) * cos(g1 - g2))

print("\nA distância entre os pontos é de: %.2f km" % distancia)

# print("Primeiro ponto")

# t1,g1 = map(
#    float,input("Digite a primeira coordenada sem espaços separadas por vírgula: ").split(","))

# t2,g2 = map(
#    float,input("Digite a segunda coordenada sem espaços separadas por vírgula: ").split(","))