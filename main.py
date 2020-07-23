x = 0
p1y = 0
p2y = -1
p3y = -2

def on_forever():
    global x, p1y, p2y, p3y
    x = randint(0, 5)
    if p3y < 8:
        for index in range(7):
            basic.pause(500)
            led.unplot(x, p1y)
            led.unplot(x, p2y)
            led.unplot(x, p3y)
            p1y += 1
            p2y += 1
            p3y += 1
            led.plot_brightness(x, p1y, 255)
            led.plot_brightness(x, p2y, 154)
            led.plot_brightness(x, p3y, 53)
basic.forever(on_forever)
