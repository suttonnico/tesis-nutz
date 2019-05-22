from smbus import SMBus
#1 stop
#2 go nunca
#3 reversa
#4 corriente
#+ mas rapido
#- mas lento
#ABCDEF puertas
addr = 0x8 # bus address
bus = SMBus(1) # indicates /dev/ic2-1

 # switch it on
def go():
		bus.write_byte(addr,ord('3'))

def stop():
		bus.write_byte(addr,ord('1'))

def openA1():
		bus.write_byte(addr,ord('U'))

def closeA1():
		bus.write_byte(addr,ord('u'))

def openA2():
		bus.write_byte(addr,ord('V'))

def closeA2():
		bus.write_byte(addr,ord('v'))

def closeB1():
		bus.write_byte(addr,ord('x'))


def openB1():
	bus.write_byte(addr, ord('X'))

def closeB2():
	bus.write_byte(addr, ord('y'))