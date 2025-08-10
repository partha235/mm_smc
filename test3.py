# this program is to test HC-SR04 ultrasonic sensor
from machine import Pin, time_pulse_us
import time

trigger = Pin(25, Pin.OUT)
echo = Pin(26, Pin.IN)

def get_distance():
    trigger.off()
    time.sleep_us(2)
    trigger.on()
    time.sleep_us(10)
    trigger.off()



    # Measure echo pulse duration in microseconds
    duration = time_pulse_us(echo, 1, 30000)  # Timeout = 30ms

    # Calculate distance in cm (sound speed = 34300 cm/s)
    distance_cm = (duration / 2) / 29.1
    return distance_cm

# Main loop
while True:
    dist = get_distance()
    print("Distance: {:.2f} cm".format(dist))
    time.sleep(1)