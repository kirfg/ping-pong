from pygame import *


window = display.set_mode((700,500))
display.set_caption('ping pong')
background = transform.scale(image.load('brawl.jpg'),(700,500))

clock = time.Clock()
FPS = 60
class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_speed,player_x,player_y,w,h):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(w,h))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y 
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))
class Player(GameSprite):
    def update_l(self):
        keys_pressed=key.get_pressed()        
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 635:
            self.rect.y += self.speed
        if self.rect.y >=430:
            self.rect.y -= self.speed
    def update_r(self):
        keys_pressed=key.get_pressed()        
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 635:
            self.rect.y += self.speed
        if self.rect.y >=430:
            self.rect.y -= self.speed

ping =Player('images.png',10,610,40,65,80)
pong =Player('images.png',10,30,40,65,80)
finish =False
game =True

while game:
    if finish != True:

        window.blit(background,(0,0))
        ping.reset()
        ping.update_r()
        pong.reset()
        pong.update_l()






    for e in event.get():
        if e.type == QUIT:
            game = False

                
    
    
       
    
    display.update()
    clock.tick(FPS)









