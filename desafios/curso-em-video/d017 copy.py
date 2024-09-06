from random import shuffle
cor = {
    'normal':'\033[m',
    'verde':'\033[32m',
    'amarelo':'\033[33m',
}
n1 = str(input('{}Primeiro aluno:{} '.format(cor['amarelo'], cor['normal'])))
n2 = str(input('{}Segundo aluno:{} '.format(cor['amarelo'], cor['normal'])))
n3 = str(input('{}Terceiro aluno:{} '.format(cor['amarelo'], cor['normal'])))
n4 = str(input('{}Quarto aluno:{} '.format(cor['amarelo'], cor['normal'])))
lista = [n1,n2,n3,n4]
shuffle(lista)
print('A ordem de apresentação será: ')
print(cor['verde'], lista, cor['normal'])