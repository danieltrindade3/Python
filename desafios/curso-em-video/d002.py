cor = {
    'limpo':'\033[m',
    'amarelo':'\033[33m',
    'magenta':'\033[35m'
    }
n = input('{}Digite algo:{} '.format(cor['amarelo'], cor['limpo']))
print('\033[36mQual o tipo?', cor['magenta'], type(n))
print('\033[36mSó tem espaço?', cor['magenta'], n.isspace())
print('\033[36mÉ um numérico?', cor['magenta'], n.isnumeric())
print('\033[36mÉ alfabético?', cor['magenta'], n.isalpha())
print('\033[36mÉ alfanumérico?', cor['magenta'], n.isalnum())
print('\033[36mEstá em minúsculo?', cor['magenta'], n.islower())
print('\033[36mEstá em maiúsculo?', cor['magenta'], n.isupper(), cor['limpo'])