cor = {
    'normal':'\033[m',
    'amarelo':'\033[33m',
    'azul':'\033[34m',
    'magenta':'\033[35m',
    'ciano':'\033[36m'
}
lar = float(input('{}Largura da parede:{} '.format(cor['amarelo'], cor['normal'])))
alt = float(input('{}Altura da parede:{} '.format(cor['amarelo'], cor['normal'])))
área = lar * alt
litro = área / 2
print('Sua parede tem a dimensão {}{}X{} {}e sua área é de {}{}m².'.format(cor['azul'], lar, alt, cor['normal'], cor['magenta'], área))
print('{}Para pintar a parede, você precisa de {}{}l de tinta.{}'.format(cor['normal'], cor['ciano'], litro, cor['normal']))