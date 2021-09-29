# Add your Python code here. E.g.
from microbit import *
import music

while True:
    display.scroll('HELLO YOU!')
    sleep(2000)
    
    if button_a.is_pressed():
        display.scroll("Dani")
        music.play(music.DADADADUM)
        
    elif button_b.is_pressed():
        egel = Image("00000:0900:90999:99999:90909")
        display.show(egel)
        sleep(2000)
        display.scroll('egel')