from pico2d import *
import math

def move_right(start, end):
    for x in range (start, end, 3):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, 90)
        delay(0.01)
        
def move_triup(x, y):
    for i in range (0, 130, 3):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x - 3 * i, y + i * 3 * 475 / 390)    #높이 475, 넓이 780
        delay(0.01)
    
def move_tridown(x, y):
    for i in range (0, 130, 3):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x - 3 * i, y - i * 3 * 475 / 390)    #높이 475, 넓이 780
        delay(0.01)

def move_up(start, end):
    for y in range (start, end , 2):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(790, y)
        delay(0.01)

def move_down(start, end):
    for y in range (start, end , -2):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(10, y)
        delay(0.01)

def move_left(start, end):
    for x in range (start, end, -3):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, 565)
        delay(0.01)

def move_sqare():
    move_right(400, 790)
    move_up(90, 565)
    move_left(790, 10)
    move_down(565, 90)
    move_right(10, 400)
    
def move_circle():
    cx = 800 / 2
    cy = (600 + 50) / 2     # 60-> 잔디 높이
    rx = cx - 20 / 2        # 20-> 캐릭터 넓이
    ry = cy - 90            # 90-> 캐릭터 초기값
    for i in range (-180, 180, 2):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(cx + rx * math.sin(math.radians(i)), cy + ry * math.cos (math.radians(i)))
        # i /360 * 2 * math.pi -> math.radians(i)...
        delay(0.01)

def move_triangle():
    move_right(400, 790)
    move_triup(790, 90)
    move_tridown(400, 565)
    move_right(10, 400)

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

grass.draw_now(400, 30)
character.draw_now(400, 90)

while True:
    move_sqare()
    delay(0.1)
    move_triangle()
    delay(0.1)
    move_circle()
    delay(0.1)
    
close_canvas()
