#ex018 - Ler um angulo, dar seno, coseno e tangente.
import math
ang = float(input('Digite um angulo: '))
sin = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print(f'o seno é {sin:.2f}, o coseno é {cos:.2f} e a tangente é {tan:.2f}!')