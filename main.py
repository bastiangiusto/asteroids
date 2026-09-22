import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Initialize pygame
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt: float = 0.0

    # Creating pygame groups to organize the objects
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    # Spawning a player object
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Starting the game loop
    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        
        # Render the player on the screen before flipping the screen
        for player in drawable:
            player.draw(screen)

        # Rotate player if key is pressed
        updatable.update(dt)

        
        # Updating the screen
        pygame.display.flip()


        # Updating dt
        dt = clock.tick(60) / 1000




if __name__ == "__main__":
    main()
