from pygame import *
window = display.set_mode((700, 500))
display.set_caption('Labyrinth/Maze')
background = transform.scale(image.load('background.jpg'), (700, 500))
clock = time.Clock()
FPS = 360

mixer.init()
mixer.music.load('into-the-jungle-157758.ogg')
mixer.music.play()
mixer.music.set_volume(0.1)

money = mixer.Sound('money.ogg')
kick = mixer.Sound('kick.ogg')

font.init()
font = font.SysFont('Arial', 70)
win = font.render('YOU WIN', True, (0,255,0))
lose = font.render('YOU LOSE', True, (255,0,0))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 595:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 395:
            self.rect.y += self.speed
        
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < 595:
            self.rect.x += self.speed
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 395:
            self.rect.y += self.speed
    

class Monster(GameSprite): 
    direction = 'left'
    def update(self):
        if self.rect.x <= 405:
            self.direction = 'left'
        if self.rect.x >= 540:
            self.direction = 'right'
        if self.direction == 'left':
            self.rect.x += self.speed
        if self.direction == 'right':
            self.rect.x -= self.speed

class Wall(sprite.Sprite):
    def __init__(self, r,g,b,x,y,w,h):
        super().__init__()
        self.image = Surface((w, h))
        self.image.fill((r, b, g))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))



player = Player('Indiana.png', 25, 300, 2)
monster = Monster('spider1.png', 500, 280, 1)
monster2 = Monster('spider1.png', 500, 130, 1)
final = GameSprite('treasure.png', 500, 350, 0)
w1 = Wall(205, 150, 255, 100, 20, 500, 10)
w2 = Wall(205, 150, 255, 100, 20, 10, 300)
w3 = Wall(205, 150, 255, 100, 420, 10, 100)
w4 = Wall(205, 150, 255, 200, 120, 10, 500)
w5 = Wall(205, 150, 255, 300, 20, 10, 370)
w6 = Wall(205, 150, 255, 400, 120, 10, 500)
w7 = Wall(205, 150, 255, 600, 20, 10, 500)


game = True
finish = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        window.blit(background, (0, 0))
        if sprite.collide_rect(player, monster) or sprite.collide_rect(player, monster2) or sprite.collide_rect(player, w1) or sprite.collide_rect(player, w2) or sprite.collide_rect(player, w3) or sprite.collide_rect(player, w4) or sprite.collide_rect(player, w5) or sprite.collide_rect(player, w6) or sprite.collide_rect(player, w7):
            finish = True
            kick.play()
            window.blit(lose, (200, 200))
        if sprite.collide_rect(player, final):
            finish = True
            money.play()
            window.blit(win, (200, 200))

        player.reset()
        player.update()
        monster.reset()
        monster.update()
        monster2.reset()
        monster2.update()
        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        w5.draw_wall()
        w6.draw_wall()
        w7.draw_wall()
        final.reset()

    clock.tick(FPS)
    display.update()