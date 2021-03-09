
WIDTH = 1000
HEIGHT= 800

ash = Actor("ash1", (WIDTH/2, HEIGHT/2))

ash_down = ['ash1','ash2','ash3']
ash_down_int = 0

def draw():
    screen.clear()
    screen.fill((0,0,0))
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
    animate(ash, tween="accelerate", pos=(ash.x, ash.y + 50))

def move_ash():
    if(keyboard.down):
        ash.image = 'ash2'
        clock.schedule_interval(switch_ash, 0.01)
    if(keyboard.space):
        animate(ash,tween='bounce_start',on_finished=end_jump, pos=(ash.x, ash.y-50))
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