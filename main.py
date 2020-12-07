''' DELETE LINE FOR GUI
import pygame
pygame.init()
DELETE LINE FOR GUI '''

# parameters
screen_size = 300


######################################
def showMorpion(m):
    for i in range(9):
        print(m[i], end=" ")
        if i % 3 == 2: print()


######################################

# 1
print('dirtyMorpion')
morpion = []
for i in range(9):
    morpion.append('-')
showMorpion(morpion)

# 2: main loop, inputs
# morpion[3*l+c] = sign
joueur = 0
end_of_game = False

''' DELETE LINE FOR GUI
# some colors
orange = (255, 175,  14)
black  = (  0,   0,   0)

# setting window
screen = pygame.display.set_mode((screen_size, screen_size))
pygame.display.set_caption('dirtyMorpion')
screen.fill(orange)
# drawing lines rect, cheating on sizes
rec = pygame.Rect(100, -1, 100, 302)
pygame.draw.rect(screen, black, rec, 1)
rec = pygame.Rect(-1, 100, 302, 100)
pygame.draw.rect(screen, black, rec, 1)
# setup font
font = pygame.font.SysFont('monospace', 75, True)

# display window
pygame.display.flip()
DELETE LINE FOR GUI '''

print('Au tour du joueur', joueur)
while not end_of_game:

    ''' DELETE LINE FOR GUI
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        end_of_game = False
        pygame.quit()
  
      if event.type == pygame.MOUSEBUTTONDOWN:
        print("pressed")
        c, l = [int(i/100) for i in pygame.mouse.get_pos()]
    '''
    if 1:
        if 1:
            l, c = [int(k) for k in input('line column').split(' ')]
            # DELETE LINE EXCEPT LAST 3 CHARS FOR GUI '''

            if morpion[3 * l + c] == '-':
                sign = 'X' if joueur == 0 else 'O'
                morpion[3 * l + c] = sign
                ''' DELETE LINE FOR GUI
                label = font.render(sign, 1, black)
                screen.blit(label,(100*c+30,100*l+10))
                pygame.display.update()
                DELETE LINE FOR GUI '''
            showMorpion(morpion)
            joueur = (joueur + 1) % 2
            print('Au tour du joueur', joueur)