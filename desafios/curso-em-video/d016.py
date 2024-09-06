from math import sin, cos, tan, radians
cor = {
    'normal':'\033[m',
    'amarelo':'\033[33m',
    'magenta':'\033[35m',
    'ciano':'\033[36m'
}
angu = float(input('{}Digite o ângulo que você deseja:{} '.format(cor['amarelo'], cor['normal'])))
seno = sin(radians(angu))
coss = cos(radians(angu))
tang = tan(radians(angu))
print('O ângulo de {}{}{} tem o {}SENO de {:.2f}'.format(cor['magenta'], angu, cor['normal'], cor['ciano'], seno))
print('{}O ângulo de {}{}{} tem o {}COSSENO de {:.2f}'.format(cor['normal'], cor['magenta'], angu, cor['normal'], cor['ciano'], coss))
print('{}O ângulo de {}{}{} tem o {}TANGENTE de {:.2f}'.format(cor['normal'], cor['magenta'], angu, cor['normal'], cor['ciano'], tang))