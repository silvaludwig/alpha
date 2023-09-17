# conversor de medidas

n1 = float(input('Digite um número em metros: '))
cm = n1 * 100
mm = n1 * 1000
km = n1 / 1000

print(f'{n1} pode ser convertido em {cm}cm, {mm}mm, ou {km}km!')
