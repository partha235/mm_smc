from machine import SoftI2C, Pin 
from bmp180 import BMP180
from time import sleep
import dht 

# Use SoftI2C instead of I2C
i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=100000)

# dht sensor
sensor = dht.DHT11(Pin(4))

bmp180 = BMP180(i2c)
bmp180.oversample_sett = 2
bmp180.baseline = 101325  # Sea level pressure in Pa

temp = bmp180.temperature
p = bmp180.pressure
altitude = bmp180.altitude



while True:
  try:
    sleep(5)
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()
    temp_f = temp * (9/5) + 32.0
    print('Temperature: %3.1f C' %temp)
    print('Temperature: %3.1f F' %temp_f)
    print('Humidity: %3.1f %%' %hum)
    print("Temperature:", temp, "°C")
    print("Pressure:", p, "Pa")
    print("Altitude:", altitude, "m")
  except OSError as e:
    print('Failed to read sensor.')
    print("Temperature:", temp, "°C")
    print("Pressure:", p, "Pa")
    print("Altitude:", altitude, "m")