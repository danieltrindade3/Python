from random import randint
from time import sleep
com = randint(0, 5) # Faz o computador "pensar"
cor = {
    'normal':'\033[m',
    'vermelho':'\033[31m',
    'verde':'\033[32m',
    'amarelo':'\033[33m',
    'azul':'\033[34m',
    'magenta':'\033[35m',
}
print('{}-=-'.format(cor['amarelo']) * 20)
print('{}Vou pensar em um número entre 0 e 5. Tente adivinhar...'.format(cor['azul']))
print('{}-=-{}'.format(cor['amarelo'], cor['normal']) * 20)
num = int(input('Em que número eu pensei? '))
print('{}Processando...'.format(cor['magenta']))
sleep(3)
if num == com:
    print('{}Parabéns! {}Você conseguiu me vencer!'.format(cor['verde'], cor['normal']))
else:
    print('{}Ganhei! {}Eu pensei em {}{}{} ao invés de {}{}{}'.format(cor['vermelho'], cor['normal'], cor['verde'], com, cor['normal'], cor['vermelho'], num, cor['normal']))