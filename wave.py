from enemy import *


class Wave:
    enemies_start = pygame.time.get_ticks()

    def __init__(self, player, enemies_list, spawn_time, max_enemies, total_max_enemies):
        self.player = player
        self.enemies_list = enemies_list
        self.spawn_time = spawn_time
        self.max_enemies = max_enemies
        self.total_max_enemies = total_max_enemies
        self.wave_num = 1
        self.wave_score = 0
        self.end_of_wave = False
        self.num_enemies_spawned = 0
        self.start = 0
        self.count_started = False

    def get_end_of_wave(self):
        if self.end_of_wave and not self.count_started:
            self.start = pygame.time.get_ticks()
            self.count_started = True
        return self.end_of_wave

    def timer(self, seconds):
        countdown = (pygame.time.get_ticks() - self.start) / 1000
        font = pygame.font.Font('graphics/fonts/8-BitMadness.ttf', 32)
        time_left = font.render("Time remaining before wave " + str(self.wave_num) + ": " + str(int(seconds-countdown)), True, (255, 255, 255))
        time_left_width = time_left.get_width()
        screen.blit(time_left, (799//2 - time_left_width//2, 100))

        if countdown > seconds:
            self.start = 0
            self.count_started = False
            self.end_of_wave = False

    def score_reached(self):
        return self.wave_score % self.total_max_enemies == 0 and len(self.enemies_list) == 0

    def enemies_spawn_time(self, enemies_list):
        now = pygame.time.get_ticks()
        if now - self.enemies_start > self.spawn_time:
            self.enemies_start = now
            if len(self.enemies_list) < self.max_enemies and self.num_enemies_spawned < self.total_max_enemies:
                spawn_enemies(enemies_list)
                self.num_enemies_spawned += 1
            elif self.num_enemies_spawned == self.total_max_enemies and self.score_reached():
                self.num_enemies_spawned = 0
                self.wave_score = 0
                self.wave_num += 1
                self.end_of_wave = True
