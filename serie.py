import shiftpi
SER_PIN=17
RCLK_PIN=27
SRCLK_PIN=22
shiftpi.pinsSetup({"ser": SER_PIN, "rclk": RCLK_PIN, "srclk": SRCLK_PIN}

shiftpi.digitalWrite(1, shiftpi.HIGH)