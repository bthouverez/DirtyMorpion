def showMorpion(m):
    for i in range(9):
        print(m[i], end=" ")
        if i % 3 == 2: print()
# 1
print('dirtyMorpion')
morpion = []
for i in range(9):
    morpion.append('-')
showMorpion(morpion)

joueur = 0
end_of_game = False
print('Au tour du joueur', joueur)
while not end_of_game:
    l, c = [int(k) for k in input('line column').split(' ')]
    if morpion[3 * l + c] == '-':
        sign = 'X' if joueur == 0 else 'O'
        morpion[3 * l + c] = sign
    showMorpion(morpion)
    joueur = (joueur + 1) % 2
    print('Au tour du joueur', joueur)