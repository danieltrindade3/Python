from random import randint
from time import sleep
com = randint(0, 5) # Faz o computador "pensar"
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
num = int(input('Em que número eu pensei? '))
print('Processando...')
sleep(3)
if num == com:
    print('Parabéns! Você conseguiu me vencer!')
else:
    print('Ganhei! Eu pensei em {} ao invés de {}'.format(com, num))