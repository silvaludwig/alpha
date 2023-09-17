# Calculo de tinta por area #
ap = float(input('Altura da parede: '))
lp = float(input('Largura da parede: '))
arp = ap*lp
t = arp / 2

print(f'A área da sua parede é {arp}!')
print(f'Vai gastar {t:.2f}L de tinta.')

