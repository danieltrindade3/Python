metros = float(input('Uma distância em metros: '))
km = metros / 1000
hm = metros / 100
dam = metros / 10
dm = metros * 10
cm = metros * 100
mm = metros * 1000
print('A medida de {}m corresponde a: \n{:.1f}km\n{:.1f}hm\n{:.1f}dam\n{:.1f}dm\n{:.1f}cm\n{:.1f}mm'.format(metros, km, hm, dam, dm, cm, mm))

