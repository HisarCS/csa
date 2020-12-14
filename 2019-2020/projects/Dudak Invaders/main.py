import pygame
import random
import math

# Initialize the pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((1600, 800))

# Background
background = pygame.image.load('background.png')

# Title and Icon
pygame.display.set_caption("Dudak Invaders")
icon = pygame.image.load('taylo.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('cemR.png')
playerX = 770
playerY = 370
playerX_change = 0
playerY_change = 0
isRight = True

# Nexus
nexusImg = pygame.image.load('nexus.png')
nexusX = 736
nexusY = 0
life = 5
lifeX = 10
lifeY = 10

# Enemy
enemyImg = []
spawnX = []
enemyX = []
enemyY = []
enemyX_change = []
num_of_enemies = 5

# Score
score_val = 0
font = pygame.font.Font('pixelfont.ttf', 32)
textX = 1425
textY = 10

# Game Over text
game_over_font = pygame.font.Font('pixelfont.ttf', 64)

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    spawnX = bool(random.getrandbits(1))
    if spawnX:
        enemyX.append(1536)
        enemyX_change.append(-1)
    else:
        enemyX.append(0)
        enemyX_change.append(1)
    enemyY.append(random.randint(0, 736))

# Bullet
# bulletImg = []
# bulletX = []
# bulletY = []
# bulletX_change = []
# num_of_bullets = 2
# bullet_loaded = 0
# bullet_state = []

bulletImgR = pygame.image.load('bulletR.png')
bulletImgL = pygame.image.load('bulletL.png')
bulletX = 0
bulletY = playerY
bulletX_change = 20
bullet_state = "ready"
is_bullet_right = True


def show_score(x, y):
    scoreText = font.render("Score:", True, (255, 0, 0))
    score = font.render(str(score_val), True, (255, 0, 0))
    screen.blit(scoreText, (x, y))
    screen.blit(score, (x + 50, y + 40))


def show_life(x, y):
    lifeText = font.render("Life:", True, (255, 0, 0))
    life_num = font.render(str(life), True, (255, 0, 0))
    screen.blit(lifeText, (x, y))
    screen.blit(life_num, (x + 50, y + 40))


def game_over_text():
    over_text = game_over_font.render("GAME OVER", True, (0, 0, 0))
    screen.blit(over_text, (500, 340))


def player(x, y, right):
    # Turns player
    global playerImg
    if not right:
        playerImg = pygame.image.load('cemL.png')
    else:
        playerImg = pygame.image.load('cemR.png')
    # Draws the player on the screen
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    # Draw enemy on these coordinates
    screen.blit(enemyImg[i], (x, y))


def fire_bulletR(x, y):
    # Fire Right bullet
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImgR, (x + 16, y + 10))


def fire_bulletL(x, y):
    # Fire Left Bullet
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImgL, (x + 16, y + 10))


def isCollision(x1, y1, x2, y2):
    distance = math.sqrt((math.pow((x1 - x2), 2)) + (math.pow((y1 - y2), 2)))
    if distance < 32:
        return True
    return False


def take_damage(x1, y1, x2, y2):
    distance = math.sqrt((math.pow((x1 - x2), 2)) + (math.pow((y1 - y2), 2)))
    if distance < 64:
        return True
    return False


running = True
while running:
    # Color of Screen (RGB)
    screen.fill((178, 160, 100))

    # Background image
    screen.blit(background, (0, 0))

    # Nexus image
    screen.blit(nexusImg, (nexusX, nexusY))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Checks if any key has been pressed
        if event.type == pygame.KEYDOWN:
            # Checks if the key pressed are the keys to move
            if event.key == pygame.K_d:
                isRight = True
                playerX_change = 10

            if event.key == pygame.K_a:
                isRight = False
                playerX_change = -10

            if event.key == pygame.K_w:
                playerY_change = -8

            if event.key == pygame.K_s:
                playerY_change = 8

            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    is_bullet_right = not isRight
                    bulletX = playerX
                    bulletY = playerY
                    if isRight:
                        bulletX_change = 20
                        fire_bulletR(bulletX, bulletY)
                    else:
                        bulletX_change = -20
                        fire_bulletL(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                playerX_change = 0
            if event.key == pygame.K_w or event.key == pygame.K_s:
                playerY_change = 0

    # Player Movement
    playerX += playerX_change
    playerY += playerY_change

    if playerY <= 0:
        playerY = 0
    elif playerY >= 736:
        playerY = 736
    if playerX <= 0:
        playerX = 0
    elif playerX >= 1536:
        playerX = 1536

    # Enemy Movement
    for i in range(num_of_enemies):

        # Game Over
        if life <= 0:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]

        # Collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = playerY
            bullet_state = "ready"
            score_val += 1
            spawnX = bool(random.getrandbits(1))
            if spawnX:
                enemyX[i] = 1536
                enemyX_change[i] = -1
            else:
                enemyX[i] = 0
                enemyX_change[i] = 1
            enemyY[i] = random.randint(0, 736)
            if score_val % 20 == 0:
                enemyImg.append(pygame.image.load('enemy.png'))
                spawnX = bool(random.getrandbits(1))
                if spawnX:
                    enemyX.append(1536)
                    enemyX_change.append(-1)
                else:
                    enemyX.append(0)
                    enemyX_change.append(1)
                enemyY.append(random.randint(0, 736))
                num_of_enemies += 1

        # Nexus Damage
        if (abs(enemyX[i] - nexusX) < 64):
            life -= 1
            spawnX = bool(random.getrandbits(1))
            if spawnX:
                enemyX[i] = 1536
                enemyX_change[i] = -1
            else:
                enemyX[i] = 0
                enemyX_change[i] = 1
            enemyY[i] = random.randint(0, 736)

        enemy(enemyX[i], enemyY[i], i)

    # Bullet Movement
    # for i in range(num_of_bullets):
    if bulletX <= 0 or bulletX >= 1568:
        bulletX = playerX
        bullet_state = "ready"
    #   fire_bullet(bulletX[i], bulletY[i], )
    if bullet_state == "fire":
        if not is_bullet_right:
            fire_bulletR(bulletX, bulletY)
        else:
            fire_bulletL(bulletX, bulletY)
        bulletX += bulletX_change

    player(playerX, playerY, isRight)
    show_score(textX, textY)
    show_life(lifeX, lifeY)
    pygame.display.update()
