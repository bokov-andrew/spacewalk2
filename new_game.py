#spacewalk2
#by andrew bokov

# This lets you later run the game right from here
import pgzrun

print("Andrew is AWESOME!!!!")

WIDTH = 800
HEIGHT =600
player_x = 600
player_y =350


def draw():
    screen.blit(images.backdrop, (0, 0))
    screen.blit(images.mars, (50, 50))
    screen.blit(images.astronaut, (player_x, player_y))
    screen.blit(images.ship, (550, 300))
    
def game_loop():
    global player_x, player_y
    if keyboard.right:
        player_x += 10
    if keyboard.left:
        player_x -= 10
    if keyboard.up:
        player_y -= 10
    if keyboard.down:
        player_y += 10
        
clock.schedule_interval(game_loop, 0.03)

# This is what launches the game
pgzrun.go()
