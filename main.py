import tsapp, tsappMod
import random

#tsapp.GraphicsWindow.finish_frame = exec("print(\"test\")");

display = tsapp.GraphicsWindow(width=1280,height=720,background_color=(255,0,0))

p = tsappMod.PolygonalObject(
    points=[
        [-128,-128],
        [128,-128],
        [128,128],
        [-128,256]
    ],
    color=(255,0,255),
    linewidth=0,
    show_center=True,
    show_speed=True)

display.add_object(p)

while display.is_running:
    if(tsapp.is_key_down(tsapp.K_LEFT)): p.x_speed -= 20
    if(tsapp.is_key_down(tsapp.K_RIGHT)): p.x_speed += 20
    if(tsapp.is_key_down(tsapp.K_UP)): p.y_speed -= 20
    if(tsapp.is_key_down(tsapp.K_DOWN)): p.y_speed += 20

    display.finish_frame()