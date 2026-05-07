import pygame

pygame.init()

# Load the game's font (adjust size as needed for a crisp icon)
font = pygame.font.Font('font/font.ttf', 120)

text = "TETRIS"
colors = [
    (255, 0, 0),       # Red
    (255, 127, 0),     # Orange
    (255, 255, 0),     # Yellow
    (0, 255, 0),       # Green
    (0, 0, 255),       # Blue
    (148, 0, 211)      # Purple
]

rendered_letters = []
total_width, max_height = 0, 0

# Render each letter and calculate the total size required for the image
for i, char in enumerate(text):
    rendered = font.render(char, True, colors[i % len(colors)])
    rendered_letters.append(rendered)
    total_width += rendered.get_width()
    max_height = max(max_height, rendered.get_height())

icon_surface = pygame.Surface((total_width, max_height), pygame.SRCALPHA)

current_x = 0
for rendered in rendered_letters:
    icon_surface.blit(rendered, (current_x, 0))
    current_x += rendered.get_width()

pygame.image.save(icon_surface, 'icon.png')
print("Success: 'icon.png' generated!")
pygame.quit()