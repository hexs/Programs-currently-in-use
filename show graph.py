import json
import pygame
import pygame_gui
import sys
import numpy as np


def surface(w, h):
    numpy_array = np.full((h, w, 3), (200, 200, 200), dtype=np.uint8)
    image_surface = pygame.surfarray.make_surface(numpy_array.swapaxes(0, 1))
    image_surface = image_surface.convert()
    return image_surface


# Initialize Pygame
pygame.init()

# Set up the screen
width, height = 920, 740
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Graph Display")
surf = surface(900, 600)

try:
    with open('program name.json', encoding='utf-8') as f:
        string = (f.read())
    program_name = json.loads(string)
except:
    program_name = {'': 0}
manager = pygame_gui.UIManager((width, height))
clock = pygame.time.Clock()
options_list = list(program_name.keys())
options_list.sort(key=str.lower)
pygame_gui.elements.UIDropDownMenu(options_list, options_list[0], pygame.Rect(10, 10, 500, 30), manager)

# Set up colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Main loop
running = True
while running:
    time_delta = clock.tick(60) / 1000.0
    for event in pygame.event.get():
        manager.process_events(event)
        if event.type == pygame.QUIT:
            running = False

    font = pygame.font.Font('freesansbold.ttf', 24)

    for i,h in enumerate(range(8, 21)):
        ax = i * 75
        text = font.render(f'{h}', True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.centerx = ax
        surf.blit(text, textRect)
        pygame.draw.circle(surf, (255, 0, 0), (ax, 40),3)

    pygame.draw.rect(surf, (255, 0, 0), pygame.Rect(30, 50, 60, 10))

    display.fill(WHITE)
    display.blit(surf, (10, 100))
    manager.update(time_delta)
    manager.draw_ui(display)
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
