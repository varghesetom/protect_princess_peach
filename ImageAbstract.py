
from abc import ABC, abstractmethod 
import pygame 

class Image(ABC):

    @abstractmethod
    def stretch(self):
        return pygame.transform.scale(self.image, (40,40))

    @abstractmethod
    def draw_character(self, screen):
        screen.blit(self.stretch(), self.body) 

