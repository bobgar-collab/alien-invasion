import random
import sys

import pygame

import menu as sb
from alien import Alien
from bonus import Bonus, BonusType
from bullet import Bullet
from game_state import GameState
from game_stats import GameStats
from scoreboard import Scoreboard
from screen_background import ScreenBackground
from settings import Settings
from ship import Ship
from sound_manager import SoundManager
# Events
from style_manager import StyleManager

ALIENS_FIRE_EVENT = pygame.USEREVENT + 1
DISABLE_FIRE_BONUS = pygame.USEREVENT + 2
DISABLE_MUSHROOM_STYLE_BONUS = pygame.USEREVENT + 3


class AlienInvasion:

    def __init__(self):
        pygame.init()

        self.settings = Settings()
        if self.settings.full_screen:
            self.screen = pygame.display.set_mode((self.settings.screen_width,
                                                   self.settings.screen_height),
                                                  pygame.FULLSCREEN, depth=16)
            self.settings.screen_width = self.screen.get_rect().width
            self.settings.screen_height = self.screen.get_rect().height
        else:
            self.screen = pygame.display.set_mode((self.settings.screen_width,
                                                   self.settings.screen_height), depth=16)

        pygame.display.set_caption("Alien Invasion")

        self.style = StyleManager(self)
        self.background = ScreenBackground(self)
        self.stats = GameStats(self)
        self.scoreboard = Scoreboard(self)

        self.sound = SoundManager()
        self.sound.play_music()

        self.menu = sb.Menu(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.aliens_bullets = pygame.sprite.Group()
        self.aliens_bullet_last_tick = 0
        self.bonuses = pygame.sprite.Group()

    def run_game(self):
        clock = pygame.time.Clock()

        # Events
        pygame.time.set_timer(ALIENS_FIRE_EVENT, 3000)

        # Main loop
        while True:
            # Limit the framerate and get the delta time
            self.settings.delta_time = clock.tick(100)
            # Ignore wait() execution result
            if self.settings.delta_time > 500:
                continue

            self.settings.delta_time = 11

            self._check_events()

            if self.stats.game_state == GameState.PLAY:
                self.background.update()
                self.ship.update()
                self._update_aliens()
                self._update_bullets()
                self._update_bonuses()
            # elif:  # TODO set to RECORDS statistic
            else:
                self.menu.update()

            self._update_screen()

    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()

        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        self._check_aliens_bottom()

    def _check_bullet_collisions(self):
        collisions = pygame.sprite.groupcollide(self.aliens_bullets, self.bullets, True, True)

        if collisions:
            for bullets in collisions.values():
                self.sound.play('explosion_bullets')

    def _check_bullet_alien_collisions(self):
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if collisions:
            for aliens in collisions.values():
                self.sound.play('explosion')
                self.stats.score += self.settings.alien_points * len(aliens)
                for alien in aliens:
                    self._add_bonus(alien.rect)

            self.scoreboard.prep_score()
            self.scoreboard.check_high_score()

        if not self.aliens:
            self.bullets.empty()
            self.aliens_bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

            self.stats.level += 1
            self.scoreboard.prep_level()

    def _check_bullet_ship_collisions(self):
        collisions = pygame.sprite.spritecollide(self.ship, self.aliens_bullets, True)

        if collisions:
            self._ship_hit()

    def _check_aliens_bottom(self):
        screen_rect = self.screen.get_rect()

        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break

    def _update_bullets(self):
        self.bullets.update()
        self.aliens_bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        for bullet in self.aliens_bullets.copy():
            if bullet.rect.top >= self.screen.get_rect().height:
                self.aliens_bullets.remove(bullet)

        self._check_bullet_alien_collisions()
        self._check_bullet_ship_collisions()
        self._check_bullet_collisions()

    def _create_fleet(self):
        alien = Alien(self)
        alian_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alian_width)
        number_aliens_x = available_space_x // (2 * alian_width)

        ship_height = self.ship.rect.height
        available_space_y = self.settings.screen_height - (3 * alien_height) - ship_height
        number_rows = available_space_y // (2 * alien_height)

        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien_height + 2 * alien_height * row_number
        self.aliens.add(alien)

    def _show_ship_explosion(self):
        # Show ship explosion
        self.ship.show_explosion_ship_img()
        self._update_screen()
        # Show standard ship image
        self.ship.show_ship_img()

    def _ship_hit(self):
        self._show_ship_explosion()
        self.sound.play('explosion_ship')

        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
            self.scoreboard.prep_ships()

            self.aliens.empty()
            self.bonuses.empty()
            self.aliens_bullets.empty()
            self.bullets.empty()

            self._create_fleet()
            self.ship.center_ship()

            # Making the script wait for 2 seconds
            pygame.time.delay(2000)
        else:
            # TODO set to RECORDS statistic

            # Making the script wait for 2 seconds
            pygame.time.delay(2000)

            self.stats.game_state = GameState.STOP

    def _check_fleet_edges(self):
        alien: Alien
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed

        self.settings.fleet_direction *= -1

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEMOTION:
                self.menu.check_mouse_motion_event(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.menu.check_mouse_events()
            elif event.type == ALIENS_FIRE_EVENT:
                self._aliens_fire()
            elif event.type == DISABLE_FIRE_BONUS:
                self.settings.ship_fire_bonus = False

    def _aliens_fire(self):
        if self.stats.game_state == GameState.PLAY:
            aliens_count = len(self.aliens)
            random_index = random.randint(0, aliens_count - 1)
            alien = self.aliens.sprites()[random_index]
            self._alien_fire_bullet(alien)

    def call_play_button(self):
        if self.stats.game_state == GameState.STOP:
            self.background.reset_state()
            self.settings.initialize_dynamic_settings()
            self.stats.reset_stats()

            self.scoreboard.prep_score()
            self.scoreboard.prep_level()
            self.scoreboard.prep_ships()

            self.aliens.empty()
            self.bonuses.empty()
            self.aliens_bullets.empty()
            self.bullets.empty()

            self._create_fleet()
            self.ship.center_ship()

        self.stats.game_state = GameState.PLAY

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_ESCAPE:
            self.stats.game_state = GameState.PAUSE
        # TODO Temporary
        elif event.key == pygame.K_e:
            self.settings.mushroom_style_bonus = not self.settings.mushroom_style_bonus

    def _alien_fire_bullet(self, alien):
        new_bullet = Bullet(self, alien.rect.midbottom, 180, "bullet_green")
        self.aliens_bullets.add(new_bullet)
        self.sound.play('shot')

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            if self.settings.ship_fire_bonus:
                self.bullets.add(Bullet(self, self.ship.rect.midtop, 0, "bullet"))
                self.bullets.add(Bullet(self, self.ship.rect.midtop, 30, "bullet"))
                self.bullets.add(Bullet(self, self.ship.rect.midtop, -30, "bullet"))
            else:
                self.bullets.add(Bullet(self, self.ship.rect.midtop, 0, "bullet"))
            self.sound.play('shot')

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self):
        if self.stats.game_state == GameState.PLAY:
            # PLAY

            self.background.draw()
            self.ship.draw()
            self.scoreboard.draw()

            self.aliens.draw(self.screen)
            self.bullets.draw(self.screen)
            self.aliens_bullets.draw(self.screen)
            self.bonuses.draw(self.screen)
        else:
            # MENU

            self.menu.draw()

        pygame.display.flip()

    # Bonuses

    def _update_bonuses(self):
        self.bonuses.update()

        for bonus in self.bonuses.copy():
            if bonus.rect.top >= self.screen.get_rect().height:
                self.bonuses.remove(bonus)

        self._check_bonus_collisions()

    def _add_bonus(self, alien_rect):
        if random.randint(1, 10) == 1:
            bonus_type: BonusType = None
            if random.randint(1, 3) == 1:
                bonus_type = BonusType.LIFE
            elif random.randint(1, 3) == 1:
                bonus_type = BonusType.FIRE
            elif random.randint(1, 3) == 1:
                bonus_type = BonusType.MUSHROOM_STYLE

            if bonus_type is not None:
                new_bonus = Bonus(self, alien_rect.midbottom, bonus_type)
                self.bonuses.add(new_bonus)

    def _check_bonus_collisions(self):
        collisions = pygame.sprite.spritecollide(self.ship, self.bonuses, False)

        if collisions:
            for bonus in collisions:
                bonus_type: BonusType = bonus.bonus_type
                if bonus_type == BonusType.LIFE:
                    # Life
                    if self.settings.ship_limit >= self.stats.ships_left:
                        self.bonuses.remove(bonus)
                        self.bonus_life()
                elif bonus_type == BonusType.FIRE:
                    # if not self.settings.ship_fire_bonus:
                    self.bonuses.remove(bonus)
                    self.settings.ship_fire_bonus = True
                    pygame.time.set_timer(DISABLE_FIRE_BONUS, 10000)
                elif bonus_type == BonusType.MUSHROOM_STYLE:
                    self.bonuses.remove(bonus)
                    # TODO handle MUSHROOM_STYLE bonus!!!!
                else:
                    raise ValueError(f"Unknown bonus type: {bonus.bonus_type}")

    def bonus_life(self):
        self.stats.ships_left += 1
        self.scoreboard.prep_ships()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
