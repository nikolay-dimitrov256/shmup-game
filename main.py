import os
from pygame.locals import MOUSEMOTION, KEYDOWN, K_ESCAPE, MOUSEBUTTONDOWN
# from app_config import *
from enemies import *
from player import Player
from sprite_groups import *


def draw_score():
    score_text = f'Enemies killed: {Enemy.enemies_killed}'
    score_surf = game_font.render(score_text, True, 'blue')
    score_rect = score_surf.get_rect(topleft=(10, 10))
    screen.blit(score_surf, score_rect)


def draw_lives():
    lives_text = str(player.lives)
    lives_surf = game_font.render(lives_text, True, 'blue')
    lives_rect = lives_surf.get_rect(center=(15, HEIGHT - 20))
    screen.blit(lives_surf, lives_rect)


# pygame.init()

# screen = pygame.display.set_mode((WIDTH, HEIGHT))
timer = pygame.time.Clock()
font_location = os.path.join('./', 'Fonts', 'ubuntu', 'Ubuntu-R.ttf')
game_font = pygame.font.Font(font_location, 20)

ADD_ENEMY1 = pygame.USEREVENT + 1
pygame.time.set_timer(ADD_ENEMY1, 1000, loops=30)

pygame.mouse.set_visible(False)

player = Player()
all_sprites.add(player)


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

        elif event.type == MOUSEMOTION:
            mouse_position = pygame.mouse.get_pos()
            player.move_player(mouse_position)

        elif event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                new_bullet = player.current_weapon(player.rect.midtop)
                all_sprites.add(new_bullet)
                player_bullets.add(new_bullet)
                player.shooting = True

        elif event.type == ADD_ENEMY1:
            new_enemy = Enemy1()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)

    screen.fill('white')

    for enemy in enemies:
        if enemy.dead:
            continue
        if enemy.shoot:
            bullet = enemy.bullet(enemy.rect.midbottom)
            enemy_bullets.add(bullet)
            all_sprites.add(bullet)

        for bullet in player_bullets:
            if enemy.rect.colliderect(bullet.rect):
                enemy.get_hit(bullet.damage)
                enemy.got_hit_counter = 3
                bullet.kill()

    for bullet in enemy_bullets:
        if player.rect.colliderect(bullet.rect):
            player.get_hit()
            bullet.kill()

    draw_score()
    draw_lives()

    # for b in player_bullets:
    #     b.animate()
    #
    # for b in enemy_bullets:
    #     b.animate()
    #
    # for e in enemies:
    #     e.animate()

    for item in all_sprites:
        item.animate()
        item.update()
        screen.blit(item.surf, item.rect)
    pygame.display.flip()
    timer.tick(fps)

pygame.quit()
