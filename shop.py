from wave import *
from upgrade import *


class Shop:

    def __init__(self, player, music, upgrades_list):
        self.player = player
        self.music = music
        self.upgrades_list = upgrades_list

        self.slots_selected = False
        self.slot_1 = None
        self.slot_2 = None
        self.slot_3 = None

        self.slot_1_selected = False
        self.slot_2_selected = False
        self.slot_3_selected = False

        self.start = pygame.time.get_ticks()

    def slots_selected_change(self):
        self.slots_selected = False

    def remove_upgrades(self):
        for upgrade in self.upgrades_list:
            if upgrade.vel_count == 5 and upgrade.upgrade_name == "boots":
                self.upgrades_list.remove(upgrade)
            elif upgrade.wsu_count == 5 and upgrade.upgrade_name == "speed_up":
                self.upgrades_list.remove(upgrade)
            elif upgrade.wdu_count == 5 and upgrade.upgrade_name == "damage_up":
                self.upgrades_list.remove(upgrade)

    def random_upgrades(self):
        self.remove_upgrades()
        if not self.slots_selected:
            sampled_list = random.sample(self.upgrades_list, 3)
            self.slot_1 = sampled_list[0]
            self.slot_2 = sampled_list[1]
            self.slot_3 = sampled_list[2]
            self.slots_selected = True

    def slot_selected(self, x, y):

        slot_1 = pygame.Rect(196, 235, 110, 110)
        slot_2 = pygame.Rect(346, 235, 110, 110)
        slot_3 = pygame.Rect(496, 235, 110, 110)

        if slot_1.collidepoint(x,y):
            self.slot_1_selected = True
            self.slot_2_selected = False
            self.slot_3_selected = False
        elif slot_2.collidepoint(x,y):
            self.slot_1_selected = False
            self.slot_2_selected = True
            self.slot_3_selected = False
        elif slot_3.collidepoint(x,y):
            self.slot_1_selected = False
            self.slot_2_selected = False
            self.slot_3_selected = True
        else:
            self.slot_1_selected = False
            self.slot_2_selected = False
            self.slot_3_selected = False

    def upgrade_purchased(self):
        now = pygame.time.get_ticks()
        if self.slot_1_selected and self.slot_1 is not None and self.slot_1.enough_fund(self.player):
            self.slot_1.upgrade_activated(self.player, self.music)
            self.slot_1 = None
            self.start = now
        elif self.slot_2_selected and self.slot_2 is not None and self.slot_2.enough_fund(self.player):
            self.slot_2.upgrade_activated(self.player, self.music)
            self.slot_2 = None
            self.start = now
        elif self.slot_3_selected and self.slot_3 is not None and self.slot_3.enough_fund(self.player):
            self.slot_3.upgrade_activated(self.player, self.music)
            self.slot_3 = None
            self.start = now
        else:
            if now - self.start >= 1000:
                self.start = now
                self.music.denied_sound()

    def shop_display(self):

        box = pygame.image.load('graphics/ui/box.png')
        box = pygame.transform.scale(box, (500, 250))
        screen.blit(box, (148, 200))

        select = pygame.image.load('graphics/ui/select.png')
        select = pygame.transform.scale(select, (140, 140))

        if self.slot_1_selected:
            screen.blit(select, (182,220))
        elif self.slot_2_selected:
            screen.blit(select, (332, 220))
        elif self.slot_3_selected:
            screen.blit(select, (482, 220))

        font = pygame.font.Font('graphics/fonts/8-BitMadness.ttf', 25)

        x_coor = 185

        x_rect = 175

        slots = [self.slot_1, self.slot_2, self.slot_3]
        for slot in slots:

            if slot is not None:
                upgrade_text = font.render(slot.upgrade_name.replace("_", " "), True, (255, 255, 255))
                text_width = upgrade_text.get_width()
                screen.blit(upgrade_text, (x_rect+75 - text_width // 2, 350))

                upgrade_image = pygame.image.load('graphics/upgrades/'+slot.upgrade_name+'.png')
                upgrade_image = pygame.transform.scale(upgrade_image, (80, 80))
                screen.blit(upgrade_image, (x_coor+25, 250))

                coin = pygame.image.load('graphics/coin/1.png')
                coin = pygame.transform.scale(coin, (24, 24))
                coin_width = coin.get_width()
                screen.blit(coin, (x_rect+95 - coin_width // 2, 380))

                coin_font = pygame.font.Font('graphics/fonts/8-BitMadness.ttf', 40)
                coin_font = coin_font.render(str(slot.cost), True, (255, 255, 255))
                coin_text_width = coin_font.get_width()
                screen.blit(coin_font, (x_rect+60 - coin_text_width // 2, 380))

            x_coor += 150
            x_rect += 150

        shop = pygame.image.load('graphics/ui/shop.png')
        screen.blit(shop, (235, 150))

        shop_title = pygame.image.load('graphics/ui/shop_title.png')
        shop_title = pygame.transform.scale(shop_title, (267, 38))
        screen.blit(shop_title, (262, 170))