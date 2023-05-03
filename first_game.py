import pygame
import random
import os
import tkinter as tk
from cards_for_first_game import list_of_cards
from result_of_game import Result
from result_game_over import ResultGameOver

class FirstLevel:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()

        self.sound_for_spin = pygame.mixer.Sound("Sounds/spin_sound.wav")
        self.sound_for_failed = pygame.mixer.Sound("Sounds/failed_sound.wav")
        self.sound_for_points = pygame.mixer.Sound("Sounds/points_sound.wav")
        self.sound_for_thief = pygame.mixer.Sound("Sounds/thief_sound.flac")
        self.sound_for_game_over = pygame.mixer.Sound("Sounds/game_over_sound.wav")

 
        self.user1_player = "player"

        settings_root = tk.Tk()

        settings_root.geometry("400x300")

        settings_root.title("Basic settings for the player")

        settings_root.iconbitmap('Images/icon.ico')

        # varijabla za unos korisnickog imena i godina
        username_var = tk.StringVar()

        # kreira labelu za korisnicko ime i polje za unos
        username_label = tk.Label(settings_root, text="Enter a username:")
        username_label.pack()
        username_entry = tk.Entry(settings_root, textvariable=username_var, width=10, borderwidth=2, highlightthickness=2,
                               relief="groove", bg="white", fg="black")
        username_entry.pack()

        # kreira labelu za dob i polje za unos
        label_for_age = tk.Label(settings_root, text="Choose your age:")
        label_for_age.pack()
        age_label = tk.Spinbox(settings_root, from_=8, to=100)
        age_label.pack()

        # kreira labelu za avatare i padajuci meni za odabir
        avatar_label = tk.Label(settings_root, text="Choose your avatar:")
        avatar_label.pack()
        avatar_var = tk.StringVar()
        avatar_dropdown = tk.OptionMenu(settings_root, avatar_var, "Avatar 1", "Avatar 2", "Avatar 3", "Avatar 4",
                                        "Avatar 5",
                                        "Avatar 6", "Avatar 7", "Avatar 8", "Avatar 9", "Avatar 10", "Avatar 11",
                                        "Avatar 12", "Avatar 13", "Avatar 14", "Avatar 15", "Avatar 16", "Avatar 17",
                                        "Avatar 18", "Avatar 19", "Avatar 20")
        avatar_var.set("Avatar 1")
        avatar_dropdown.pack()

        def submit():
            user = "player"
            random_number_player = str(random.randrange(1000, 10000000))

            if username_var.get() != "":
                username = username_var.get()
                new_username = str(username)
                if new_username.islower():
                    username = new_username
                else:
                    username = new_username.lower()
            else:
                username = user + random_number_player

            age = age_label.get()
            avatar = avatar_var.get()

            self.user1_player = username

            print(f"Korisnicko ime: {username}")
            print(f"Godine: {age}")
            print(f"Avatar: {avatar}")

            return username, age, avatar

        submit_button = tk.Button(settings_root, text="Submit!",
                                  command=lambda: [submit(), settings_root.destroy()])
        submit_button.pack()

        screen_width = settings_root.winfo_screenwidth()
        screen_height = settings_root.winfo_screenheight()
        window_width = settings_root.winfo_width()
        window_height = settings_root.winfo_height()
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        settings_root.geometry(f"+{x}+{y}")

        settings_root.mainloop()


        pygame.display.set_caption("First level")
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        screen_width, screen_height = pygame.display.get_surface().get_size()
        print(f"Screen size: {screen_width}x{screen_height}")
        self.background = pygame.image.load("Images/background_first_level.jpg").convert()
        self.background = pygame.transform.scale(self.background, (screen_width, screen_height))
        self.clock = pygame.time.Clock()

        self.player1_label = pygame.font.SysFont("Times New Roman", 24).render(f"{self.user1_player}", True, (255, 255, 255))
        self.player2_label = pygame.font.SysFont("Times New Roman", 24).render("Player 2", True, (255, 255, 255))

        self.score1 = 0
        self.score2 = 0

        self.player1_score = pygame.font.SysFont("Times New Roman", 24).render(f"Score: {self.score1}", True, (255, 255, 255))
        self.player2_score = pygame.font.SysFont("Times New Roman", 24).render(f"Score: {self.score2}", True, (255, 255, 255))

        self.box1 = pygame.Rect(173, 212, 100, 100)

        self.box2 = pygame.Rect(173, 330, 100, 100)
        self.box3 = pygame.Rect(173, 448, 100, 100)
        self.box4 = pygame.Rect(self.screen.get_width() - 270, 212, 100, 100)
        self.box5 = pygame.Rect(self.screen.get_width() - 270, 330, 100, 100)
        self.box6 = pygame.Rect(self.screen.get_width() - 270, 448, 100, 100)

        self.current_image = None
        self.current_image1 = None
        self.current_image2 = None
        self.current_image3 = None
        self.current_image4 = None
        self.current_image5 = None
        self.current_image6 = None

        self.box7 = pygame.Rect(610, 310, 150, 150)

        self.button_pokreni = pygame.Rect(654, 555, 60, 60)

        self.image_spin = pygame.transform.scale(pygame.image.load("Images/spin.png").convert(),
                                                    (self.button_pokreni.width, self.button_pokreni.height))

        self.box_width = 100
        self.box_height = 100

        self.incorrect_list = []
        self.player1 = []
        self.player2 = []

    def random_image(self):
        path = "Images/Heroes"
        files = os.listdir(path)
        d = random.choice(files)
        abs_path = os.path.join(path, d)
        self.image = pygame.image.load(abs_path).convert_alpha()
        self.scaled_image = pygame.transform.smoothscale(self.image, (self.box_width, self.box_height))
        self.current_image_name = d

        return self.scaled_image


    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.incorrect_list = ""
                    self.player1 = []
                    self.player2 = []
                    if self.button_pokreni.collidepoint(event.pos):
                        self.sound_for_spin.play()
                        self.current_image = self.random_image()
                        if self.current_image.get_width() < 150 or self.current_image.get_height() < 150:
                            self.current_image = pygame.transform.smoothscale(self.image, (150, 150))

                        self.incorrect_list = self.current_image_name

                        self.current_image1 = self.random_image()
                        self.player1.append(self.current_image_name)
                        self.current_image2 = self.random_image()
                        self.player1.append(self.current_image_name)
                        self.current_image3 = self.random_image()
                        self.player1.append(self.current_image_name)

                        self.current_image4 = self.random_image()
                        self.player2.append(self.current_image_name)
                        self.current_image5 = self.random_image()
                        self.player2.append(self.current_image_name)
                        self.current_image6 = self.random_image()
                        self.player2.append(self.current_image_name)

                        for img in self.player1:
                            if img == "return_to_start.png" and self.incorrect_list == "return_to_start.png":
                                self.sound_for_failed.play()
                                self.score1 = 0
                                self.player1_score = pygame.font.SysFont("Times New Roman", 24).render(
                                    f"Score: {self.score1}", True, (255, 255, 255))
                            elif img == "thief.png" and self.incorrect_list == "thief.png":
                                self.sound_for_thief.play()
                                self.score1 += self.score2
                                self.score2 = 0
                                self.player1_score = pygame.font.SysFont("Times New Roman", 24).render(
                                    f"Score: {self.score1}", True, (255, 255, 255))
                                self.player2_score = pygame.font.SysFont("Times New Roman", 24).render(
                                    f"Score: {self.score2}", True, (255, 255, 255))
                            elif img == self.incorrect_list:
                                self.score1 += list_of_cards[img]
                                self.sound_for_points.play()
                                self.player1_score = pygame.font.SysFont("Times New Roman", 24).render(
                                    f"Score: {self.score1}", True, (255, 255, 255))

                        for img2 in self.player2:
                            if img2 == "return_to_start.png" and self.incorrect_list == "return_to_start.png":
                                self.sound_for_failed.play()
                                self.score2 = 0
                                self.player2_score = pygame.font.SysFont("Times New Roman", 24).render(
                                    f"Score: {self.score2}", True, (255, 255, 255))
                            elif img2 == "thief.png" and self.incorrect_list == "thief.png":
                                self.sound_for_thief.play()
                                self.score2 += self.score1
                                self.score1 = 0
                                self.player2_score = pygame.font.SysFont("Times New Roman", 24).render(
                                    f"Score: {self.score2}", True, (255, 255, 255))
                                self.player1_score = pygame.font.SysFont("Times New Roman", 24).render(
                                    f"Score: {self.score1}", True, (255, 255, 255))
                            elif img2 == self.incorrect_list:
                                self.score2 += list_of_cards[img2]
                                self.sound_for_points.play()
                                self.player2_score = pygame.font.SysFont("Times New Roman", 24).render(
                                    f"Score: {self.score2}", True, (255, 255, 255))


                        if self.score1 >= 123 or self.score2 >= 123:
                            print(f"{self.user1_player} je pobijedio!")
                            running = False
                            pygame.quit()
                            rezultat1 = Result()
                            rezultat1.run()

                        if self.score1 < - 1 or self.score2 < - 1:
                            print(f"{self.user1_player} je izgubio!")
                            running = False
                            rezultat2 = ResultGameOver()
                            rezultat2.run()


                        self.screen.blit(self.current_image, self.box7)
                        self.screen.blit(self.current_image1, self.box1)
                        self.screen.blit(self.current_image2, self.box2)
                        self.screen.blit(self.current_image3, self.box3)
                        self.screen.blit(self.current_image4, self.box4)
                        self.screen.blit(self.current_image5, self.box5)
                        self.screen.blit(self.current_image6, self.box6)

                        pygame.display.update()


            self.screen.blit(self.background, (0, 0))
            self.screen.blit(self.player1_label, (50, 50))
            self.screen.blit(self.player2_label, (self.screen.get_width() - 150, 50))
            self.screen.blit(self.player1_score, (52, 662))
            self.screen.blit(self.player2_score, (1215, 662))
            pygame.draw.rect(self.screen, (255, 255, 255), self.box1, 2)
            pygame.draw.rect(self.screen, (255, 255, 255), self.box2, 2)
            pygame.draw.rect(self.screen, (255, 255, 255), self.box3, 2)
            pygame.draw.rect(self.screen, (255, 255, 255), self.box4, 2)
            pygame.draw.rect(self.screen, (255, 255, 255), self.box5, 2)
            pygame.draw.rect(self.screen, (255, 255, 255), self.box6, 2)
            pygame.draw.rect(self.screen, (255, 255, 255), self.box7, 2)

            pygame.draw.rect(self.screen, (255, 255, 255), self.button_pokreni, 2)
            self.screen.blit(self.image_spin, self.button_pokreni)
            font = pygame.font.Font(None, 24)
            self.button_pokreni = pygame.Rect(654, 555, 60, 60)

            # CENTER

            if self.current_image:
                self.screen.blit(self.current_image, self.box7)

            # PLAYER 1

            if self.current_image1:
                self.screen.blit(self.current_image1, self.box1)

            if self.current_image2:
                self.screen.blit(self.current_image2, self.box2)

            if self.current_image3:
                self.screen.blit(self.current_image3, self.box3)

            # PLAYER 2

            if self.current_image4:
                self.screen.blit(self.current_image4, self.box4)

            if self.current_image5:
                self.screen.blit(self.current_image5, self.box5)

            if self.current_image6:
                self.screen.blit(self.current_image6, self.box6)

            pygame.display.update()
            pygame.display.flip()

            self.clock.tick(60)

        pygame.quit()

if __name__ == '__main__':
    level = FirstLevel()
    level.run()

