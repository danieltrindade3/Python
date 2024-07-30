cor = {
    'normal':'\033[m',
    'vermelho':'\033[31m',
    'verde':'\033[32m',
    'amarelo':'\033[33m',
    'azul':'\033[34m',
    'magenta':'\033[35m'
}
print('{}-=-'.format(cor['amarelo']) * 20)
print('{}Analisador de Triângulos'.format(cor['azul']))
print('{}-=-'.format(cor['amarelo']) * 20)
r1 = float(input('{}Primeiro segmento:{} '.format(cor['magenta'], cor['normal'])))
r2 = float(input('{}Segundo segmento:{} '.format(cor['verde'], cor['normal'])))
r3 = float(input('{}Terceiro segmento:{} '.format(cor['vermelho'], cor['normal'])))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima {}PODEM FORMAR um triângulo!{}'.format(cor['verde'], cor['normal']))
else:
    print('Os segmentos acima {}NÃO PODEM FORMAR um triângulo!{}'.format(cor['vermelho'], cor['normal']))