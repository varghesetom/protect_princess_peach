import pygame 

class Nintendo:
    def __init__(self,left, top, width, height, speed_min=0, speed_max=0, minsize=0, maxsize=0):
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.body = self.rectFrame()
        self.speed_min = speed_min
        self.speed_max = speed_max
        self.minsize = minsize 
        self.maxsize = maxsize 
        
    def rectFrame(self):
        return pygame.Rect(self.left, self.top, self.width, self.height)
    
    def hitKoopa(self, char_rect_obj, k):
        if char_rect_obj.colliderect(k["rect"]):
            return True
        return False 

    def stretch(self):
        return pygame.transform.scale(self.image, (40,40))
    
    def drawCharacter(self, screen, char_stretched, char_rect):
        screen.blit(char_stretched, char_rect)
    
class Mario(Nintendo):

    def __init__(self,left, top, width, height)
        super().__init__(left, top, width, height)
        self.move_rate = 5
        self.image = pygame.image.load("images/mario.bmp")

class Peach(Nintendo):

    def __init__(self,left, top, width, height,speed_min=0, speed_max=0, minsize=0, maxsize=0):
        super().__init__(left, top, width, height)
        self.image = pygame.image.load("images/peach.bmp") 

    def move(self, window_surface):
        left = random.randint(-10, 10)
        top = random.randint(-10, 10) 
        self.left += left 
        self.top += top 
        self.body.clamp_ip(window_surface.get_rect()) 


if __name__  == "__main__":
    Nintendo()
    Mario(Nintendo)
        
