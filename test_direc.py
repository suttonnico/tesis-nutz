import i2c_module as i2c
import time
sleep_time = 2
if __name__ == "__main__":
    i2c.go()                #Prender motor
    time.sleep(sleep_time)
    i2c.stop()              #Parar motor
    time.sleep(sleep_time)
    i2c.openA1()            #Abrir primer puerta izquierda
    time.sleep(sleep_time)
    i2c.closeA1()           #Cerrar primer puerta izquierda
    time.sleep(sleep_time)
    i2c.openA2()            #Abrir segunda puerta izquierda
    time.sleep(sleep_time)
    i2c.closeA2()           #Cerrar segunda puerta izquierda
    time.sleep(sleep_time)
    i2c.leftBig()           #Cerrar tercera puerta izquierda
    time.sleep(sleep_time)
    i2c.leftSmall()         #Abrir tercera puerta izquierda
    time.sleep(sleep_time)
    i2c.openB1()            #Abrir primera puerta derecha
    time.sleep(sleep_time)
    i2c.closeB1()           #Cerrar primera puerta derecha
    time.sleep(sleep_time)
    i2c.openB2()            #Abrir segunda puerta derecha
    time.sleep(sleep_time)
    i2c.closeB2()           #Cerrar segunda puerta derecha
    time.sleep(sleep_time)
    i2c.rightBig()          #Cerrar tercera puerta derecha
    time.sleep(sleep_time)
    i2c.rightSmall()        #Abrir segunda puerta derecha