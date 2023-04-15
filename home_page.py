import time
import pygame
pygame.init()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT_SIZE = 30
GRAY = (128, 128, 128)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


class TextInputBox:
    def __init__(self, x, y, width, label):
        self.label = label
        self.rect = pygame.Rect(x, y, width, FONT_SIZE)
        self.color = GRAY
        self.text = ""
        self.font = pygame.font.SysFont(None, FONT_SIZE)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = GREEN if self.active else GRAY
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    self.active = False
                    self.color = GRAY
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode

    def update(self):
        text_surface = self.font.render(self.text, True, BLACK)
        width = max(self.rect.w, text_surface.get_width()+10)
        self.rect.w = width
        return text_surface

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect, 2)
        label_surface = self.font.render(self.label, True, BLACK)
        surface.blit(label_surface, (self.rect.x - label_surface.get_width() - 10, self.rect.y + 5))
        surface.blit(self.update(), (self.rect.x+5, self.rect.y+5))


class Checkbox:
    def __init__(self, surface, x, y, name, color=(230, 230, 230), caption="", outline_color=(0, 0, 0),
                 check_color=(0, 0, 0), font_size=22, font_color=(0, 0, 0), text_offset=(28, 1)):
        self.surface = surface
        self.x = x
        self.y = y
        self.color = color
        self.caption = caption
        self.oc = outline_color
        self.cc = check_color
        self.fs = font_size
        self.fc = font_color
        self.to = text_offset
        # checkbox object
        self.checkbox_obj = pygame.Rect(self.x, self.y, 12, 12)
        self.checkbox_outline = self.checkbox_obj.copy()
        # variables to test the different states of the checkbox
        self.checked = False
        self.active = False
        self.unchecked = True
        self.click = False
        self.name = name

    def _draw_button_text(self):
        self.font = pygame.font.Font(None, self.fs)
        self.font_surf = self.font.render(self.caption, True, self.fc)
        w, h = self.font.size(self.caption)
        self.font_pos = (self.x + 12 / 2 - w / 2 + self.to[0], self.y + 12 / 2 - h / 2 + self.to[1])
        self.surface.blit(self.font_surf, self.font_pos)

    def render_checkbox(self):
        if self.checked:
            pygame.draw.rect(self.surface, self.color, self.checkbox_obj)
            pygame.draw.rect(self.surface, self.oc, self.checkbox_outline, 1)
            pygame.draw.circle(self.surface, self.cc, (self.x + 6, self.y + 6), 4)

        elif self.unchecked:
            pygame.draw.rect(self.surface, self.color, self.checkbox_obj)
            pygame.draw.rect(self.surface, self.oc, self.checkbox_outline, 1)
        self._draw_button_text()

    def _update(self, event_object):
        x, y = event_object.pos
        # self.x, self.y, 12, 12
        px, py, w, h = self.checkbox_obj  # getting check box dimensions
        if px < x < px + w and px < x < px + w:
            self.active = True
        else:
            self.active = False

    def _mouse_up(self):
            if self.active and not self.checked and self.click:
                    self.checked = True
            elif self.checked:
                self.checked = False
                self.unchecked = True

            if self.click is True and self.active is False:
                if self.checked:
                    self.checked = True
                if self.unchecked:
                    self.unchecked = True
                self.active = False

    def update_checkbox(self, event_object):

        if event_object.type == pygame.MOUSEBUTTONDOWN:
            x = event_object.pos[0]
            y = event_object.pos[1]
            if 200 <= x <= 210 and 502 <= y <= 510 and self.name == "best random":
                self.click = True
            elif 200 <= x <= 210 and 552 <= y <= 560 and self.name == "minimax":
                self.click = True
            elif 200 <= x <= 210 and 602 <= y <= 610 and self.name == "alphabeta":
                self.click = True
            elif 200 <= x <= 210 and 652 <= y <= 660 and self.name == "expectimax":
                self.click = True
            else:
                self.click = False
            # self._mouse_down()
        if event_object.type == pygame.MOUSEBUTTONUP:
            self._mouse_up()
        if event_object.type == pygame.MOUSEMOTION:
            self._update(event_object)

    def is_checked(self):
        if self.checked is True:
            return True
        else:
            return False

    def is_unchecked(self):
        if self.checked is False:
            return True
        return False


