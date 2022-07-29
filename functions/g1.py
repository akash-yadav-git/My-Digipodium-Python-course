from turtle import _Screen, Screen
import pgzrun
HEIGHT=500
WIDTH=500


def draw():
    Screen.fill('white')
    Screen.draw.text("hello from pygamezero",(30,30),color='red',fontsize=50)
pgzrun.go()