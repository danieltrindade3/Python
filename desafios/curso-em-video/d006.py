cor = {
    'normal':'\033[m',
    'amarelo':'\033[33m',
    'magenta':'\033[35m',
    'ciano':'\033[36m'
}
metros = float(input('{}Uma distância em metros:{} '.format(cor['amarelo'], cor['normal'])))
km = metros / 1000
hm = metros / 100
dam = metros / 10
dm = metros * 10
cm = metros * 100
mm = metros * 1000
print('A medida de {}{}m{} corresponde a: {}\n{:.1f}km\n{:.1f}hm\n{:.1f}dam\n{:.1f}dm\n{:.1f}cm\n{:.1f}mm{}'.format(cor['magenta'], metros, cor['normal'], cor['ciano'], km, hm, dam, dm, cm, mm, cor['normal']))