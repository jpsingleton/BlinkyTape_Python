from BlinkyTape import BlinkyTape
import time

#bb = BlinkyTape('/dev/tty.usbmodemfa131')
bb = BlinkyTape('COM8')

while True:

    for x in range(60):
        bb.sendPixel(100, 100, 100)
    bb.show()

    time.sleep(.5)

    for x in range(60):
        bb.sendPixel(0, 0, 0)
    bb.show()

    time.sleep(.5)
