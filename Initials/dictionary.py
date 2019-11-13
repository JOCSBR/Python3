# dictionary

#john
john = {'name': 'john', 'lastname': 'travolta', 'profession': 'actor', 'age': 36, 'sons': ['jr','mary']}
print(john['sons'])
print('len =',len(john))
del john['age']
print(john)
john['age'] = 30
print(john)
print('sons' in john)
for x in john:
    print(x+': ',john[x])

# paul
paul = {0: 'paul', 1:'anka', 2: 'musician', 3: 46, 4: ['cindy']}
print(paul[3])
print('len =',len(paul))
print(paul.get(0, 'Not exist'))
print(paul)
paul[4].append('linda')
print(paul)
paul.clear()
print(paul)

#exercicio
cores = {'vermelho':'red', 'azul':'blue','verde':'green', 'amarelo':'yellow'}
cor = input('Insira cor em Pt').lower()
traducao = cores.get(cor, 'Nao encontrado')
print(traducao)

