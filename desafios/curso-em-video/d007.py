cor = {
    'normal':'\033[m',
    'amarelo':'\033[33m',
    'ciano':'\033[36m'
}
num = int(input('{}Digite um número para ver sua tabuada:{} '.format(cor['amarelo'], cor['normal'])))
print('-' * 12)
print('{} X {:2} = {}{}{}'.format(num, 1, cor['ciano'], num * 1, cor['normal']))
print('{} X {:2} = {}{}{}'.format(num, 2, cor['ciano'], num * 2, cor['normal']))
print('{} X {:2} = {}{}{}'.format(num, 3, cor['ciano'], num * 3, cor['normal']))
print('{} X {:2} = {}{}{}'.format(num, 4, cor['ciano'], num * 4, cor['normal']))
print('{} X {:2} = {}{}{}'.format(num, 5, cor['ciano'], num * 5, cor['normal']))
print('{} X {:2} = {}{}{}'.format(num, 6, cor['ciano'], num * 6, cor['normal']))
print('{} X {:2} = {}{}{}'.format(num, 7, cor['ciano'], num * 7, cor['normal']))
print('{} X {:2} = {}{}{}'.format(num, 8, cor['ciano'], num * 8, cor['normal']))
print('{} X {:2} = {}{}{}'.format(num, 9, cor['ciano'], num * 9, cor['normal']))
print('{} X {:2} = {}{}{}'.format(num, 10, cor['ciano'], num * 10, cor['normal']))
print('\033[m-' * 12)