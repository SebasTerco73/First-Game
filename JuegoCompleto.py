import pygame, random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
CANT_METEORS = 7

pygame.init()
pygame.mixer.init() # Permite cargar sonidos
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Shooter")
clock = pygame.time.Clock()

# Marcador
def draw_text(surface, text, size, x, y):
    font = pygame.font.SysFont("serif",size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x,y)
    surface.blit(text_surface,text_rect)

def draw_shield_bar(surface, x,y, percentage):
        BAR_LENGHT = 100
        BAR_HEIGHT = 10
        fill = percentage
        border = pygame.Rect(x,y,BAR_LENGHT,BAR_HEIGHT)
        fill = pygame.Rect(x,y, fill, BAR_HEIGHT)
        pygame.draw.rect(surface, GREEN, fill)
        pygame.draw.rect(surface, WHITE, border, 2)

def create_meteor():
    meteor = Meteor()
    all_sprites.add(meteor)
    meteor_list.add(meteor)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("/assets/player.png").convert_alpha()
        # self.image = pygame.transform.scale(self.image, (100, 100))
        self.image
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.bottom = SCREEN_HEIGHT - 10
        self.speed_x = 10
        self.shield = 100 # Vida/Escudo
        
    def update(self):
        self.speed_x = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speed_x = -5
        if keystate[pygame.K_RIGHT]:
            self.speed_x = 5
        self.rect.x += self.speed_x
        # Borde derecho y borde izquierdo
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.left < 0:
            self.rect.left = 0    

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)
        laser_sound.play()
        
class Meteor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # self.image = pygame.image.load("/assets/meteorGrey_med1.png").convert_alpha()
        self.image = random.choice(meteor_images)
        # self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
        # Que aparezcan antes de la pantalla (simulan estar cayendo)
        self.rect.y = random.randrange(-140, -100)
        # Distintas velocidades
        self.speedy = random.randrange(1,8)
        self.speedx = random.randrange(-5,5)

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.top > SCREEN_HEIGHT +10 or self.rect.left < -40 or self.rect.right > SCREEN_WIDTH +40:
            self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
        # Que aparezcan antes de la pantalla (simulan estar cayendo)
            self.rect.y = random.randrange(-100, -40)
        # Distintas velocidades
            self.speedy = random.randrange(1,10)

class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y ):
        super().__init__()
        self.image = pygame.image.load("/assets/laser1.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.y = y
        # Centro real del objeto
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        # Eliminar las instancias del objeto de todas las listas cuando sobrepasa el borde superior
        if self.rect.bottom < 0:
            self.kill()

class Explosion(pygame.sprite.Sprite):
    def __init__(self, center):
        super().__init__()
        self.image = explosion_anim[0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0 # Selector de imagen
        self.last_update = pygame.time.get_ticks() 
        self.frame_rate = 50 # Velocidad de la explosion

    def update(self):
        now = pygame.time.get_ticks()
        # Si ha pasado más tiempo que frame_rate desde el último cambio de imagen, 
        # entonces es hora de avanzar al siguiente frame.
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(explosion_anim):
                self.kill()
            else:
                center = self.rect.center
                self.image = explosion_anim[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center

def show_go_screen():
    screen.blit(background,[0,0])
    draw_text(screen, "SHOOTER", 65, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4)
    draw_text(screen, "Instrucciones van aquí", 27, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    draw_text(screen, "Press Enter", 20, SCREEN_WIDTH // 2, SCREEN_HEIGHT * 3/4)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RETURN:  # Verifica si la tecla soltada fue Enter
                    waiting = False

meteor_images = []
meteor_list = ["/assets/meteorGrey_big1.png", "/assets/meteorGrey_big2.png", "/assets/meteorGrey_big3.png", "/assets/meteorGrey_big4.png",
				"/assets/meteorGrey_med1.png", "/assets/meteorGrey_med2.png", "/assets/meteorGrey_small1.png", "/assets/meteorGrey_small2.png",
				"/assets/meteorGrey_tiny1.png", "/assets/meteorGrey_tiny2.png"]

for img in meteor_list:
    meteor_images.append(pygame.image.load(img).convert_alpha())

# Animacion explosiones
explosion_anim = []
for i in range(9):
    file = "/assets/regularExplosion0{}.png".format(i)
    img = pygame.image.load(file).convert_alpha()
    img_scale = pygame.transform.scale(img,(70,70))
    explosion_anim.append(img_scale)

# Imagen de fondo
background = pygame.image.load("/assets/background.png").convert_alpha()

# Sonidos
laser_sound = pygame.mixer.Sound("/assets/laser5.ogg")
explosion_sound = pygame.mixer.Sound("/assets/explosion.wav")
pygame.mixer.music.load("/assets/music.ogg")
pygame.mixer.music.set_volume(0.2)

#Reproducir musica, y que se repita infinitamente. Si el valor es por ejemplo 2, se reproduce 2 veces
pygame.mixer.music.play(loops=-1)

### Game over
game_over = True
running = True
while running:
    if game_over:
        show_go_screen()
        game_over = False
        meteor_list = pygame.sprite.Group()
        all_sprites = pygame.sprite.Group()
        bullets = pygame.sprite.Group()
        for i in range(CANT_METEORS):
            create_meteor()
        player = Player()
        all_sprites.add(player)
        score = 0

    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()

    all_sprites.update()

    # Colisiones (meteoro/laser)
    # Chequea las colisines de 2 grupos
    # True desaparece los meteoros, True desaparece las balas
    hits = pygame.sprite.groupcollide(meteor_list, bullets, True, True)
    for hit in hits:
        score +=10
        explosion_sound.play()
        explosion = Explosion(hit.rect.center)
        all_sprites.add(explosion)
        create_meteor()
    # Colisiones (jugador/meteoro)
    # True, el objeto con el que colisiona desaparece
    hits = pygame.sprite.spritecollide(player, meteor_list, True)
    for hit in hits:
        player.shield -= 10
        create_meteor()
        if player.shield <= 0:  
            game_over = True
        
    #Imagen de fondo, y donde empieza
    screen.blit(background,[0,0])
    all_sprites.draw(screen)

    # Marcador
    draw_text(screen, str(score), 25, SCREEN_WIDTH // 2, 10)
    # Escudo
    draw_shield_bar(screen, 5, 5, player.shield)
    pygame.display.flip()

pygame.quit()

