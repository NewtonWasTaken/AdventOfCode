import re

with open('input.txt', 'r') as f:
    text = f.readlines()
numbers = text[0]
text.pop(0)
pocet = 0
tabulky = []
skip_radek = 0
def split(map):
    return([char for char in map if char != '\n'])

for i in text:
    if i == '\n':
        pocet += 1
for i in range(pocet):
    for y in range(1, 6):
        tabulky.append(re.split('\n| +| ', text[skip_radek + y]))


    tabulky.append(' ')
    skip_radek += 6
for x in tabulky:
    if x == '':
        tabulky[x].remove('')
def valid(tab):
    for x in range(len(tab)):
        for y in range(len(tab[i])):
            print()
print(tabulky)