from character import *
import os

def num_files(enemy, type):
    walk_count = 0
    attack_count = 0
    death_count = 0
    hit_count = 0
    num_walk = 1
    num_attack = 1
    num_death = 1
    num_hit = 1
    arr = os.listdir('graphics/'+enemy)
    for file in arr:
        if file == 'R'+str(num_walk)+'.png':
            num_walk += 1
            walk_count += 1
        elif file == 'RA'+str(num_attack)+'.png':
            num_attack += 1
            attack_count += 1
        elif file == 'RD'+str(num_death)+'.png':
            num_death += 1
            death_count += 1
        elif file == 'RH'+str(num_hit)+'.png':
            num_hit += 1
            hit_count += 1
    if type == "walk":
        return walk_count
    elif type == "attack":
        return attack_count
    elif type == "death":
        return death_count
    else:
        return hit_count

class Enemy:
    left = False
    right = False
    up = False
    down = False
    #animation
    def __init__(self, name, enemy_x, enemy_y, vel, health, damage, cooldown):
        self.name = name
        self.enemy_x = enemy_x
        self.enemy_y = enemy_y
        self.vel = vel
        self.health = health
        self.damage = damage
        self.cooldown = cooldown
        self.max_health = health
        self.walk_count = 0
        self.attack_count = 0
        self.death_count = 0
        self.hit_count = 0
        self.death_stop = False
        self.hit_stop = False
        self.hit = False
        self.attack_activated = False
        self.attack_on_going = False
        self.hit_on_going = False
        self.start = pygame.time.get_ticks()


    def move_left(self):
        self.left = True
        self.right = False
        self.up = False
        self.down = False
        self.enemy_x -= self.vel
    def move_right(self):
        self.left = False
        self.right = True
        self.up = False
        self.down = False
        self.enemy_x += self.vel
    def move_up(self):
        self.left = False
        self.right = False
        self.up = True
        self.down = False
        self.enemy_y -= self.vel
    def move_down(self):
        self.left = False
        self.right = False
        self.up = False
        self.down = True
        self.enemy_y += self.vel

    def dimensions(self):
        if self.name == "enemy1":
            return 180, 99
        elif self.name == "enemy2":
            return 200, 200
        elif self.name == "enemy3":
            return 64, 50

    def hitbox(self):
        x = self.dimensions()[0] // 2 + self.enemy_x
        y = self.dimensions()[1] // 2 + self.enemy_y
        return x, y

    def is_close(self, player, distance):
        if abs(player.hitbox()[0] - self.hitbox()[0]) < distance and abs(player.hitbox()[1] - self.hitbox()[1]) < distance:
            return True

    def attack_sound(self, music):
        if self.attack_count == 1 and self.name == "enemy1":
            music.axe_sound()
        elif self.attack_count == 7 and self.name == "enemy2":
            music.dagger_sound()
        elif self.attack_count == 3 and self.name == "enemy3":
            music.slime_attack_sound()

    def hit_sound(self, music):
        if self.name == "enemy1":
            music.monster_hit_sound()
        elif self.name == "enemy2":
            music.goblin_hit_sound()
        else:
            music.slime_hit_sound()

    def death_sound(self, music):
        if self.name == "enemy1":
            music.monster_death_sound()
        elif self.name == "enemy2":
            music.goblin_death_sound()
        else:
            music.slime_death_sound()

    def move_towards_player(self, player):

        left_border = 80
        right_border = 730
        up_border = 120
        down_border = 420

        dirvect = pygame.math.Vector2(player.hitbox()[0] - self.hitbox()[0], player.hitbox()[1] - self.hitbox()[1])
        dir_x = dirvect[0]*(player.hitbox()[0] - self.hitbox()[0])
        dir_y = dirvect[1]*(player.hitbox()[1] - self.hitbox()[1])
        if dir_y == 0:
            if self.hitbox()[0] > player.hitbox()[0] + 20 and self.hitbox()[0] > left_border:
                self.move_left()
            elif self.hitbox()[0] < player.hitbox()[0] - 20 and self.hitbox()[0] < right_border:
                self.move_right()
        elif dir_x == 0:
            if self.hitbox()[1] < player.hitbox()[1] and self.hitbox()[1] < down_border:
                self.move_down()
            elif self.hitbox()[1] > player.hitbox()[1] and self.hitbox()[1] > up_border:
                self.move_up()
        else:
            if self.hitbox()[0] > player.hitbox()[0] + 20 and self.hitbox()[0] > left_border:
                self.move_left()
            if self.hitbox()[1] < player.hitbox()[1] and self.hitbox()[1] < down_border:
                self.move_down()
            elif self.hitbox()[0] < player.hitbox()[0] - 20 and self.hitbox()[0] < right_border:
                self.move_right()
            elif self.hitbox()[1] > player.hitbox()[1] and self.hitbox()[1] > up_border:
                self.move_up()
            if self.hitbox()[1] < player.hitbox()[1] and self.hitbox()[1] < down_border:
                self.move_down()
            if self.hitbox()[0] > player.hitbox()[0] + 20 and self.hitbox()[0] > left_border:
                self.move_left()
            elif self.hitbox()[0] < player.hitbox()[0] - 20 and self.hitbox()[0] < right_border:
                self.move_right()
            elif self.hitbox()[1] > player.hitbox()[1] and self.hitbox()[1] > up_border:
                self.move_up()

    def enemy_sprites(self, type, code):

        num_sprites = num_files(self.name, type)

        sprites_list = []

        for num in range(1, num_sprites + 1):
            if self.name == "enemy2" and "L" in code:
                image = pygame.image.load('graphics/' + self.name + '/R' + code.replace("L", "") + str(num) + '.png')
                image = pygame.transform.flip(image, True, False)
                image = pygame.transform.scale(image, (200, 200))
            else:
                image = pygame.image.load('graphics/' + self.name + '/' + code + str(num) +'.png')
                if self.name == "enemy1":
                    image = pygame.transform.scale(image, (180, 99))
                elif self.name == "enemy2":
                    image = pygame.transform.scale(image, (200, 200))
                elif self.name == "enemy3":
                    image = pygame.transform.scale(image, (64, 50))
            sprites_list.append(image)
        return sprites_list

    def enemy_animation(self, player):
        self.move_towards_player(player)
        # character movement

        walk_right = self.enemy_sprites("walk", "R")

        walk_left = self.enemy_sprites("walk", "L")

        if self.walk_count + 1 >= 3 * len(walk_right):
            self.walk_count = 0
        if self.left:
            screen.blit(walk_left[self.walk_count // 3], (self.enemy_x, self.enemy_y))
            self.walk_count += 1
        elif self.right:
            screen.blit(walk_right[self.walk_count // 3], (self.enemy_x, self.enemy_y))
            self.walk_count += 1
        elif self.up:
            if self.left:
                screen.blit(walk_left[self.walk_count // 3], (self.enemy_x, self.enemy_y))
                self.walk_count += 1
            else:
                screen.blit(walk_right[self.walk_count // 3], (self.enemy_x, self.enemy_y))
                self.walk_count += 1
            #screen.blit(walk_up[self.walk_count // 3], (self.enemy_x, self.enemy_y))
            #self.walk_count += 1
        else:
            if self.right:
                screen.blit(walk_left[self.walk_count // 3], (self.enemy_x, self.enemy_y))
                self.walk_count += 1
            else:
                screen.blit(walk_right[self.walk_count // 3], (self.enemy_x, self.enemy_y))
                self.walk_count += 1
            #screen.blit(walk_down[self.walk_count // 3], (self.enemy_x, self.enemy_y))
            #self.walk_count += 1
        #else:
            #screen.blit(still[self.walk_count // 3], (self.enemy_x, self.enemy_y))
            #self.walk_count += 1

    def attack_animation(self, player, music):

        right_attack = self.enemy_sprites("attack", "RA")

        left_attack = self.enemy_sprites("attack", "LA")

        attack_speed = 3
        if self.name == "enemy2":
            attack_speed = 2

        if self.attack_activated:
            self.attack_on_going = True
            if self.attack_count + 1 >= attack_speed * len(right_attack):
                self.attack_activated = False
                self.attack_on_going = False
                self.attack_count = 0

            self.attack_sound(music)

            if self.attack_count == len(right_attack):
                self.attack(player)

            if self.left:
                screen.blit(left_attack[self.attack_count // attack_speed], (self.enemy_x, self.enemy_y))
                self.attack_count += 1
            elif self.right:
                screen.blit(right_attack[self.attack_count // attack_speed], (self.enemy_x, self.enemy_y))
                self.attack_count += 1
            elif self.up:
                if self.left:
                    screen.blit(left_attack[self.attack_count // attack_speed], (self.enemy_x, self.enemy_y))
                    self.attack_count += 1
                else:
                    screen.blit(right_attack[self.attack_count // attack_speed], (self.enemy_x, self.enemy_y))
                    self.attack_count += 1
            else:
                if self.left:
                    screen.blit(left_attack[self.attack_count // attack_speed], (self.enemy_x, self.enemy_y))
                    self.attack_count += 1
                else:
                    screen.blit(right_attack[self.attack_count // attack_speed], (self.enemy_x, self.enemy_y))
                    self.attack_count += 1

    def attack(self, player):
        if self.is_close(player, 30):
            player.hit = True
            player.hit_sound = True

            if player.has_armor():
                player.armor -= self.damage
            else:
                player.health -= self.damage

    def attack_timer(self):

        now = pygame.time.get_ticks()
        if now - self.start >= self.cooldown:
            self.attack_activated = True
            self.start = now


    def hit_animation(self, music):

        hit_right = self.enemy_sprites("hit", "RH")

        hit_left = self.enemy_sprites("hit", "LH")

        if self.hit:
            self.hit_on_going = True
            if self.hit_count + 1 >= 3 * len(hit_right):
                self.hit = False
                self.hit_on_going = False
                self.hit_count = 0
            if self.left:
                self.walk_count = 0
                screen.blit(hit_left[self.hit_count // 3], (self.enemy_x, self.enemy_y))
                self.hit_count += 1
                if self.hitbox()[0] < 730:
                    self.enemy_x += 5
            elif self.right:
                self.walk_count = 0
                screen.blit(hit_right[self.hit_count // 3], (self.enemy_x, self.enemy_y))
                self.hit_count += 1
                if self.hitbox()[0] > 80:
                    self.enemy_x -= 5
            else:
                self.walk_count = 0
                screen.blit(hit_right[self.hit_count // 3], (self.enemy_x, self.enemy_y))
                self.hit_count += 1
                if self.hitbox()[0] > 80:
                    self.enemy_x -= 5



    def death_animation(self, music):

        death_right = self.enemy_sprites("death", "RD")

        death_left = self.enemy_sprites("death", "LD")

        if not self.death_stop:
            if self.death_count + 1 >= 3 * len(death_right):
                self.death_stop = True
            elif self.death_count == 0:
                self.death_sound(music)
            if self.left:
                screen.blit(death_left[self.death_count // 3], (self.enemy_x, self.enemy_y))
                self.death_count += 1
            elif self.right:
                screen.blit(death_right[self.death_count // 3], (self.enemy_x, self.enemy_y))
                self.death_count += 1
            else:
                screen.blit(death_right[self.death_count // 3], (self.enemy_x, self.enemy_y))
                self.death_count += 1

    def health_display(self):

        enemy_width = self.dimensions()[0]

        health_width = 58*(self.health / self.max_health)
        health_height = self.enemy_y-8
        if self.name == "enemy2":
            health_height = self.enemy_y+65
        if self.name == "enemy3":
            health_height = self.enemy_y-5

        middle = self.enemy_x + (enemy_width // 2) - (58 // 2)
        if self.health > 0:
            pygame.draw.rect(screen, (213, 0, 0), (middle+1, health_height, health_width-2, 7))

        bar = pygame.image.load('graphics/health/enemy_bar.png')
        bar = pygame.transform.scale(bar, (58, 7))
        screen.blit(bar, (middle, health_height))

def spawn_enemies(enemies_list):
    spawn1 = [70, 230]
    spawn2 = [399, 100]
    spawn3 = [730, 230]
    spawn4 = [399, 420]
    random_spawn = random.choice([spawn1,spawn2,spawn3,spawn4])
    enemies = [Enemy("enemy1", random_spawn[0], random_spawn[1], 1, 5, 3, 3000),
               Enemy("enemy2", random_spawn[0], random_spawn[1], 3, 3, 1, 1000),
               Enemy("enemy3", random_spawn[0], random_spawn[1], 2, 2, 2, 2000)]
    random_enemy = random.choice(enemies)
    random_enemy.enemy_x -= random_enemy.dimensions()[0] // 2
    random_enemy.enemy_y -= random_enemy.dimensions()[1] // 2
    enemies_list.append(random_enemy)

def enemies_animation(player, music, enemies_list):
    for enemy in enemies_list:
        if enemy.health <= 0:
            enemy.death_animation(music)
        elif enemy.hit or enemy.hit_on_going:
            enemy.hit_animation(music)
        elif enemy.attack_activated and enemy.is_close(player, 30) or enemy.attack_on_going:
            enemy.attack_animation(player, music)
        else:
            enemy.enemy_animation(player)
        enemy.health_display()

def remove_enemies(player, wave, enemies_list):
    for enemy in enemies_list:
        if enemy.death_stop:
            enemies_list.remove(enemy)
            player.score += 1
            wave.wave_score += 1

def enemies_attack_timer(enemies_list):
    for enemy in enemies_list:
        enemy.attack_timer()
