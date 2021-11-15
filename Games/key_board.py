import pygame

R = 255
G = 255
B = 255

def main():
    pygame.init()
    size = (640, 490)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Game")
    COLOR = (R, G, B)
    screen.fill(COLOR)
    IMAGE = r"C:\Network\work\Games\games.jfif"
    img = pygame.image.load(IMAGE)
    screen.blit(img, (0, 0))
    player_image = pygame.image.load(r"C:\Network\work\Games\plane.png").convert()
    player_image.set_colorkey(COLOR)
    x = 245
    y = 215
    psize = (x, y)
    screen.blit(player_image, psize)
    pygame.display.flip()
    pos_list = []
    clock = pygame.time.Clock()
    finish = False
    while not finish:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y -= 15
                    pos = (x, y)
                    screen.blit(img, (0, 0))
                    screen.blit(player_image, pos)
                    pygame.display.flip()
                elif event.key == pygame.K_DOWN:
                    y += 15
                    pos = (x, y)
                    screen.blit(img, (0, 0))
                    screen.blit(player_image, pos)
                    pygame.display.flip()

                elif event.key == pygame.K_LEFT:
                    x -= 15
                    pos = (x, y)
                    screen.blit(img, (0, 0))
                    screen.blit(player_image, pos)
                    pygame.display.flip()
                elif event.key == pygame.K_RIGHT:
                    x += 15
                    pos = (x, y)
                    screen.blit(img, (0, 0))
                    screen.blit(player_image, pos)
                    pygame.display.flip()
                pos_list += [pos]
            clock.tick(60)
    pygame.quit()
    print(pos_list)


if __name__ == '__main__':
    main()
