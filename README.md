# PX4Flow-Python-Test
This is a test set for testing PX4Flow I2C on with Python for RPI &  BBB

Make sure that the PX4Flow is detectected by issuing command i2cdetect -r -y 1 (or 2 for BBB) and you should see "42"

Edit the  def __init__(self, address, bus=smbus.SMBus(2)): and put the appropriate bus 1 for RPI or 2 for BBB

Launch test


