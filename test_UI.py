import display
import RPi.GPIO as GPIO
import time

pin_parada = 40
pin_arranque = 37
pin_arriba = 36
pin_abajo = 33

start = time.time()
while time.time()-start<60:
    if GPIO.input(pin_arriba) == GPIO.LOW:
        display.print_ln("BOTON 1")
    if GPIO.input(pin_abajo) == GPIO.LOW:
        display.print_ln("BOTON 2")
    if GPIO.input(pin_parada) == GPIO.LOW:
        display.print_ln("BOTON PARADA")
    if GPIO.input(pin_arranque) == GPIO.LOW:
        display.print_ln("BOTON ARRANQUE")