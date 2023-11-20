
with open('pattern.txt') as f:
    pattern = f.read()

data = []
with open('data.txt') as f:
    for line in f.readlines():
        data.append(line.strip().split(', '))

for i in data:
    with open(f'messages/{i[0]}.txt', 'w') as f:
        f.write(pattern.format(*i))
