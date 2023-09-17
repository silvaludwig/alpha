# Cálculo de desconto #

p = float(input('Qual o preço do produto? '))
d = float(input('Quantos % de desconto? '))
pcd = p - (p * d) / 100

print(f'O protudo custava {p}, mas com o desconto de {d}% passa a custar {pcd}!')