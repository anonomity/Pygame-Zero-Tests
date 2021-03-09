
WIDTH = 587
HEIGHT= 423

ash = Actor("ash1", (WIDTH/2, HEIGHT/2))

ash_down = ['ash1','ash2','ash3']
ash_down_int = 0

def draw():
    screen.clear()
    screen.blit('pokemonbg',(0,0))
    ash.draw()

def switch_ash():
    global ash_down
    global ash_down_int
    if(ash_down_int == 2):

        ash_down_int = 0
        ash.image = ash_down[ash_down_int]
        ash.pos = (ash.x, ash.y+0.5)
    else:

        ash_down_int +=1
        ash.image = ash_down[ash_down_int]
        ash.pos = (ash.x, ash.y+0.5)

def end_jump():
    if(keyboard.right):
        animate(ash, duration=0.1, pos=(ash.x + 30, ash.y))
    animate(ash, tween="accelerate",duration=0.2, pos=(ash.x, ash.y + 50))

def jump_up():

    animate(ash,tween='linear', duration=0.1,on_finished=end_jump, pos=(ash.x, ash.y-50))

def move_ash():
    if(keyboard.down):
        ash.image = 'ash2'
        #clock.schedule_interval(switch_ash, 0.01)
        ash.y +=2
    if(keyboard.up):
        ash.image = 'ash2'
        ash.y -=1
    if(keyboard.space):
        clock.schedule_unique(jump_up, 0.09)

    if(keyboard.left):
        ash.image = 'ashleft'
        ash.x -= 2
    if(keyboard.right):
        ash.image ='ashright'
        ash.x +=2

    else:
        clock.unschedule(switch_ash)

def update():
    draw()
    move_ash()