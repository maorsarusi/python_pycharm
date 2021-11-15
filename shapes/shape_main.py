from shapes.shape import Ball
import pygame
import random

BACKGROUND = r"C:\Network\work\shapes\background.jpg"
NUMBERS_OF_BALLS = 7
DISTANCE = 100


def main():
    pygame.init()
    start = (0, 0)
    pygame.display.set_caption("Maor Haaluf")
    size = (700, 700)
    screen = pygame.display.set_mode(size)
    background = pygame.image.load(BACKGROUND)
    screen.blit(background, start)
    clock = pygame.time.Clock()

    ball_list = pygame.sprite.Group()
    new_ball_list = pygame.sprite.Group()
    finish = False

    while not finish:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish = True
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = pygame.mouse.get_pos()
                ball = Ball(x, y)
                vx = random.randint(-9, 9)
                vy = random.randint(-9, 9)
                ball.update_v(vx, vy)
                ball_list.add(ball)

        for ball in ball_list:
            ball.update_location()
            x, y = ball.get_pos()
            vx, vy = ball.get_v()
            if x + 55 > 700 or x < 0:
                vx *= -1
            if y + 55 > 700 or y < 0:
                vy *= -1
            ball.update_v(vx, vy)

        new_ball_list.empty()
        for ball in ball_list:
            hit = pygame.sprite.spritecollide(ball, ball_list, False)
            if len(hit) == 1:
                ball_list.add(ball)
        ball_list.empty()
        for ball in new_ball_list:
            ball_list.add(ball)

        screen.blit(background, start)
        ball_list.draw(screen)
        pygame.display.flip()
        clock.tick(60)


if __name__ == '__main__':
    main()
