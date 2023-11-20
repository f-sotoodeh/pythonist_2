from random import choice, randint


firstnames = []
with open('firstnames.txt') as f:
    for line in f.readlines():
        firstnames.append(line.split()[1].strip())

lastnames = []
with open('lastnames.txt') as f:
    for line in f.readlines():
        lastnames.append(line.split()[1].strip())

names = []
for i in range(100):
    firstname = choice(firstnames)
    lastname = choice(lastnames)
    score = randint(60, 80) / 4
    s = f'{firstname} {lastname}, {score}'
    names.append(s)

with open('data.txt', 'w') as f:
    f.write('\n'.join(names))

