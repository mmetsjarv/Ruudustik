import pygame

WIDTH, HEIGHT = 640, 480


def draw_grid(screen, cell_size, rows, cols, line_color):
    for row in range(rows + 1):
        y = row * cell_size
        pygame.draw.line(screen, line_color, (0, y), (cols * cell_size, y))

    for col in range(cols + 1):
        x = col * cell_size
        pygame.draw.line(screen, line_color, (x, 0), (x, rows * cell_size))


def menu(screen):
    pygame.font.init()
    font = pygame.font.SysFont(None, 32)

    cell_size = 20
    rows = 10
    cols = 10
    color = [0, 255, 0]

    selected = 0  # 0 cell, 1 rows, 2 cols, 3 color

    running = True
    while running:
        screen.fill((30, 30, 30))

        texts = [
            f"Ruudu suurus: {cell_size}",
            f"Read: {rows}",
            f"Veerud: {cols}",
            f"Värv (G): {color[1]}  (↑↓ muudab)"
        ]

        for i, text in enumerate(texts):
            col = (255, 255, 0) if i == selected else (200, 200, 200)
            img = font.render(text, True, col)
            screen.blit(img, (50, 50 + i * 40))

        hint = font.render("ENTER = start | TAB = next | ↑↓ = change", True, (150, 150, 150))
        screen.blit(hint, (50, 250))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    running = False

                elif event.key == pygame.K_TAB:
                    selected = (selected + 1) % 4

                elif event.key == pygame.K_UP:
                    if selected == 0:
                        cell_size += 5
                    elif selected == 1:
                        rows += 1
                    elif selected == 2:
                        cols += 1
                    elif selected == 3:
                        color[1] = min(255, color[1] + 10)

                elif event.key == pygame.K_DOWN:
                    if selected == 0:
                        cell_size = max(5, cell_size - 5)
                    elif selected == 1:
                        rows = max(1, rows - 1)
                    elif selected == 2:
                        cols = max(1, cols - 1)
                    elif selected == 3:
                        color[1] = max(0, color[1] - 10)

    return cell_size, rows, cols, tuple(color)


def run_grid_app(cell_size, rows, cols, line_color):
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Ruudustik - Metsjärv")

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 102, 51))
        draw_grid(screen, cell_size, rows, cols, line_color)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    settings = menu(screen)

    if settings:
        run_grid_app(*settings)