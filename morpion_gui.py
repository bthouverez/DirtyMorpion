import pygame
pygame.init()
screen_size = 300
morpion = ['-' for i in range(9)]
joueur, end_of_game = 0, False
orange, black = (255, 175, 14), (0, 0, 0)

screen = pygame.display.set_mode((screen_size, screen_size))
pygame.display.set_caption('dirtyMorpion')
screen.fill(orange)
rec = pygame.Rect(100, -1, 100, 302)
pygame.draw.rect(screen, black, rec, 1)
rec = pygame.Rect(-1, 100, 302, 100)
pygame.draw.rect(screen, black, rec, 1)
font = pygame.font.SysFont('monospace', 75, True)
pygame.display.flip()

while not end_of_game:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        end_of_game = False
        pygame.quit()
      if event.type == pygame.MOUSEBUTTONDOWN:
        c, l = [int(i/100) for i in pygame.mouse.get_pos()]
        if morpion[3 * l + c] == '-':
            sign = 'X' if joueur == 0 else 'O'
            morpion[3 * l + c] = sign
            label = font.render(sign, 1, black)
            screen.blit(label, (100*c+30, 100*l+10))
            pygame.display.update()
        joueur = (joueur + 1) % 2