import time
from Adafruit_LED_Backpack import Matrix8x8

# Initialize the LED matrix
matrix = Matrix8x8.Matrix8x8()
matrix.begin()

# Set the LED at the intersection of the 3rd column and the 4th row to on
matrix.set_pixel(3, 4, 1)

# Blink the LED 10 times
for i in range(10):
    matrix.write_display()
    time.sleep(0.5)
    matrix.clear()
    matrix.write_display()
    time.sleep(0.5)
