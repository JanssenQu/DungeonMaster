from ui import *
import time
import math
class Player:
    left = True
    right = False
    up = False
    down = False

    def __init__(self, name, player_x, player_y, vel, health):
        self.name = name
        self.player_x = player_x
        self.player_y = player_y
        self.health = health
        self.max_health = health
        self.vel = vel
        self.armor = 0
        self.bomb = 0
        self.damage = 1
        self.coin = 0
        self.rl_count = 0
        self.uds_count = 0
        self.a_count = 0
        self.s_count = 0
        self.h_count = 0
        self.score = 0
        self.wave = 1
        self.cooldown = 1000
        self.attack_state = False
        self.attack_sound = False
        self.attack_activated = False
        self.attack_sound = False
        self.hit = False
        self.hit_sound = False
        self.last = pygame.time.get_ticks()
        self.start = pygame.time.get_ticks()

    def has_armor(self):
        return self.armor > 0

    def armor_regen(self):
        self.armor = 10

    def health_regen(self):
        self.health = self.max_health

    def get_max_health(self):
        return self.max_health

    def wave_change(self):
        self.end_of_wave = not self.end_of_wave

    def coor_change(self, x, y):
        self.player_x += x
        self.player_y += y

    def move_left(self):
        self.left = True
        self.right = False
        self.up = False
        self.down = False

    def move_right(self):
        self.left = False
        self.right = True
        self.up = False
        self.down = False

    def move_up(self):
        self.up = True
        self.down = False

    def move_down(self):
        self.up = False
        self.down = True

    def is_game_over(self):
        if self.health == 0 or self.health < 0:
            return True

    def attack_hitbox(self):
        x = 0
        if self.left:
            x = 32 + self.player_x
        elif self.right:
            x = 95 + self.player_x
        y = 96 // 2 + self.player_y
        return x, y

    def hitbox(self):
        x = 59 + self.player_x
        y = 96 // 2 + self.player_y
        return x, y

    def animation(self):

        # character movement
        walk_right = [pygame.image.load('graphics/'+self.name+'/R1.png'), pygame.image.load('graphics/'+self.name+'/R2.png'), pygame.image.load('graphics/'+self.name+'/R3.png'), pygame.image.load('graphics/'+self.name+'/R4.png'), pygame.image.load('graphics/'+self.name+'/R5.png'),pygame.image.load('graphics/'+self.name+'/R6.png')]

        walk_left = [pygame.image.load('graphics/'+self.name+'/L1.png'), pygame.image.load('graphics/'+self.name+'/L2.png'), pygame.image.load('graphics/'+self.name+'/L3.png'), pygame.image.load('graphics/'+self.name+'/L4.png'), pygame.image.load('graphics/'+self.name+'/L5.png'),pygame.image.load('graphics/'+self.name+'/L6.png')]

        if self.rl_count + 1 >= 18:
            self.rl_count = 0
        if self.uds_count + 1 >= 15:
            self.uds_count = 0

        if self.left or self.left and self.up or self.left and self.down:
            screen.blit(walk_left[self.rl_count // 3], (self.player_x, self.player_y))
            self.rl_count += 1
        if self.right or self.right and self.up or self.right and self.down:
            screen.blit(walk_right[self.rl_count // 3], (self.player_x, self.player_y))
            self.rl_count += 1

    def attack_animation(self, enemies_list, music):

        right_attack = [pygame.image.load('graphics/'+self.name + '/RA1.png'),pygame.image.load('graphics/'+self.name + '/RA2.png'),pygame.image.load('graphics/'+self.name + '/RA3.png'),

                        pygame.image.load('graphics/'+self.name + '/RA4.png'), pygame.image.load('graphics/'+self.name + '/RA5.png'), pygame.image.load('graphics/'+self.name + '/RA6.png')]

        left_attack = [pygame.image.load('graphics/'+self.name + '/LA1.png'),pygame.image.load('graphics/'+self.name + '/LA2.png'), pygame.image.load('graphics/'+self.name + '/LA3.png'),

                       pygame.image.load('graphics/'+self.name + '/LA4.png'),pygame.image.load('graphics/'+self.name + '/LA5.png'), pygame.image.load('graphics/'+self.name + '/LA6.png')]

        if self.attack_activated:
            if self.a_count + 1 >= 12:
                self.attack_activated = False
                self.a_count = 0

            if self.a_count == 6:
                self.player_attack(enemies_list, music)

            if self.left:
                screen.blit(left_attack[self.a_count // 2], (self.player_x, self.player_y))
                self.a_count += 1
            elif self.right:
                screen.blit(right_attack[self.a_count // 2], (self.player_x, self.player_y))
                self.a_count += 1
            elif self.up:
                if self.left:
                    screen.blit(left_attack[self.a_count // 2], (self.player_x, self.player_y))
                    self.a_count += 1
                elif self.right:
                    screen.blit(right_attack[self.a_count // 2], (self.player_x, self.player_y))
                    self.a_count += 1
            elif self.down:
                if self.left:
                    screen.blit(left_attack[self.a_count // 2], (self.player_x, self.player_y))
                    self.a_count += 1
                elif self.right:
                    screen.blit(right_attack[self.a_count // 2], (self.player_x, self.player_y))
                    self.a_count += 1

    def player_still(self):
        old_right_still = [pygame.image.load('graphics/' + self.name + '/RS1.png'), pygame.image.load('graphics/' + self.name + '/RS2.png'),
                      pygame.image.load('graphics/' + self.name + '/RS3.png')]

        right_still = []
        for image in old_right_still:
            new_image = pygame.transform.scale(image, (108, 96))
            right_still.append(new_image)

        old_left_still = [pygame.image.load('graphics/' + self.name + '/LS1.png'), pygame.image.load('graphics/' + self.name + '/LS2.png'),
                     pygame.image.load('graphics/' + self.name + '/LS3.png')]

        left_still = []
        for image in old_left_still:
            new_image = pygame.transform.scale(image, (118, 96))
            left_still.append(new_image)

        if self.s_count + 1 >= 9:
            self.s_count = 0

        if self.left:
            self.rl_count = 0
            screen.blit(left_still[self.s_count // 3], (self.player_x, self.player_y))
            self.s_count += 1
        elif self.right:
            self.rl_count = 0
            screen.blit(right_still[self.s_count // 3], (self.player_x, self.player_y))
            self.s_count += 1

    def hit_animation(self):

        old_right_hit = [pygame.image.load('graphics/' + self.name + '/RH1.png'),
                           pygame.image.load('graphics/' + self.name + '/RH2.png'),
                           pygame.image.load('graphics/' + self.name + '/RH3.png')]

        right_hit = []
        for image in old_right_hit:
            new_image = pygame.transform.scale(image, (108, 96))
            right_hit.append(new_image)

        old_left_hit = [pygame.image.load('graphics/' + self.name + '/LH1.png'),
                          pygame.image.load('graphics/' + self.name + '/LH2.png'),
                          pygame.image.load('graphics/' + self.name + '/LH3.png')]

        left_hit = []
        for image in old_left_hit:
            new_image = pygame.transform.scale(image, (118, 96))
            left_hit.append(new_image)

        if self.hit:
            if self.h_count + 1 >= 9:
                self.hit = False
                self.h_count = 0

            if self.left:
                self.rl_count = 0
                screen.blit(left_hit[self.h_count // 3], (self.player_x, self.player_y))
                self.h_count += 1
                if self.player_x < 675:
                    self.player_x += 5
            elif self.right:
                self.rl_count = 0
                screen.blit(right_hit[self.h_count // 3], (self.player_x, self.player_y))
                self.h_count += 1
                if self.player_x > 15:
                    self.player_x -= 5

    def player_attack(self, enemies, music):
        for enemy in enemies:
            if abs(self.attack_hitbox()[0] - enemy.hitbox()[0]) < 40 and abs(self.attack_hitbox()[1] - enemy.hitbox()[1]) < 40:
                enemy.attack_activated = False
                enemy.attack_on_going = False
                enemy.attack_count = 0
                enemy.health -= self.damage
                enemy.hit = True
                if enemy.health > 0:
                    enemy.hit_sound(music)

    def attack_timer(self):

        now = pygame.time.get_ticks()
        if now - self.last >= self.cooldown:
            self.last = now
            self.attack_activated = True
            self.attack_sound = True

    def health_display(self):
        for num in range(0, 11):
            new_health = math.floor(self.health*10 / self.max_health)
            if int(new_health) == num:
                bar = pygame.image.load('graphics/health/bar_' + str(num) + '.png')
                bar = pygame.transform.scale(bar, (248, 25))
                screen.blit(bar, (500, 10))

        for num in range(0, 11):
            if int(self.armor) == num:
                bar = pygame.image.load('graphics/health/sbar_' + str(num) + '.png')
                bar = pygame.transform.scale(bar, (248, 25))
                screen.blit(bar, (500, 55))

    def show_score(self):
        font = pygame.font.Font('graphics/fonts/8-BitMadness.ttf', 32)
        score = font.render("Score : " + str(self.score), True, (255, 255, 255))
        width = score.get_width()
        height = score.get_height()
        if self.is_game_over():
            screen.blit(score, (799 // 2 - width // 2, 250))
        else:
            screen.blit(score, (10,10))

    def coins_collected(self, music, coin_list):
        for coin in coin_list:
            if abs((self.player_x + 64) - coin.x) < 30 and abs((self.player_y + 48) - coin.y) < 30:
                coin_list.remove(coin)
                music.coin_sound()
                self.coin += 1

    def show_coins_collected(self, x, y):
        font = pygame.font.Font('graphics/fonts/8-BitMadness.ttf', 32)
        coin = font.render("Coins : " + str(self.coin), True, (255, 255, 255))
        screen.blit(coin, (x, y))

    def show_highscore(self):
        f = open('highscore.txt')
        highscore = f.readline()
        f.close()
        if self.score > int(highscore):
            f = open('highscore.txt', 'w')
            f.write(str(self.score))
            f.close()
        font = pygame.font.Font('graphics/fonts/8-BitMadness.ttf', 32)
        score = font.render("High Score : " + highscore, True, (255, 255, 255))
        width = score.get_width()
        screen.blit(score, (799//2-width//2, 280))
        f.close()