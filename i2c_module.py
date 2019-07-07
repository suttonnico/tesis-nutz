from smbus import SMBus

# 1 stop
# 2 go nunca
# 3 reversa
# 4 corriente
# + mas rapido
# - mas lento
# ABCDEF puertas
addr_arduino = 0x8  # bus address
bus = SMBus(1)  # indicates /dev/ic2-1


# switch it on
def go():
    bus.write_byte(addr_arduino, ord('3'))


def stop():
    bus.write_byte(addr_arduino, ord('1'))


def openA1():
    bus.write_byte(addr_arduino, ord('U'))


def closeA1():
    bus.write_byte(addr_arduino, ord('u'))


def openA2():
    bus.write_byte(addr_arduino, ord('V'))


def closeA2():
    bus.write_byte(addr_arduino, ord('v'))


def closeB1():
    bus.write_byte(addr_arduino, ord('x'))


def openB1():
    bus.write_byte(addr_arduino, ord('X'))


def closeB2():
    bus.write_byte(addr_arduino, ord('y'))

def openB2():
    bus.write_byte(addr_arduino, ord('Y'))

def openB3():
    bus.write_byte(addr_arduino, ord('Z'))

def openA3():
    bus.write_byte(addr_arduino, ord('W'))

def closeB3():
    bus.write_byte(addr_arduino, ord('z'))

def closeA3():
    bus.write_byte(addr_arduino, ord('w'))