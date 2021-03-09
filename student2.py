import random
alien = Actor('alien')
alien.pos = 100, 56
ship = Actor('ship')
ship.pos = 100, 400
rocket = Actor('racket')
rocket.pos = 100, 400
asteroid = Actor('asteroid')
asteroid.pos = random.randint(0,1000),10
barrier1 = Actor('barrier')
barrier1.pos = 400, 200
barrier2 = Actor('barrier')
barrier2.pos = 700, 250
heart1 = Actor('heart')
heart1.pos = 900, 30
heart2 = Actor('heart')
heart2.pos = 950, 30
heart3 = Actor('heart')
heart3.pos = 850, 30

WIDTH = 1000
HEIGHT = 575
hearts = [heart1,heart2,heart3]
heart = 3
game_over = False
score = 0
timer = 1000
level = 1

def draw():
    screen.clear()
    if (game_over == True):
        screen.blit('gameover', (0,0))
    elif((game_over is False) and (level is 1)):
        screen.blit('gamebackground', (0,0))
        alien.draw()
        ship.draw()
        rocket.draw()
        screen.draw.text("Level 1",(300,0))
        screen.draw.text("score = "+ str(score),(0,0))
        screen.draw.text("timer = "+ str(timer),(0,30))
        asteroid.draw()
        hearts[0].draw()
        hearts[1].draw()
        hearts[2].draw()
    elif((game_over is False) and (level is 2)):
        screen.blit('backround_2', (0,0))
        alien.draw()
        ship.draw()
        rocket.draw()
        screen.draw.text("Level2",(300,0))
        screen.draw.text("score = "+ str(score),(0,0))
        screen.draw.text("timer = "+ str(timer),(0,30))
        asteroid.draw()
        hearts[0].draw()
        hearts[1].draw()
        hearts[2].draw()
        barrier1.draw()
        barrier2.draw()

######################################## Rocket Function ##############################################

def move_rocket(ship):
    offset = 0

    if keyboard.lshift:
        offset = 15
    if keyboard.left:
        rocket.x -= 5 + offset
        ship.x -= 5 + offset
    if keyboard.right:
        rocket.x += 5 + offset
        ship.x += 5 + offset
    elif ((keyboard.space) & ( rocket.y == 400)):
        animate(rocket, pos =(ship.x, 0))
        hit = rocket.colliderect(barrier1)
        if hit == True:
            rocket.y = ship.y
            screen.clear()
        else:
            clock.schedule_unique(reset_rocket, 1)
            screen.clear()
            #sounds.combine.play()
    if ship.x > WIDTH:
        ship.x = 0
        rocket.x = 0
    if ship.x < 0:
        ship.x = WIDTH
        rocket.x = WIDTH

def reset_rocket():
    rocket.x = ship.x
    rocket.y = 400

def set_ship_normal():
    ship.image = 'ship'
    rocket.image = 'racket'

#################################### Asteroid Function ##################################

def asteroid_drop(asteroid):
    asteroid.y += 10
    if asteroid.y > HEIGHT:
        asteroid.pos = random.randint(0,1000),10
    collide = asteroid.colliderect(ship)
    if collide == True:
        ship.image = 'alien_hurt'
        rocket.image = 'alien_hurt'
        clock.schedule_unique(set_ship_normal, 1)
        clock.schedule_unique(left_hart, 0.2)
        #sounds.drop.play()

#################################### Heart Function ###########################################

def left_hart():
    global heart
    global hearts
    global game_over
    heart-=1

    if(heart == 2):
       hearts[2].x = 100 + WIDTH

    elif (heart == 1):
       hearts[1].x = 100 + WIDTH

    elif (heart == 0):
       hearts[0].x = 100 + WIDTH
       game_over = True
       #sounds.gameover.play()





##################################### alien function ###################################################

def set_alien_hurt():
    alien.image = 'alien_hurt'
    #sounds.ouch.play()
    clock.schedule_unique(set_alien_normal, 0.2)


def move_alien(alien):
    collide = rocket.colliderect(alien)
    alien.left += 2
    if collide == 1:
        set_alien_hurt()
    if alien.left > WIDTH:
        alien.right = 0

def set_alien_normal():
    alien.image = 'alien'
    global score
    score += 1

def reset():
    global hearts
    global heart
    heart = 3
    global game_over

    game_over = False

    hearts[0].x = 850
    hearts[1].x = 900
    hearts[2].x = 950

def update():

    global game_over

    if ((keyboard.r) & (game_over == True)):
        reset()
    global timer
    timer -= 1
    if timer < 0:
        game_over = True
    global score
    if score == 3:
        global level
        level = 2
    if game_over == False:
        asteroid_drop(asteroid)
        move_rocket(ship)
        move_alien(alien)