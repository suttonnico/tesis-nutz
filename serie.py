import shiftpi
import RPi.GPIO as GPIO

shiftpi.digitalWrite(1, shiftpi.LOW)

# switch it on
def go():
    shiftpi.digitalWrite(0, shiftpi.HIGH)

def stop():
    shiftpi.digitalWrite(0, shiftpi.LOW)

def openA1():
    shiftpi.digitalWrite(1, shiftpi.HIGH)


def closeA1():
    shiftpi.digitalWrite(1, shiftpi.LOW)


def openA2():
    shiftpi.digitalWrite(2, shiftpi.HIGH)

def closeA2():
    shiftpi.digitalWrite(2, shiftpi.LOW)


def closeB1():
    shiftpi.digitalWrite(4, shiftpi.LOW)

def openB1():
    shiftpi.digitalWrite(4, shiftpi.HIGH)

def closeB2():
    shiftpi.digitalWrite(5, shiftpi.LOW)

def openB2():
    shiftpi.digitalWrite(5, shiftpi.HIGH)


def openB3():
    shiftpi.digitalWrite(6, shiftpi.HIGH)

def openA3():
    shiftpi.digitalWrite(3, shiftpi.HIGH)


def closeB3():
    shiftpi.digitalWrite(6, shiftpi.LOW)


def closeA3():
    shiftpi.digitalWrite(3, shiftpi.LOW)

def leftSmall():
    closeA3()
    openA2()
    openA1()


def leftBig():
    closeA2()
    openA1()

def leftBad():
    openA3()
    openA2()
    openA1()


def rightSmall():
    bus.write_byte(addr_arduino, ord('D'))


def rightBig():
    bus.write_byte(addr_arduino, ord('E'))


def rightBad():
    bus.write_byte(addr_arduino, ord('F'))


