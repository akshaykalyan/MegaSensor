import pp
import time
import os
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008


# Software SPI configuration:
CLK  = 11
MISO = 9
MOSI = 10
CS   = 8
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

# Hardware SPI configuration:
# SPI_PORT   = 0
# SPI_DEVICE = 0
# mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))


print('Reading MCP3008 values, press Ctrl-C to quit...')
while True:
    values = [0]*6
    for i in range(6):
        values[i] = mcp.read_adc(i)
    x=pp.pp(values)
    readings=x.get()
    print(readings)
    y=open("//home//pi//status.txt","w")
    y.write(str(readings))
    y.close()
    os.system("sshpass -p 2307 scp //home//pi//status.txt akshay@169.254.89.233://var//www//html//read")
    time.sleep(0.5)
