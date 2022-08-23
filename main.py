from machine import Pin, I2C
from time import sleep
import BME280

SDA_I2CADDR = Pin(21)
SCL_I2CADDR = Pin(22)
I2CBUS_FREQ = 10000

# ESP32 - Pin assignment
i2c = I2C(scl=SCL_I2CADDR, sda=SDA_I2CADDR, freq=I2CBUS_FREQ)

while True:
  bme = BME280.BME280(i2c=i2c)
  temp = bme.temperature
  hum = bme.humidity
  pres = bme.pressure

  print('Temperature: ', temp)
  print('Humidity: ', hum)
  print('Pressure: ', pres)
  print()

  sleep(5)
