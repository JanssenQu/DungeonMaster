from ui import *

class Coin:
    c_count = 0
    def __init__(self):
        self.x = random.randint(70,700)
        self.y = random.randint(150,420)

    def coin_animation(self):
        animation = [pygame.image.load('graphics/coin/1.png'), pygame.image.load('graphics/coin/2.png'), pygame.image.load('graphics/coin/3.png'), pygame.image.load('graphics/coin/4.png'), pygame.image.load('graphics/coin/5.png')]

        if self.c_count + 1 >= 15:
            self.c_count = 0

        screen.blit(animation[self.c_count // 3], (self.x, self.y))
        self.c_count += 1

def coin_animation(coin_list):
    for coin in coin_list:
        coin.coin_animation()

def spawn_coin(coin_list):
    new_coin = Coin()
    coin_list.append(new_coin)

coin_start = pygame.time.get_ticks()
def spawn_coin_time(time, coin_list, max_coin):
    global coin_start
    now = pygame.time.get_ticks()
    if now - coin_start > time:
        coin_start = now
        if len(coin_list) < max_coin:
            spawn_coin(coin_list)