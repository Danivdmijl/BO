from microbit import *

while True:
    
    if button_a.is_pressed():
        for x in range(4):
            display.show(Image(
        "90909:"
        "09990:"
        "99999:"
        "09990:"
        "90909"))
            sleep(200)
            display.clear()
            sleep(200)
    if button_b.is_pressed():
        for x in range(4):
            display.show(Image.SAD)
            sleep(200)
            display.clear()
            sleep
            
    if display.read_light_level() < 100:
        display.show(Image(
        "99999:"
        "99999:"
        "99999:"
        "99999:"
        "99999"))
    else:
        display.clear()
    sleep(2000)
            
        