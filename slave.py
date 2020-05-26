from smbus import SMBus

addr = 0x4
bus = SMBus(1)



while(1):
    data = bus.read_byte(addr)
    if data == 0x1:
        print("Temperature")
    
    elif data == 0x2:
        print("Humidity")
    

