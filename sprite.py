import pygame
from settings import *

pygame.font.init()


class Tile(pygame.sprite.Sprite):
    def __init__(self, game, x, y, text):
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface((tiles_size, tiles_size))
        self.x, self.y = x, y
        self.text = text
        self.rect = self.image.get_rect()

        if self.text != "empty":
            self.font = pygame.font.SysFont("Consolas", 70)
            font_surface = self.font.render(self.text, True, num_color)
            self.image.fill(tile_color)
            self.font_size = self.font.size(self.text)
            text_x = (tiles_size / 2) - self.font_size[0] / 2
            text_y = (tiles_size / 2) - self.font_size[1] / 2
            self.image.blit(font_surface,(text_x, text_y))

    def update(self):
        self.rect.x = self.x * tiles_size
        self.rect.y = self.y * tiles_size

    def click(self, mouse_x, mouse_y):
        return self.rect.left <= mouse_x <= self.rect.right and self.rect.top <= mouse_y <= self.rect.bottom

    def right(self):
        return self.rect.x + tiles_size < grid_size * tiles_size

    def left(self):
        return self.rect.x - tiles_size >= 0

    def up(self):
        return self.rect.y - tiles_size >= 0

    def down(self):
        return self.rect.y + tiles_size < grid_size * tiles_size

class UIElement:
    def __init__(self, x, y, text):
        self.x, self.y = x, y
        self.text = text

    def draw(self, screen):
        font = pygame.font.SysFont("Consolas", 20)
        text = font.render(self.text, True, white)
        screen.blit(text, (self.x, self.y))

class Button:
    def __init__(self, x, y, width, height, text, colour, text_colour):
        self.colour, self.text_colour = colour, text_colour
        self.width, self.height = width, height
        self.x, self.y = x, y
        self.text = text

    def draw(self, screen):
        pygame.draw.rect(screen, self.colour, (self.x, self.y, self.width, self.height))
        font = pygame.font.SysFont("Consolas", 20)
        text = font.render(self.text, True, self.text_colour)
        self.font_size = font.size(self.text)
        draw_x = self.x + (self.width / 2) - self.font_size[0] / 2
        draw_y = self.y + (self.height / 2) - self.font_size[1] / 2
        screen.blit(text, (draw_x, draw_y))

    def click(self, mouse_x, mouse_y):
        return self.x <= mouse_x <= self.x + self.width and self.y <= mouse_y <= self.y + self.height

