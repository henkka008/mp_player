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
    mp3_files = [file for file in os.listdir(folder) if file.endswith(".mp3")]

    if not mp3_files:
        print("No .mp3 files found!")

    while True:
        print("***** MP3 PLAYER *****")
        print("MP3 song list:")

        for index, song in enumerate(mp3_files, start=1):
            print(f"{index}. {song}")
        

        choice_input = input("\nEnter the song # to play (or 'Q' to quit): ")

        if choice_input.upper() == "Q":
            print("Exiting Player...")
            break

        if not choice_input.isdigit():
            print("Enter a valid number")
            continue

if __name__ == "__main__":
    main()