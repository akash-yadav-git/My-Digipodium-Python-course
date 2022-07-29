import pgzrun
HEIGHT=500
WIDTH=600
p= Rect((40,40),(50,50))

def draw():
    screen.fill('white')
    screen.draw.filled_rect(p,'green')

def update():
    control_player()

def control_player():
    if keyboard.RIGHT:
        p.x += 2
    if keybord.LEFT:
        p.x += -2

pgzrun.go()
