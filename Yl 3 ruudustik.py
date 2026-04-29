import pygame
import sys

def joonista_ruudustik(read, veerud, ruudu_suurus, joone_varv):
    # Fikseeritud akna suurus
    WIDTH, HEIGHT = 640, 480
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Ruudustik - Metsjärv")

    # Loome ruudud
    cells = []
    for r in range(read):
        for v in range(veerud):
            x = v * ruudu_suurus
            y = r * ruudu_suurus
            if x < WIDTH and y < HEIGHT:
                cells.append((x, y))

    current_cell = 0
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  # Naaseb seadete aknasse

        screen.fill((0, 102, 51))  # Taustavärv

        # Joonistame ruudud
        for i in range(min(current_cell, len(cells))):
            x, y = cells[i]
            rect = pygame.Rect(x, y, ruudu_suurus, ruudu_suurus)
            pygame.draw.rect(screen, joone_varv, rect, 1)

        if current_cell < len(cells):
            current_cell += 5

        pygame.display.flip()
        clock.tick(60)


def seadete_aken():
    pygame.init()
    # Seadete akna suurus
    screen = pygame.display.set_mode((450, 350))
    pygame.display.set_caption("Ruudustiku seadistamine")
    
    # MUUDATUS: Font on nüüd Comic Sans
    try:
        font = pygame.font.SysFont("Comic Sans MS", 18)
    except:
        font = pygame.font.SysFont("Arial", 18) # Varufont, kui süsteemis Comic Sansi pole

    # Sinu soovitud roheline värv
    roheline = (0, 102, 51)

    # Algväärtused
    inputs = {
        "Ruudu suurus (px)": "30",
        "Ridade arv": "10",
        "Veergude arv": "15",
        "Varv R,G,B": "255,255,255"
    }
    keys = list(inputs.keys())
    active_idx = 0

    running = True
    while running:
        screen.fill((40, 44, 52)) # Tume taust, et tekst välja paistaks

        # Juhis (Nüüd roheline)
        info = font.render("TAB: liigu | BACKSPACE: kustuta | ENTER: käivita", True, roheline)
        screen.blit(info, (20, 20))

        for i, key in enumerate(keys):
            # Aktiivne väli on paksemalt/eredamalt märgitud (aga ikka roheline)
            label_color = (0, 200, 100) if i == active_idx else roheline

            # Sildi joonistamine
            txt = font.render(f"{key}:", True, label_color)
            screen.blit(txt, (30, 80 + i * 50))

            # Sisestuskasti taust ja tekst
            pygame.draw.rect(screen, (33, 37, 43), (220, 75 + i * 50, 180, 35))
            val_txt = font.render(inputs[key], True, (224, 108, 117)) # Sisestatud tekst on punakas
            screen.blit(val_txt, (230, 80 + i * 50))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    try:
                        s = int(inputs["Ruudu suurus (px)"])
                        r = int(inputs["Ridade arv"])
                        v = int(inputs["Veergude arv"])
                        c = tuple(map(int, inputs["Varv R,G,B"].replace(" ", "").split(',')))

                        # Käivitame põhiakna
                        joonista_ruudustik(r, v, s, c)

                        # Lähtestame seadete akna ekraani suuruse
                        screen = pygame.display.set_mode((450, 350))
                    except Exception as e:
                        print(f"Viga sisestuses: {e}")

                elif event.key == pygame.K_TAB:
                    active_idx = (active_idx + 1) % len(keys)
                elif event.key == pygame.K_BACKSPACE:
                    inputs[keys[active_idx]] = inputs[keys[active_idx]][:-1]
                else:
                    if event.unicode.isprintable() and len(inputs[keys[active_idx]]) < 15:
                        inputs[keys[active_idx]] += event.unicode

        pygame.display.flip()

if __name__ == "__main__":
    seadete_aken()
