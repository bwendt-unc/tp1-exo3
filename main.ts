let x = 0
let p1y = 0
let p2y = -1
let p3y = -2
basic.forever(function () {
    x = randint(0, 4)
    for (let index = 0; index < 7; index++) {
        basic.pause(500)
        led.unplot(x, p1y)
        led.unplot(x, p2y)
        led.unplot(x, p3y)
        p1y += 1
        p2y += 1
        p3y += 1
        led.plotBrightness(x, p1y, 255)
        led.plotBrightness(x, p2y, 154)
        led.plotBrightness(x, p3y, 53)
    }
})
