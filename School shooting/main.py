import pygame

width, height = 700, 500

window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Shooting")
back = pygame.transform.scale(pygame.image.load("galaxy.jpg"), (700,500))


game = True
clock = pygame.time.Clock()

from time import sleep
class GameSprite(pygame.sprite.Sprite):
    def __init__(self, image, x, y, speed, size_x, size_y ):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(image), (size_x, size_y))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

player = GameSprite('rocket.png', 220, 390, 4, 65, 100)

pygame.mixer.init()
pygame.mixer.music.load('Deadlocked.mp3')
pygame.mixer.music.play()
speed=3

while game:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False
    key=pygame.key.get_pressed()
    if key[pygame.K_LEFT] and player.rect.x>0:
        player.rect.x-=speed
    if key[pygame.K_RIGHT] and player.rect.x<635:
        player.rect.x+=speed
    if key[pygame.K_DOWN] and player.rect.y<390:
        player.rect.y+=speed
    if key[pygame.K_UP] and player.rect.y>320:
        player.rect.y-=speed
    if key[pygame.K_w]:
        speed=6
    if key[pygame.K_q]:
        speed=3


    window.blit(back,(0, 0))
    player.draw()
    pygame.display.update()
    clock.tick(60)





