class Upgrade:
    wsu_count = 0
    vel_count = 0
    wdu_count = 0

    def __init__(self, upgrade_name, upgrade_class, cost):
        self.upgrade_name = upgrade_name
        self.upgrade_class = upgrade_class
        self.cost = cost

    def enough_fund(self, player):
        fund = player.coin
        if fund - self.cost >= 0:
            if self.upgrade_name == "hp_regen" and player.health == player.max_health or self.upgrade_class == "food" \
                    and player.health == player.max_health or \
                    self.upgrade_name == "armor" and player.armor == 10:
                return False
            else:
                return True
        else:
            return False

    def upgrade_activated(self, player, music):
        player.coin -= self.cost

        if self.upgrade_name == "speed_up":
            player.cooldown -= 100
            self.wsu_count += 1

        elif self.upgrade_name == "hp_regen":
            player.health_regen()

        elif self.upgrade_name == "hp_boost":
            player.max_health += 2
            player.health += 2

        elif self.upgrade_name == "armor":
            player.armor_regen()

        elif self.upgrade_name == "watermelon":
            if player.health + 2 > player.max_health:
                player.health_regen()
            else:
                player.health += 2

        elif self.upgrade_name == "meat" or self.upgrade_name == "sandwich":
            if player.health + 5 > player.max_health:
                player.health_regen()
            else:
                player.health += 5

        elif self.upgrade_name == "cookies" or self.upgrade_name == "onigiri":
            if player.health + 3 > player.max_health:
                player.health_regen()
            else:
                player.health += 3

        elif self.upgrade_name == "boots":
            player.vel += 2
            self.vel_count += 1

        elif self.upgrade_name == "bomb":
            player.bomb += 1

        elif self.upgrade_name == "damage_up":
            player.damage += 1
            self.wdu_count += 1

        music.upgrade_sound(self)
