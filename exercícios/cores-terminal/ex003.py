nome = 'Daniel'
cores = {
    'limpo':'\033[m', 
    'azul':'\033[34m', 
    'vermelho': '\033[31m'
    }
print('Prazer em te conhecer {}{}{}!'.format(cores['azul'], nome, cores['limpo']))
# print('Prazer em te conhecer {}{}{}!'.format('\033[4;34m', nome, '\033[m'))