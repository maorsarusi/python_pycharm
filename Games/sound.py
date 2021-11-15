import pygame

LEFT = 1
SCROLL = 2
RIGHT = 3


def main():
    SOUND_FILE = r"C:\Network\work\Games\UEFA Champions League Theme Song [Lyrics On Screen] (mp3cut.net).mp3"
    pygame.mixer.init()
    pygame.mixer.music.load(SOUND_FILE)
    pygame.mixer.music.play()
    # infinite loop
    while True:

        print("Press 'p' to pause, 'r' to resume")
        print("Press 'e' to exit the program")
        query = input("  ")

        if query == 'p':

            # Pausing the music
            pygame.mixer.music.pause()
        elif query == 'r':

            # Resuming the music
            pygame.mixer.music.unpause()
        elif query == 'e':

            # Stop the mixer
            pygame.mixer.music.stop()
            break


if __name__ == '__main__':
    main()
