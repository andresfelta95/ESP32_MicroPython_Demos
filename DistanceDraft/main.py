from machine import Pin, time_pulse_us
import time

SOUND_SPEED=340 # Vitesse du son dans l'air
TRIG_PULSE_DURATION_US=10

trig_pin = Pin(5, Pin.OUT)
echo_pin = Pin(18, Pin.IN)
led_pin = Pin(2, Pin.OUT)
flag = 0

while True:
    # toggle led
    if flag == 0:
        led_pin.value(1)
        flag = 1
    else:
        led_pin.value(0)
        flag = 0
    # Prepare le signal
    trig_pin.value(0)    
    time.sleep_us(5)
    # Créer une impulsion de 10 µs
    trig_pin.value(1)    
    time.sleep_us(TRIG_PULSE_DURATION_US)
    trig_pin.value(0)

    ultrason_duration = time_pulse_us(echo_pin, 1, 30000) # Renvoie le temps de propagation de l'onde (en µs)
    distance_cm = SOUND_SPEED * ultrason_duration / 20000

    print(f"Distance : {distance_cm} cm")
    time.sleep_ms(500)