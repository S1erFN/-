#Создай собственный Шутер!

from pygame import *
from random import randint
window = display.set_mode((1000,700))
display.set_caption("Шутер")
back = transform.scale(image.load("Космос.png"),(1000,700))
win = 0
lost = 0
font.init()
font = font.Font(None, 40)
class GameSprite(sprite.Sprite):
    def  __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_LEFT] and self.rect.x >0:
            self.rect.x -= self.speed
        if keys_pressed[K_RIGHT] and self.rect.x <900:
            self.rect.x += self.speed
    def fire(self):
        bullet = Bullet('bullet.png',self.rect.centerx,self.rect.top,9)
        bullets.add(bullet)

bullets = sprite.Group()

class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y<0:
            self.kill()
    
class Enemy(GameSprite):
    def update(self):
        global lost
        self.rect.y += self.speed
        if self.rect.y >700:
            self.rect.y = -100
            self.rect.x = randint(0,1000)
            self.speed = randint(2,5)
            lost +=1

ufo1=sprite.Group()
for i in range(5):
    sssr2 = Enemy("ufo.png",randint(0,1000),0,randint(2,4))
    ufo1.add(sssr2)

ufo2=sprite.Group()
for i in range(3):
    sssr1 = Enemy("asteroid.png",randint(0,1000),0,randint(2,4))
    ufo2.add(sssr1)

clock=time.Clock()
FPS= 70

s1 = Player('rocket.png',270,600,15)

game = True
finish=False
while game:
    if not finish:


        window.blit(back,(0,0))
        ufo1.update()
        ufo1.draw(window)
        ufo2.update()
        ufo2.draw(window)
        bullets.update()
        bullets.draw(window)
        s1.reset()
        s1.update()
        ler=sprite.groupcollide(ufo1,bullets,True,True)
        for l in ler:
            sssr2 = Enemy("ufo.png",randint(0,1000),-50,randint(2,4))
            ufo1.add(sssr2)
           

        

        
        # for o in ler1:
        #     sssr1 = Enemy("asteroid.png",randint(0,1000),-50,randint(2,4))
        #     ufo2.add(sssr1)
        if sprite.groupcollide(ufo1, bullets, True, True):
            win = win + 1
            window.blit(text_win, (10, 60))
        if sprite.groupcollide(ufo2, bullets, False, True):
            pass
        if win == 20:
            finish = True
            text = font.render("Вы Выиграли", True, (235, 205, 0))
            window.blit(text, (275,150))
        if lost > 9 or sprite.spritecollide(s1, ufo1, False):
            finish = True
            text = font.render("Вы Проиграли", True, (235, 205, 0))
            window.blit(text, (275,150))
        if lost > 9 or sprite.spritecollide(s1, ufo2, False):
            finish = True
            text = font.render("Вы Проиграли", True, (235, 205, 0))
            window.blit(text, (275,150))
    for e in event.get():
        if e.type == QUIT:
        
            game = False
        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                s1.fire()



        
    display.update()
    clock.tick(FPS)      
        