from coin import *
from shop import *
from bomb import *
from reset import *

# game running
menu = True
options = False
credits = False
running = False
pause = False

music = Music(initiate_music()[0], initiate_music()[1])

play_once = True

music.menu_music()

game_menu = Menu()

clock.tick(30)

scroll_y = 0
intermediate = pygame.Surface((799, 5900))

while menu:
    keys = pygame.key.get_pressed()
    pos = pygame.mouse.get_pos()
    x, y = pos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            menu = False
            running = False
        elif event.type == pygame.MOUSEBUTTONUP and game_menu.play_button:
            running = True
            enemies_list = []
            coin_list = []
            bombs_list = []
            music.game_music()
            player = Player("player", 799//2 - 59, 575//2 - 48, 10, 10)
            wave = Wave(player, enemies_list, 2000, 4, 20)
            upgrades_list = [Upgrade("speed_up", "weapon", 10), Upgrade("hp_regen", "hp", 10),
                             Upgrade("hp_boost", "hp", 7), Upgrade("armor", "item", 10), \
                             Upgrade("watermelon", "food", 2), Upgrade("meat", "food", 5),
                             Upgrade("sandwich", "food", 5), Upgrade("cookies", "food", 3), \
                             Upgrade("onigiri", "food", 3), Upgrade("boots", "item", 10), Upgrade("bomb", "item", 8),
                             Upgrade("damage_up", "weapon", 10)]
            shop = Shop(player, music, upgrades_list)
            while running:
                keys = pygame.key.get_pressed()
                pos = pygame.mouse.get_pos()
                x, y = pos
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        menu = False
                        running = False
                    elif player.is_game_over():
                        if event.type == pygame.MOUSEBUTTONUP and game_menu.try_again_button:
                            enemies_list.clear()
                            coin_list.clear()
                            bombs_list.clear()
                            Reset(player, wave, shop).reset(upgrades_list)
                            game_menu.try_again_button = False
                        elif event.type == pygame.MOUSEBUTTONUP and game_menu.menu_button:
                            game_menu.menu_button = False
                            running = False
                            music.menu_music()

                player.show_score()

                if not player.is_game_over():
                    player.health_display()
                    player.coins_collected(music, coin_list)
                    player.show_coins_collected(10, 50)
                    if not wave.get_end_of_wave():
                        play_once = True
                        shop.slots_selected_change()
                        wave.enemies_spawn_time(enemies_list)
                        if wave.num_enemies_spawned != wave.total_max_enemies:
                            spawn_coin_time(5000, coin_list, 4)
                        coin_animation(coin_list)
                        enemies_attack_timer(enemies_list)
                        enemies_animation(player, music, enemies_list)
                        remove_enemies(player, wave, enemies_list)
                        bombs_animation(3, bombs_list)

                        if player.hit:
                            player.hit_animation()
                            if player.hit_sound:
                                music.hit_sound()
                                player.hit_sound = False
                        else:
                            if player.attack_activated:
                                player.attack_animation(enemies_list, music)
                                if player.attack_sound:
                                    music.sword_sound()
                                    player.attack_sound = False

                            elif not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and not keys[pygame.K_UP] and not \
                            keys[pygame.K_DOWN]:
                                player.player_still()

                            else:
                                player.animation()

                        if keys[pygame.K_SPACE]:
                            player.attack_timer()

                        else:
                            if keys[pygame.K_d]:
                                bomb_planted(player, enemies_list, bombs_list, music, 3000)

                            if keys[pygame.K_LEFT] and player.player_x > 10:
                                player.coor_change(-player.vel, 0)
                                player.move_left()

                            elif keys[pygame.K_RIGHT] and player.player_x < 670:
                                player.coor_change(player.vel, 0)
                                player.move_right()

                            elif keys[pygame.K_UP] and player.player_y > 75:
                                player.coor_change(0, -player.vel)
                                player.move_up()

                            elif keys[pygame.K_DOWN] and player.player_y < 370:
                                player.coor_change(0, player.vel)
                                player.move_down()

                    else:
                        enemies_list.clear()
                        coin_list.clear()
                        if play_once:
                            music.shop_sound()
                            play_once = False
                        wave.timer(10)
                        shop.random_upgrades()
                        shop.slot_selected(x, y)
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            shop.upgrade_purchased()

                        shop.shop_display()

                else:
                    game_over_text()
                    player.show_highscore()
                    game_menu.game_over_selected(music, x, y)
                    game_menu.game_over_text()
                pygame.display.update()
                background()

        elif event.type == pygame.MOUSEBUTTONUP and game_menu.option_button:
            options = True
            while options:
                keys = pygame.key.get_pressed()
                pos = pygame.mouse.get_pos()
                x, y = pos
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        options = False
                        menu = False

                    if event.type == pygame.MOUSEBUTTONUP and game_menu.back_button:
                        options = False
                    elif event.type == pygame.MOUSEBUTTONUP and game_menu.music_button:
                        music.music_change_file("music")
                        if music.music:
                            music.music_change()
                            pygame.mixer.music.stop()
                        else:
                            music.music_change()
                            music.menu_music()
                    elif event.type == pygame.MOUSEBUTTONUP and game_menu.sound_button:
                        music.music_change_file("sound")
                        music.sound_change()
                    elif event.type == pygame.MOUSEBUTTONUP and game_menu.credits_button:
                        credits = True
                        game_menu.credits_text(intermediate, scroll_y)
                        while credits:
                            keys = pygame.key.get_pressed()
                            pos = pygame.mouse.get_pos()
                            x, y = pos
                            for event in pygame.event.get():
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    if event.button == 4: scroll_y = min(scroll_y + 50, 0)
                                    if event.button == 5: scroll_y = max(scroll_y - 50, -5300)
                                if game_menu.credits_back_button(scroll_y, x, y) and event.type == pygame.MOUSEBUTTONUP:
                                    credits = False
                                elif event.type == pygame.QUIT:
                                    credits = False
                                    options = False
                                    menu = False

                            screen.blit(intermediate, (0, scroll_y))
                            pygame.display.update()

                menu_background()
                game_menu.options_text(music)
                game_menu.options_button_selected(music, x, y)
                pygame.display.update()

        elif event.type == pygame.MOUSEBUTTONUP and game_menu.quit_button:
            menu = False

    menu_background()
    game_menu.menu_text()
    game_menu.keys_animation()
    game_menu.menu_button_selected(music, x, y)
    game_menu.how_to_play_text()
    pygame.display.update()
