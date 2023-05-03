from tkinter import messagebox
from tkinter import ttk
import webview
import pygame
import pygame.mixer
import tkinter as tk
from first_game import FirstLevel


pygame.init()
pygame.mixer.init()
pygame.display.init()
pygame.font.init()

#melodija
melody = pygame.mixer.Sound("Sounds/isolee_pisco.mp3")
melody.play()

WIDTH_SCREEN = 800
HEIGHT_SCREEN = 600

first_screen = pygame.display.set_mode((WIDTH_SCREEN, HEIGHT_SCREEN))

pygame.display.set_caption("PyRoyale")

icon = pygame.image.load('Images/icon.png')
pygame.display.set_icon(icon)

# boje
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
BRIGHT_RED = (255, 0, 0)
ORANGE = (255, 165, 0)
GRAY = (102, 128, 109)
GRAY2 = (115, 115, 115)
GREEN = (22, 201, 70)
LIGHT_BLUE = (22, 134, 168)

# fontovi
font1 = 'Fonts/SedgwickAveDisplay.ttf'

FPS = 60
clock = pygame.time.Clock()

first_screen.fill(WHITE)

font = pygame.font.Font(None, 100)
text = font.render("PyRoyale", True, BLACK)
text_rect = text.get_rect(center=(WIDTH_SCREEN // 2, HEIGHT_SCREEN // 3))
first_screen.blit(text, text_rect)

button1 = pygame.draw.rect(
    first_screen, RED, pygame.Rect(250, 300, 300, 50))
button2 = pygame.draw.rect(
    first_screen, RED, pygame.Rect(250, 360, 300, 50))
button3 = pygame.draw.rect(
    first_screen, RED, pygame.Rect(250, 420, 300, 50))
button4 = pygame.draw.rect(
    first_screen, RED, pygame.Rect(250, 480, 300, 50))


font = pygame.font.Font(None, 48)
text_play_game = font.render("Play game", True, (255, 255, 255))
text_language = font.render("Language", True, (255, 255, 255))
text_tutorial = font.render("Tutorial", True, (255, 255, 255))
text_exit = font.render("Exit", True, (255, 255, 255))

text_button1 = text_play_game.get_rect(center=button1.center)
text_button2 = text_language.get_rect(center=button2.center)
text_button3 = text_tutorial.get_rect(center=button3.center)
text_button4 = text_exit.get_rect(center=button4.center)

first_screen.blit(text_play_game, text_button1)
first_screen.blit(text_language, text_button2)
first_screen.blit(text_tutorial, text_button3)
first_screen.blit(text_exit, text_button4)

font_creator = pygame.font.Font(None, 18)
creator_text = font_creator.render('Kreirao Josif Vukićević', True, (200, 0, 0))
first_screen.blit(creator_text, (first_screen.get_width() - creator_text.get_width() - 10, first_screen.get_height() - creator_text.get_height() - 10))

#######################
pygame.display.flip()
pygame.display.update()
#######################

def language():
    print("Language prozor pokrenut.")

    def potvrdi():
        selected_language = combo_box.get()
        if selected_language == "Izaberite jezik":
            messagebox.showinfo("Greska!", "Niste odabrali jezik!")
        else:
            print("Izabrani jezik:", selected_language)
            messagebox.showinfo("Potvrda", f"Izabrali ste jezik: {selected_language}")


    def vrati_se_nazad():
        root.destroy()

    # Kreiranje glavnog prozora
    root = tk.Tk()

    ################### STIL ZA DUGME ###################

    style = ttk.Style()

    style.configure('my.TButton',
                    borderwidth=2,  # bordure
                    background='#080000', # pozadina
                    foreground='#e61e24',  # boja teksta
                    font=('Arial', 12, "bold"),
                    relief='flat')

    root.title("Language")
    root.geometry("300x200")
    root.configure(bg="white")
    root.resizable(False, False)
    root.iconbitmap('Images/icon.ico')

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width = root.winfo_width()
    window_height = root.winfo_height()
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    root.geometry(f"+{x}+{y}")

    # Kreiranje ComboBox-a za izbor jezika
    languages = ["English", "Français", "Deutsch", "Español", "Srpski"]
    combo_box = ttk.Combobox(root, values=languages, state="readonly")
    combo_box.set("Izaberite jezik")
    combo_box.pack(pady=20)

    btn_potvrdi = ttk.Button(root, text="Potvrdi", command=potvrdi, style='my.TButton')
    btn_potvrdi.pack()

    btn_vrati_se_nazad = ttk.Button(root, text="Vrati se nazad", command=vrati_se_nazad)
    btn_vrati_se_nazad.pack(pady=10)

    root.mainloop()


def tutorial():
    print("Tutorial prozor pokrenut.")

    def odaberi_nivo(nivo):
        print("Tutorial za nivo:", nivo)
        if nivo == 1:
            webview.create_window('Level 1', 'html/first_level.html')
            webview.start()
        elif nivo == 2:
            webview.create_window('Level 2', 'html/second_level.html')
            webview.start()
        elif nivo == 3:
            webview.create_window('Level 3', 'html/third_level.html')
            webview.start()
        elif nivo == 4:
            webview.create_window('Level 4', 'html/fourth_level.html')
            webview.start()
        elif nivo == 5:
            webview.create_window('Level 5', 'html/fifth_level.html')
            webview.start()
        elif nivo == 6:
            webview.create_window('Level 6', 'html/sixth_level.html')
            webview.start()


    def otvori_html():
        webview.create_window('Tutorial', 'html/tutorial.html')
        webview.start()

    prozor = tk.Tk()
    prozor.title("Tutorial - Odaberite nivo")
    prozor.geometry("400x150")
    prozor.resizable(False, False)
    prozor.iconbitmap('Images/icon.ico')

    screen_width = prozor.winfo_screenwidth()
    screen_height = prozor.winfo_screenheight()
    window_width = prozor.winfo_width()
    window_height = prozor.winfo_height()
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    prozor.geometry(f"+{x}+{y}")

    lijevi_okvir = tk.Frame(prozor)
    lijevi_okvir.pack(side=tk.LEFT, padx=10)

    # Kreiranje dugmeta za nivoe 1, 2 i 3
    nivo1_dugme = tk.Button(lijevi_okvir, text="Level 1", command=lambda: odaberi_nivo(1), font=("Arial", 12, "bold"),
                                                                            bg="red", fg="white", bd=2)
    nivo1_dugme.pack(pady=5)

    nivo2_dugme = tk.Button(lijevi_okvir, text="Level 2", command=lambda: odaberi_nivo(2), font=("Arial", 12, "bold"),
                                                                            bg="red", fg="white", bd=2)
    nivo2_dugme.pack(pady=5)

    nivo3_dugme = tk.Button(lijevi_okvir, text="Level 3", command=lambda: odaberi_nivo(3), font=("Arial", 12, "bold"),
                                                                            bg="red", fg="white", bd=2)
    nivo3_dugme.pack(pady=5)

    desni_okvir = tk.Frame(prozor)
    desni_okvir.pack(side=tk.RIGHT, padx=10)

    # Kreiranje dugmeta za nivoe 4, 5 i 6
    nivo4_dugme = tk.Button(desni_okvir, text="Level 4", command=lambda: odaberi_nivo(4), font=("Arial", 12, "bold"),
                                                                            bg="red", fg="white", bd=2)
    nivo4_dugme.pack(pady=5)

    nivo5_dugme = tk.Button(desni_okvir, text="Level 5", command=lambda: odaberi_nivo(5), font=("Arial", 12, "bold"),
                                                                            bg="red", fg="white", bd=2)
    nivo5_dugme.pack(pady=5)

    nivo6_dugme = tk.Button(desni_okvir, text="Level 6", command=lambda: odaberi_nivo(6), font=("Arial", 12, "bold"),
                                                                            bg="red", fg="white", bd=2)
    nivo6_dugme.pack(pady=5)

    tutorial_dugme = tk.Button(prozor, text="Tutorial", command=otvori_html, font=("Arial", 12, "bold"), bg="Red",
                                                                fg="white", bd=2, width=13, height=50)
    tutorial_dugme.pack(pady=61)

    prozor.mainloop()

def exit():
    print("Izlazak iz igre")
    pygame.quit()
    quit()

def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button1.collidepoint(event.pos):
                    print("Pritisnuto dugme play game!")
                    first_level = FirstLevel()
                    first_level.run()
                    melody.stop()
                    running = False

                elif button2.collidepoint(event.pos):
                    print("Pritisnuto dugme language!")
                    language()
                elif button3.collidepoint(event.pos):
                    print("Pritisnuto dugme tutorial!")
                    tutorial()
                elif button4.collidepoint(event.pos):
                    print("Pritisnuto dugme exit!")
                    exit()


        clock.tick(FPS)
        if pygame.display.get_init():
            pygame.display.flip()

    pygame.mixer.quit()
    pygame.quit()

if __name__ == "__main__":
    main()
