
import pygame, random, math 

class Nintendo:

    def __init__(self,left, top, width, height, speed_min=0, speed_max=0, minsize=0, maxsize=0):
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.speed_min = speed_min
        self.speed_max = speed_max
        self.minsize = minsize 
        self.maxsize = maxsize 
        self.body = self.rectFrame()
        
    def rectFrame(self):
        return pygame.Rect(self.left, self.top, self.width, self.height)
    
    def hit_koopa(self, koopa):
        if self.body.colliderect(koopa.body):
            return True
        return False 

    def _stretch(self):
        return pygame.transform.scale(self.image, (40,40))
    
    def draw_character(self, screen):
        screen.blit(self._stretch(), self.body) 


class Mario(Nintendo):

    def __init__(self,left, top, width, height):
        super().__init__(left, top, width, height)
        self.move_rate = 5
        self.pause = False 
        self.move_left = False 
        self.move_right = False 
        self.move_up = False 
        self.move_down = False 
        self.image = pygame.image.load("images/mario.bmp")

    def move_and_attack(self, window_surface, koopa_army): 
        if not self.pause: 
            if self.move_left:
                self.body.move_ip(-1 * self.move_rate, 0)
            if self.move_right: 
                self.body.move_ip(self.move_rate, 0) 
            if self.move_up:
                self.body.move_ip(0, -1 * self.move_rate) 
            if self.move_down:
                self.body.move_ip(0, self.move_rate) 
        self.body.clamp_ip(window_surface.get_rect()) 
        self._attack_koopa_army(koopa_army) 

    def _attack_koopa_army(self, koopa_army):
        for k in koopa_army.koopas[:]:   # Use [:] to create a copy so we can update + remove from actual array while iterating  
            if self.hit_koopa(k):
                koopa_army.koopas.remove(k) 


class Peach(Nintendo):

    def __init__(self,left, top, width, height,speed_min=0, speed_max=0, minsize=0, maxsize=0):
        super().__init__(left, top, width, height)
        self.image = pygame.image.load("images/peach.bmp") 

    def move(self, window_surface):
        self.body.left += random.randint(-1, 1)
        self.body.top += random.randint(-1, 1)
        self.body.clamp_ip(window_surface.get_rect()) 

    def got_captured_by(self, koopa_army):
        for k in koopa_army.koopas[:]:
            return True if self.hit_koopa(k) else False 
            

class Koopa:

    min_size=30
    max_size=40 
    min_speed=1 
    max_speed=5

    def __init__(self, window_surface):
        self.size = random.randint(self.min_size, self.max_size) 
        self.image = pygame.image.load("images/koopa.bmp") 
        self.body = self._generate_body(window_surface) 

    def _generate_body(self, window_surface): 
        return pygame.Rect(random.randint(0, window_surface.get_width()), random.randint(0, window_surface.get_height() // 3), self.size, self.size)  

    def draw_character(self, screen):
        screen.blit(self._stretch(), self.body) 

    def _stretch(self):
        return pygame.transform.scale(self.image, (40,40))

    def move_towards(self, peach):
        dx, dy = self.body.x - peach.body.x, self.body.y - peach.body.y
        try: 
            dist = math.hypot(dx, dy)      # euclidean distance  
            dx, dy = dx/dist, dy/dist      # normalize distance magnitude so koopas won't move super fast 
        except ZeroDivisionError:
            pass 
        self.body.x -= dx * random.randint(self.min_speed, self.max_speed) 
        self.body.y -= dy * random.randint(self.min_speed, self.max_speed)


class KoopaArmy: 

    bad_rate = 35 

    def __init__(self): 
        self.koopas = [] 

    def move(self, peach):
        for k in self.koopas:
            k.move_towards(peach) 

    def generate_koopa(self, window_surface):
        self.koopas.append(Koopa(window_surface)) 

    def draw_army(self, window_surface):
        for k in self.koopas:
            k.draw_character(window_surface) 

    
    
