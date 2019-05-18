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

def open():
        bus.write_byte(addr,ord('U'))

def close():
        bus.write_byte(addr,ord('u'))