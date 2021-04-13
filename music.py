import pygame


# music and sound
class Music:

    def __init__(self, music, sound):
        if music == "True":
            self.music = True
        else:
            self.music = False

        if sound == "True":
            self.sound = True
        else:
            self.sound = False

    def music_change(self):
        self.music = not self.music

    def sound_change(self):
        self.sound = not self.sound

    def sword_sound(self):
        if self.sound:
            effect = pygame.mixer.Sound('music/swordswing.wav')
            effect.play()

    def coin_sound(self):
        if self.sound:
            effect = pygame.mixer.Sound('music/coin.wav')
            effect.play()

    def menu_select_sound(self):
        if self.sound:
            effect = pygame.mixer.Sound('music/menuselect.wav')
            effect.play()

    def menu_music(self):
        if self.music:
            pygame.mixer.music.load('music/intro.mp3')
            pygame.mixer.music.play(loops=-1)

    def game_music(self):
        if self.music:
            pygame.mixer.music.load('music/game.mp3')
            pygame.mixer.music.play(loops=-1)

    def upgrade_sound(self, upgrade):
        if self.sound:
            upgrade_classes = ["weapon", "hp", "item", "food"]
            for upgrade_class in upgrade_classes:
                if upgrade_class == upgrade.upgrade_class:
                    effect = pygame.mixer.Sound('music/' + upgrade_class + '.wav')
                    effect.play()

    def denied_sound(self):
        if self.sound:
            effect = pygame.mixer.Sound('music/denied.wav')
            effect.play()

    def shop_sound(self):
        if self.sound:
            effect = pygame.mixer.Sound('music/shop.wav')
            effect.play()

    def explosion_sound(self):
        if self.sound:
            effect = pygame.mixer.Sound('music/explosion.wav')
            effect.play()

    def music_change_file(self, to_change):
        f1 = open('settings.txt')
        content = f1.readlines()
        if to_change == "music":
            music = content[0].replace(str(self.music), str(not self.music))
            sound = content[1]
            f1.close()
            f2 = open('settings.txt', 'w')
            f2.write("".join([music, sound]))
            f2.close()
        elif to_change == "sound":
            music = content[0]
            sound = content[1].replace(str(self.sound), str(not self.sound))
            f1.close()
            f2 = open('settings.txt', 'w')
            f2.write("".join([music, sound]))
            f2.close()

    def hit_sound(self):
        if self.sound:
            effect = pygame.mixer.Sound('music/hit.wav')
            effect.play()

    def axe_sound(self):
        if self.sound:
            effect = pygame.mixer.Sound('music/axe.wav')
            effect.play()

    def dagger_sound(self):
        if self.sound:
            effect = pygame.mixer.Sound('music/dagger.wav')
            effect.play()

    def slime_attack_sound(self):
        if self.sound:
            effect = pygame.mixer.Sound('music/slime_attack.wav')
            effect.play()

    def slime_hit_sound(self):
        if self.sound:
            effect = pygame.mixer.Sound('music/slime_hit.wav')
            effect.play()

    def slime_death_sound(self):
        if self.sound:
            effect = pygame.mixer.Sound('music/slime_death.wav')
            effect.play()

    def monster_hit_sound(self):
        if self.sound:
            effect = pygame.mixer.Sound('music/monster_hit.wav')
            effect.play()

    def monster_death_sound(self):
        if self.sound:
            effect = pygame.mixer.Sound('music/monster_death.wav')
            effect.play()

    def goblin_hit_sound(self):
        if self.sound:
            effect = pygame.mixer.Sound('music/goblin_hit.wav')
            effect.play()

    def goblin_death_sound(self):
        if self.sound:
            effect = pygame.mixer.Sound('music/goblin_death.wav')
            effect.play()

def initiate_music():
    f = open('settings.txt')
    content = f.readlines()
    music = content[0].replace("music: ", "").replace("\n", "")
    sound = content[1].replace("sound: ", "")
    music_list = [music, sound]
    f.close()
    return music_list
