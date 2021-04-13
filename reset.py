from upgrade import *


def reset_shop(upgrades_list):
    names_list = []
    for upgrade in upgrades_list:
        names_list.append(upgrade.upgrade_name)
    if "boots" not in names_list:
        upgrades_list.append(Upgrade("boots", "armor", 10))
    if "speed_up" not in names_list:
        upgrades_list.append(Upgrade("speed_up", "weapon", 10))
    if "damage_up" not in names_list:
        upgrades_list.append(Upgrade("damage_up", "weapon", 10))


class Reset:

    def __init__(self, player, wave, shop):
        self.player = player
        self.wave = wave
        self.shop = shop

    def reset(self, upgrades_list):
        self.player.player_x = 799//2 - 59
        self.player.player_y = 575//2 - 48
        self.player.health = 10
        self.player.max_health = 10
        self.player.vel = 10
        self.player.armor = 0
        self.player.bomb = 0
        self.player.damage = 1
        self.player.coin = 0
        self.player.score = 0
        self.player.wave = 1
        self.player.cooldown = 1000
        self.player.a_count = 0
        self.player.h_count = 0
        self.player.hit = False
        self.player.attack_activated = False

        self.wave.wave_num = 1
        self.wave.wave_score = 0
        self.wave.num_enemies_spawned = 0
        self.wave.start = 0
        self.wave.count_started = False

        reset_shop(upgrades_list)
