from machine import SoftI2C, Pin 
from bmp180 import BMP180

# Use SoftI2C instead of I2C
i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=100000)

bmp180 = BMP180(i2c)
bmp180.oversample_sett = 2
bmp180.baseline = 101325  # Sea level pressure in Pa

temp = bmp180.temperature
p = bmp180.pressure
altitude = bmp180.altitude

print("Temperature:", temp, "°C")
print("Pressure:", p, "Pa")
print("Altitude:", altitude, "m")
