import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame

def main():

    try:
        pygame.mixer.init()
    except pygame.error as e:
        print("Audio initialaztion failed!", e)
        return

    folder = "music"

    if not os.path.isdir(folder):
        print(f"Folder '{folder}' not found")
        return

if __name__ == "__main__":
    main()