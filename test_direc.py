import i2c_module as i2c
import time

sleep_time = 0.2
if __name__ == "__main__":
    i2c.go()
    time.sleep(sleep_time)
    i2c.stop()
    time.sleep(sleep_time)
    i2c.openA1()
    time.sleep(sleep_time)
    i2c.closeA1()
    time.sleep(sleep_time)
    i2c.openA2()
    time.sleep(sleep_time)
    i2c.closeA2()
    time.sleep(sleep_time)
    i2c.leftBig()
    time.sleep(sleep_time)
    i2c.leftSmall()
    time.sleep(sleep_time)
    i2c.openB1()
    time.sleep(sleep_time)
    i2c.closeB1()
    time.sleep(sleep_time)
    i2c.openB2()
    time.sleep(sleep_time)
    i2c.closeB2()
    time.sleep(sleep_time)
    i2c.rightBig()
    time.sleep(sleep_time)
    i2c.rightSmall()