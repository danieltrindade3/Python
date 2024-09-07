cid = str(input('\033[33mEm que cidade você mora?\033[m ')).strip()
# print('SANTO' in cid[:5].upper())
print('\033[35m', cid[:5].upper() == 'SANTO')