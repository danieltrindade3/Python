from math import sin, cos, tan, radians
angu = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(angu))
coss = cos(radians(angu))
tang = tan(radians(angu))
print('O ângulo de {} tem o SENO de {:.2f}'.format(angu, seno))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(angu, coss))
print('O ângulo de {} tem o TANGENTE de {:.2f}'.format(angu, tang))