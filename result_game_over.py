import pygame
import pyautogui
from tkinter import filedialog
from importlib import import_module

class ResultGameOver:
    def __init__(self):
        pygame.init()

        self.sound_for_game_over = pygame.mixer.Sound("Sounds/harris_cole__game_over.mp3")

        # postavljanje veličine ekrana na veličinu monitora
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.width, self.height = self.screen.get_size()

        # postavljanje slike u pozadini preko cijelog ekrana
        self.background = pygame.image.load("Images/background.jpg").convert()
        self.background = pygame.transform.scale(self.background, (self.width, self.height))

        # font za dugmad
        self.font = pygame.font.Font(None, 35)

        # font za text game over
        self.font_for_winner = pygame.font.Font(None, 63)
        self.game_over_text1 = self.font_for_winner.render('Oh, no!', True, (255, 255, 255))
        self.game_over_text2 = self.font_for_winner.render('Your game is over!', True, (255, 0, 0))


        # postavljanje dugmadi
        button_width, button_height = 200, 50
        restart_button_rect = pygame.Rect((self.width - button_width) // 2, self.height // 2 + button_height + 30, button_width, button_height)
        screenshot_button_rect = pygame.Rect((self.width - button_width) // 2, self.height // 2 + button_height + 100, button_width, button_height)
        exit_button_rect = pygame.Rect((self.width - button_width) // 2, self.height // 2 + 2 * (button_height + 60), button_width, button_height)
        self.buttons = [
            {"rect": restart_button_rect, "text": "Restart"},
            {"rect": screenshot_button_rect, "text": "Screenshot"},
            {"rect": exit_button_rect, "text": "Exit"}
        ]


    def run(self):
        running = True
        self.sound_for_game_over.play()
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    for button in self.buttons:
                        if button["rect"].collidepoint(event.pos):
                            if button["text"] == "Restart":
                                print("Pritisnuto dugme restart")
                                running = False
                                pygame.quit()
                                FirstLevel = getattr(import_module("first_game"), "FirstLevel")
                                first_level = FirstLevel()
                                first_level.run()


                            elif button["text"] == "Screenshot":
                                print("Pritisnuto dugme screenshot")
                                myScreenshot = pyautogui.screenshot()
                                file_path = filedialog.asksaveasfilename(defaultextension='.png')
                                if not file_path:
                                    return
                                myScreenshot.save(file_path)

                            elif button["text"] == "Exit":
                                print("Pritisnuto dugme exit")
                                running = False



            # crtanje pozadine
            self.screen.blit(self.background, (0, 0))

            # ispisivanje poruke o završetku igre i rezultata
            game_over_text1_rect = self.game_over_text1.get_rect()
            game_over_text2_rect = self.game_over_text2.get_rect()

            # Centriranje teksta
            game_over_text1_rect.center = (self.width / 2, self.height / 2 - 210)
            game_over_text2_rect.center = (self.width / 2, self.height / 2 - 120)

            # Prikazivanje teksta na zaslonu
            self.screen.blit(self.game_over_text1, game_over_text1_rect)
            self.screen.blit(self.game_over_text2, game_over_text2_rect)


            # crtanje dugmadi
            for button in self.buttons:
                pygame.draw.rect(self.screen, (255, 0, 0), button["rect"])
                text_surface = self.font.render(button["text"], True, (255, 255, 255))
                text_rect = text_surface.get_rect(center=button["rect"].center)
                self.screen.blit(text_surface, text_rect)

            pygame.display.flip()

        pygame.quit()


if __name__ == '__main__':
    result_game_over = ResultGameOver()
    result_game_over.run()