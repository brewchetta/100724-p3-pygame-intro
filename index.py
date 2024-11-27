# Example file showing a basic pygame "game loop"
import pygame
from creature import Creature

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 960))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

bg = pygame.image.load("assets/truck-stop-bathroom.jpg")
brush = pygame.image.load("assets/toilet-brush-100.png")
poop = pygame.image.load("assets/cute-poop-50.png")
rainbow = pygame.image.load("assets/rainbow-poop-50.png")

Creature(50, 50, poop, rainbow)
Creature(500, 500, poop, rainbow)
Creature(1000, 100, poop, rainbow)

while running:

    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("light blue")

    screen.blit(bg, (0,0))
    # pygame.draw.rect(screen, "red", pygame.Rect(player_pos.x, player_pos.y, 100, 100))
    screen.blit(brush, (player_pos.x,player_pos.y))

    for critter in Creature.alive_creatures:
        screen.blit(critter.alive_image, (critter.x, critter.y))
        # pygame.draw.rect(screen, "green", pygame.Rect(critter.x, critter.y, 100, 100))
        in_x = (critter.x - 50) <= player_pos.x <= (critter.x + 50)
        in_y = (critter.y - 50) <= player_pos.y <= (critter.y + 50)
        if in_x and in_y:
            critter.remove()

    for critter in Creature.dead_creatures:
        screen.blit(critter.dead_image, (critter.x, critter.y))
        # pygame.draw.rect(screen, "blue", pygame.Rect(critter.x, critter.y, 100, 100))


    if len( Creature.alive_creatures ) == 0:
        running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt


    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()