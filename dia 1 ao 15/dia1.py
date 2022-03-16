print("Hello World")

# Desafio 1
distancia = float(input("Digite a distância em km: "))
velocidade_media = float(input("Digite a velocidade média em km/h: "))
tempo_total_horas = distancia / velocidade_media

print(f"\nO tempo total de viagem é de {tempo_total_horas:.2f} horas\n")
print(f"{distancia}->{velocidade_media}")

# Desafio 2
qtd_km = int(input("Digite a quantidade de quilômetros percorridos: "))
qtd_dias = int(input("Digite quantos dias você ficou com o carro:"))

preco_por_dia = 60
preco_por_km = 0.15

preco_total_km = qtd_km * preco_por_km
preco_total_dia = qtd_dias * preco_por_dia

preco_a_pagar = preco_total_km + preco_total_dia

print(f"Total a pagar: R$ {preco_a_pagar:7.2f}")