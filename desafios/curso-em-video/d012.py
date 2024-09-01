cor = {
    'limpo':'\033[m',
    'amarelo':'\033[33m',
    'azul':'\033[34m',
    'magenta':'\033[35m'
}
c = float(input('{}Informe a tempetura em {}°C:{} '.format(cor['amarelo'], cor['azul'], cor['limpo'])))
f = (c * 9/5) + 32
print('A temperatura de {}{}°C{} corresponde a {}{}°F{}'.format(cor['azul'], c, cor['limpo'], cor['magenta'], f, cor['limpo']))