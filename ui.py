import pygame
from music import *
import random

#global variables
bg_count = 0

pygame.init()

#create the screen
screen = pygame.display.set_mode((799, 575))

#title and icon
pygame.display.set_caption("DungeonMaster")
icon = pygame.image.load("graphics/icon/knight.png")
pygame.display.set_icon(icon)
clock = pygame.time.Clock()

#background animation
def menu_background():
    menu_bg = pygame.image.load("graphics/background/menu.png")
    screen.blit(menu_bg, (0, 0))

def background():
    bg = [pygame.image.load('graphics/background/f1.png'), pygame.image.load('graphics/background/f2.png'), pygame.image.load('graphics/background/f3.png'), pygame.image.load('graphics/background/f4.png'), pygame.image.load('graphics/background/f5.png'),pygame.image.load('graphics/background/f6.png')]
    global bg_count
    if bg_count + 1 >= 18:
        bg_count = 0
    screen.blit(bg[bg_count // 3], (0, 0))
    bg_count += 1

def game_over_text():
    over_font = pygame.font.Font('graphics/fonts/8-BitMadness.ttf', 64)
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    width = over_text.get_width()
    #height = over_text.get_height()
    screen.blit(over_text, (799//2 - width//2 , 200))

class Menu:
#menu options

    unpressed_button = pygame.image.load('graphics/ui/button1.png')
    unpressed_button = pygame.transform.scale(unpressed_button, (192, 192))

    pressed_button = pygame.image.load('graphics/ui/button2.png')
    pressed_button = pygame.transform.scale(pressed_button, (192, 192))

    unpressed_option = pygame.transform.scale(unpressed_button, (288, 192))
    pressed_option = pygame.transform.scale(pressed_button, (288, 192))

    unpressed_music = pygame.transform.scale(unpressed_button, (370, 192))
    pressed_music = pygame.transform.scale(pressed_button, (370, 192))

    font = pygame.font.Font('graphics/fonts/8-BitMadness.ttf', 55)

    title = pygame.image.load('graphics/ui/title.png')

    text_font = pygame.font.Font('graphics/fonts/8-BitMadness.ttf', 30)
    name = text_font.render("created by Janssen Qu", True, (255, 255, 255))

    def __init__(self):
        self.play_button = False
        self.option_button = False
        self.quit_button = False

        self.play_sound = False
        self.option_sound = False
        self.quit_sound = False

        self.back_button = False
        self.music_button = False
        self.sound_button = False
        self.credits_button = False

        self.back_sound = False
        self.music_sound = False
        self.sound_sound = False
        self.credits_sound = False

        self.try_again_button = False
        self.menu_button = False

        self.try_again_sound = False
        self.menu_sound = False

        self.key_count = 0




    def menu_button_selected(self, music, x, y):
        play_button = pygame.Rect(32, 194, 144, 60)
        option_button = pygame.Rect((32, 294, 215, 60))
        quit_button = pygame.Rect(32, 394, 144, 60)
        if play_button.collidepoint(x, y):
            self.play_button = True
            self.option_button = False
            self.quit_button = False
            if not self.play_sound:
                music.menu_select_sound()
                self.play_sound = True
                self.option_sound = False
                self.quit_sound = False
        elif option_button.collidepoint(x, y):
            self.option_button = True
            self.play_button = False
            self.quit_button = False
            if not self.option_sound:
                music.menu_select_sound()
                self.play_sound = False
                self.option_sound = True
                self.quit_sound = False
        elif quit_button.collidepoint(x, y):
            self.quit_button = True
            self.play_button = False
            self.option_button = False
            if not self.quit_sound:
                music.menu_select_sound()
                self.play_sound = False
                self.option_sound = False
                self.quit_sound = True
        else:
            self.play_button = False
            self.option_button = False
            self.quit_button = False
            self.play_sound = False
            self.option_sound = False
            self.quit_sound = False

    def options_button_selected(self, music, x, y):
        back_button = pygame.Rect(32, 194, 144, 60)
        music_button = pygame.Rect(33, 294, 277, 60)
        sound_button = pygame.Rect(33, 394, 277, 60)
        credits_button = pygame.Rect(33, 494, 214, 60)
        if back_button.collidepoint(x, y):
            self.back_button = True
            self.music_button = False
            self.sound_button = False
            self.credits_button = False
            if not self.back_sound:
                music.menu_select_sound()
                self.back_sound = True
                self.music_sound = False
                self.sound_sound = False
                self.credits_sound = False
        elif music_button.collidepoint(x, y):
            self.back_button = False
            self.music_button = True
            self.sound_button = False
            self.credits_button = False
            if not self.music_sound:
                music.menu_select_sound()
                self.back_sound = False
                self.music_sound = True
                self.sound_sound = False
                self.credits_sound = False
        elif sound_button.collidepoint(x, y):
            self.back_button = False
            self.music_button = False
            self.sound_button = True
            self.credits_button = False
            if not self.sound_sound:
                music.menu_select_sound()
                self.back_sound = False
                self.music_sound = False
                self.sound_sound = True
                self.credits_sound = False
        elif credits_button.collidepoint(x, y):
            self.back_button = False
            self.music_button = False
            self.sound_button = False
            self.credits_button = True
            if not self.credits_sound:
                music.menu_select_sound()
                self.back_sound = False
                self.music_sound = False
                self.sound_sound = False
                self.credits_sound = True
        else:
            self.back_button = False
            self.music_button = False
            self.sound_button = False
            self.credits_button = False
            self.back_sound = False
            self.music_sound = False
            self.sound_sound = False
            self.credits_sound = False

    def menu_text(self):

        screen.blit(self.title, (95, 50))

        screen.blit(self.name, (500, 550))

        play_font = self.font.render("PLAY", True, (255, 255, 255))

        option_font = self.font.render("OPTIONS", True, (255, 255, 255))

        quit_font = self.font.render("QUIT", True, (255, 255, 255))

        if self.play_button:
            screen.blit(self.pressed_button, (5, 125))
            screen.blit(play_font, (50, 207))
        else:
            screen.blit(self.unpressed_button, (5, 125))
            screen.blit(play_font, (50, 200))

        if self.option_button:
            screen.blit(self.pressed_option, (-10, 225))
            screen.blit(option_font, (50, 307))
        else:
            screen.blit(self.unpressed_option, (-10, 225))
            screen.blit(option_font, (50, 300))

        if self.quit_button:
            screen.blit(self.pressed_button, (5, 325))
            screen.blit(quit_font, (55, 407))
        else:
            screen.blit(self.unpressed_button, (5, 325))
            screen.blit(quit_font, (55, 400))

    def options_text(self, music):

        screen.blit(self.title, (95, 50))

        screen.blit(self.name, (500, 550))

        back_font = self.font.render("BACK", True, (255, 255, 255))

        music_on_font = self.font.render("MUSIC: ON", True, (255, 255, 255))
        music_off_font = self.font.render("MUSIC: OFF", True, (255, 255, 255))

        sound_on_font = self.font.render("SOUND: ON", True, (255, 255, 255))
        sound_off_font = self.font.render("SOUND: OFF", True, (255, 255, 255))

        credits_font = self.font.render("CREDITS", True, (255, 255, 255))

        if self.back_button:
            screen.blit(self.pressed_button, (5, 125))
            screen.blit(back_font, (50, 207))
        else:
            screen.blit(self.unpressed_button, (5, 125))
            screen.blit(back_font, (50, 200))

        if self.music_button:
            if music.music:
                screen.blit(self.pressed_music, (-20, 225))
                screen.blit(music_on_font, (50, 307))
            else:
                screen.blit(self.pressed_music, (-20, 225))
                screen.blit(music_off_font, (50, 307))
        else:
            if music.music:
                screen.blit(self.unpressed_music, (-20, 225))
                screen.blit(music_on_font, (50, 300))
            else:
                screen.blit(self.unpressed_music, (-20, 225))
                screen.blit(music_off_font, (50, 300))

        if self.sound_button:
            if music.sound:
                screen.blit(self.pressed_music, (-20, 325))
                screen.blit(sound_on_font, (55, 407))
            else:
                screen.blit(self.pressed_music, (-20, 325))
                screen.blit(sound_off_font, (55, 407))
        else:
            if music.sound:
                screen.blit(self.unpressed_music, (-20, 325))
                screen.blit(sound_on_font, (55, 400))
            else:
                screen.blit(self.unpressed_music, (-20, 325))
                screen.blit(sound_off_font, (55, 400))

        if self.credits_button:
            screen.blit(self.pressed_option, (-10, 425))
            screen.blit(credits_font, (48, 507))
        else:
            screen.blit(self.unpressed_option, (-10, 425))
            screen.blit(credits_font, (48, 500))

    def credits_text(self, intermediate, scroll_y):
        i_a = intermediate.get_rect()
        x1 = i_a[0]
        x2 = x1 + i_a[2]
        a, b = (255, 0, 0), (60, 255, 120)
        y1 = i_a[1]
        y2 = y1 + i_a[3]
        h = y2 - y1
        rate = (float((b[0] - a[0]) / h),
                (float(b[1] - a[1]) / h),
                (float(b[2] - a[2]) / h))

        for line in range(y1, y2):
            color = (min(max(a[0] + (rate[0] * line), 0), 255),
                     min(max(a[1] + (rate[1] * line), 0), 255),
                     min(max(a[2] + (rate[2] * line), 0), 255))
            pygame.draw.line(intermediate, color, (x1, line), (x2, line))

        y = 300

        intermediate.blit(self.title, (95, 50))
        name_width = self.name.get_width()
        intermediate.blit(self.name, (799//2 - name_width//2, 150))

        with open("credits.txt") as f:
            for line in f:
                line = line.replace("\n", "")
                font = pygame.font.Font('graphics/fonts/8-BitMadness.ttf', 19)
                line = font.render(line, True, (255, 255, 255))
                intermediate.blit(line,(0,y))
                y += 30

        back_button = pygame.image.load('graphics/ui/back.png')
        back_button = pygame.transform.scale(back_button, (32, 32))
        intermediate.blit(back_button, (10, 10+scroll_y))

        scroll = self.text_font.render("Use the scroll wheel to navigate", True, (255, 255, 255))
        scroll_width = scroll.get_width()
        intermediate.blit(scroll, (799//2 - scroll_width//2, 250))

    def credits_back_button(self, scroll_y, x, y):
        back_button = pygame.Rect(10, 10+scroll_y, 32, 32)
        if back_button.collidepoint(x, y):
            return True

    def keys_animation(self):

        keys = ["up", "down", "left", "right", "space", "d"]

        up_list = []
        down_list = []
        left_list = []
        right_list = []
        space_list = []
        d_list = []

        keys_list = [up_list, down_list, left_list, right_list, space_list, d_list]

        index = 0

        for key in keys:
            for num in range(1,5):
                image = pygame.image.load('graphics/ui/' + key + str(num) + '.png')
                if key == "space":
                    image = pygame.transform.scale(image, (160, 32))
                else:
                    image = pygame.transform.scale(image, (32, 32))
                keys_list[index].append(image)
            index += 1

        if self.key_count + 1 >= 24:
            self.key_count = 0

        self.key_count += 1
        screen.blit(up_list[self.key_count // 6], (500, 250))
        screen.blit(down_list[self.key_count // 6], (500, 275))
        screen.blit(left_list[self.key_count // 6], (465, 275))
        screen.blit(right_list[self.key_count // 6], (535, 275))
        screen.blit(space_list[self.key_count // 6], (600, 275))
        screen.blit(d_list[self.key_count // 6], (500, 375))

    def how_to_play_text(self):
        how_to_play = self.text_font.render("HOW TO PLAY:", True, (255, 255, 255))
        screen.blit(how_to_play, (575, 200))
        move = self.text_font.render("MOVE", True, (255, 255, 255))
        move_width = move.get_width()
        screen.blit(move, (516 - move_width//2, 320))
        attack = self.text_font.render("ATTACK", True, (255, 255, 255))
        attack_width = attack.get_width()
        screen.blit(attack, (680 - attack_width//2, 320))
        place_bomb = self.text_font.render("PLACE BOMB", True, (255, 255, 255))
        place_bomb_width = place_bomb.get_width()
        screen.blit(place_bomb, (516 - place_bomb_width//2, 420))

    def game_over_text(self):
        font = pygame.font.Font('graphics/fonts/8-BitMadness.ttf', 40)
        retry_text = font.render("RETRY", True, (255, 255, 255))
        menu_text = font.render("MENU", True, (255, 255, 255))
        retry_width = retry_text.get_width()
        menu_text_width = menu_text.get_width()
        screen.blit(retry_text, (799//3 - retry_width//2, 350))
        screen.blit(menu_text, (799*2//3 - menu_text_width//2, 350))

        select = pygame.image.load('graphics/ui/select2.png')
        select = pygame.transform.scale(select, (140, 41))

        if self.try_again_button:
            screen.blit(select, (195, 343))
        elif self.menu_button:
            screen.blit(select, (462, 343))

    def game_over_selected(self, music, x, y):
        try_again_button = pygame.Rect(195, 343, 140, 41)
        menu_button = pygame.Rect(462, 343, 140, 41)
        if try_again_button.collidepoint(x, y):
            self.try_again_button = True
            self.menu_button = False
            if not self.try_again_sound:
                music.menu_select_sound()
                self.try_again_sound = True
                self.menu_sound = False
        elif menu_button.collidepoint(x, y):
            self.try_again_button = False
            self.menu_button = True
            if not self.menu_sound:
                music.menu_select_sound()
                self.try_again_sound = False
                self.menu_sound = True
        else:
            self.try_again_button = False
            self.menu_button = False
