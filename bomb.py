from ui import *


class Bomb:
    b_count = 0
    e_count = 0
    cooldown_start = pygame.time.get_ticks()
    bomb_ready = True

    def __init__(self, music, bomb_x, bomb_y, player, enemies_list):
        self.music = music
        self.bomb_x = bomb_x
        self.bomb_y = bomb_y
        self.player = player
        self.enemies_list = enemies_list
        self.exploded = False
        self.e_stop = False
        self.start = pygame.time.get_ticks()

    def bomb_animation(self):
        animation = [pygame.image.load('graphics/bomb/1.png'), pygame.image.load('graphics/bomb/2.png'),
                     pygame.image.load('graphics/bomb/3.png'), pygame.image.load('graphics/bomb/4.png'),
                     pygame.image.load('graphics/bomb/5.png'), pygame.image.load('graphics/bomb/6.png')]

        if self.b_count + 1 >= 18:
            self.b_count = 0

        screen.blit(animation[self.b_count // 3], (self.bomb_x, self.bomb_y))
        self.b_count += 1

    def explosion_animation(self):

        animation = []

        for num in range(1, 13):
            image = pygame.image.load('graphics/bomb/explosion' + str(num) + '.png')
            image = pygame.transform.scale(image, (256, 256))
            animation.append(image)

        if not self.e_stop:

            if self.e_count + 1 >= 12:
                self.e_stop = True

            screen.blit(animation[self.e_count], (self.bomb_x - 119, self.bomb_y - 208))
            self.e_count += 1

    def explosion_area(self):
        for enemy in self.enemies_list:
            if abs(self.bomb_x - enemy.hitbox()[0]) < 100 and abs(self.bomb_y - enemy.hitbox()[1]) < 100:
                enemy.health -= 5
        if abs(self.bomb_x - self.player.hitbox()[0]) < 100 and abs(self.bomb_y - self.player.hitbox()[1]) < 100:
            self.player.health -= 5

    def bomb_activated(self, time, bombs_list):
        countdown = (pygame.time.get_ticks() - self.start) / 1000
        if countdown < time:
            self.bomb_animation()
        if countdown > time:
            self.explosion_animation()
            if not self.exploded:
                self.explosion_area()
                self.music.explosion_sound()
                self.exploded = True

        if countdown > time + 0.8:
            bombs_list.remove(self)

def bombs_animation(time, bombs_list):
    for bomb in bombs_list:
        bomb.bomb_activated(time, bombs_list)


start = pygame.time.get_ticks()


def bomb_planted(player, enemies_list, bombs_list, music, cooldown):
    global start
    now = pygame.time.get_ticks()
    if now - start >= cooldown:
        start = now
        if player.bomb > 0:
            bomb = Bomb(music, player.hitbox()[0], player.hitbox()[1], player, enemies_list)
            bombs_list.append(bomb)
            player.bomb -= 1
