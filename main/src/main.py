from pyray import *
import math

class player:
    def __init__(self, x, y, w, h, hp, speed):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.hp = hp
        self.speed = speed
    def move(self, left, right, up, down):
        self.x += self.speed*(is_key_down(right)-is_key_down(left))
        self.y += self.speed*(is_key_down(down)-is_key_down(up))
    def draw(self, image=None):
        if not image is None:
            pass
        else:
            draw_rectangle_v(Vector2(self.x-self.w/2,self.y-self.h/2),Vector2(self.w,self.h),RED)


init_window(750,750,">///< s-senpai don't touch me there")
set_target_fps(60)

player1 = player(375,375,20,20,10,3)

while not window_should_close():
    begin_drawing()
    clear_background(WHITE)
    
    ## player
    player1.move(KEY_LEFT,KEY_RIGHT,KEY_UP,KEY_DOWN)
    player1.draw()

    if is_key_pressed(KEY_SPACE):
        player1.hp -= 1
        

    ## health bar
    for i in range(player1.hp):
        draw_rectangle(20,20+30*i,20,20,PINK)



    end_drawing()
close_window()