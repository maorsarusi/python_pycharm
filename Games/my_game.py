import pygame

LEFT = 1
SCROLL = 2
RIGHT = 3


def main():
    SOUND_FILE = r"C:\Network\work\Games\UEFA Champions League Theme Song [Lyrics On Screen] (mp3cut.net).mp3"
    pygame.mixer.init()
    pygame.mixer.music.load(SOUND_FILE)

    pygame.init()
    size = (640, 490)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Game")
    COLOR = (255, 255, 255)
    screen.fill(COLOR)
    IMAGE = r"C:\Network\work\Games\games.jfif"
    img = pygame.image.load(IMAGE)
    screen.blit(img, (0, 0))
    player_image = pygame.image.load(r"C:\Network\work\Games\plane.png").convert()
    player_image.set_colorkey(COLOR)
    x = 350
    y = 250
    psize = (x, y)
    screen.blit(player_image, psize)
    pygame.display.flip()

    mouse_pos_list = []
    clock = pygame.time.Clock()
    finish = False
    while not finish:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish = True
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
                mouse_pos_list.append(pygame.mouse.get_pos())
                for pos in mouse_pos_list:
                    screen.blit(player_image, pos)
                    pygame.display.flip()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    screen.blit(img, (0, 0))
                    pygame.display.flip()
                    mouse_pos_list = []
                elif event.key == pygame.K_c:
                    pygame.mixer.music.play()
                elif event.key == pygame.K_ESCAPE:
                    pygame.mixer.music.stop()

        clock.tick(60)
    pygame.quit()


if __name__ == '__main__':
    main()