def validate_inputs(gameMode, depth):
    if gameMode != 1 and gameMode != 2:
        return False
    if depth < 1 or depth > 9:
        return False
    return True


def write_text():
    texts = []

    # Draw title text
    title_text = pygame.font.SysFont(None, 60).render("4-Connect AI", True, BLACK)
    title_rect = title_text.get_rect(center=(300, 100))
    texts.append((title_text, title_rect))

    title_text = pygame.font.SysFont(None, 25).render("Please enter mode '1' for playing against agent ", True, BLACK)
    title_rect = title_text.get_rect(topleft=(140, 160))
    texts.append((title_text, title_rect))

    title_text = pygame.font.SysFont(None, 25).render("or '2' for playing against another player", True, BLACK)
    title_rect = title_text.get_rect(topleft=(140, 180))
    texts.append((title_text, title_rect))

    title_text = pygame.font.SysFont(None, 25).render("Please enter depth from 1 to 9", True, BLACK)
    title_rect = title_text.get_rect(topleft=(140, 210))
    texts.append((title_text, title_rect))

    title_text = pygame.font.SysFont(None, 25).render("Choose one of the Agents to play", True, BLACK)
    title_rect = title_text.get_rect(topleft=(140, 240))
    texts.append((title_text, title_rect))

    algos = ["best random" , "minimax", "alphabeta", "expectimax"]
    y = 800 // 2 + 98
    title_font = pygame.font.SysFont(None, 30)
    for alg in algos:
        title_text = title_font.render(alg, True, BLACK)
        title_text_rect = title_text.get_rect(topleft=(220, y))
        texts.append((title_text, title_text_rect))
        y += 50
    return texts

def run_menu_screen():
    gameMode = None
    depth = None
    type = None

    screen = pygame.display.set_mode((700, 700))
    pygame.display.set_caption("Connect Four AI")

    # Create text input boxes for Mode and Depth
    mode_input_box = TextInputBox(262, 350, 100, "Mode")
    depth_input_box = TextInputBox(262, 400, 100, "Depth")

    # Create checkboxes for different agents
    best_random_checkbox = Checkbox(screen, 200, 500, "best random")
    minimax_checkbox = Checkbox(screen, 200, 550, "minimax")
    alphabeta_checkbox = Checkbox(screen, 200, 600, "alphabeta")
    expectimax_checkbox = Checkbox(screen, 200, 650, "expectimax")

    # Create start button
    start_button = pygame.Rect(500, 600, 100, 50)

    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            mode_input_box.handle_event(event)
            depth_input_box.handle_event(event)

            best_random_checkbox.update_checkbox(event)
            minimax_checkbox.update_checkbox(event)
            alphabeta_checkbox.update_checkbox(event)
            expectimax_checkbox.update_checkbox(event)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):
                    try:
                        gameMode = int(mode_input_box.text)
                        depth = int(depth_input_box.text)
                    except ValueError:
                        pass

                    if best_random_checkbox.checked:
                        type = "BestRandom"
                    elif minimax_checkbox.checked:
                        type = "MinimaxAgent"
                    elif alphabeta_checkbox.checked:
                        type = "AlphaBetaAgent"
                    elif expectimax_checkbox.checked:
                        type = "ExpectimaxAgent"

                    if validate_inputs(gameMode, depth):
                        return gameMode, depth, type
                    return 1, 3, "MinimaxAgent"

        screen.fill(WHITE)



        # Draw input boxes and checkboxes
        mode_input_box.draw(screen)
        depth_input_box.draw(screen)

        for tuples in write_text():
            screen.blit(tuples[0], tuples[1])

        best_random_checkbox.render_checkbox()
        minimax_checkbox.render_checkbox()
        alphabeta_checkbox.render_checkbox()
        expectimax_checkbox.render_checkbox()

        # Draw start button
        pygame.draw.rect(screen, GRAY, start_button, 2)
        start_text = pygame.font.SysFont(None, 30).render("Continue", True, BLACK)
        start_rect = start_text.get_rect(center=start_button.center)
        screen.blit(start_text, start_rect)

        pygame.display.update()
        clock.tick(30)  # Limit the frame rate to 30 FPS.


