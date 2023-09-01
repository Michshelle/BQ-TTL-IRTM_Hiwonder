import smbus
import time
import numpy

class ASR:

    # Global Variables
    address = None
    bus = None
    
    ASR_RESULT_ADDR = 100

    ASR_WORDS_ERASE_ADDR = 101

    ASR_MODE_ADDR = 102

    ASR_ADD_WORDS_ADDR = 160
    #词条添加的地址，支持掉电保存

    def __init__(self, address, bus=1):
        self.address = address
        self.bus = smbus.SMBus(bus)
        
    def readByte(self):
        return self.bus.read_byte(self.address)

    def writeByte(self, val):               
        value = self.bus.write_byte(self.address, val)
        if value != 0:
            return False
        return True
    
    def writeData(self, reg, val):
        self.bus.write_byte(self.address,  reg)
        self.bus.write_byte(self.address,  val)

    def getResult(self):
        if ASR.writeByte(self, self.ASR_RESULT_ADDR):
            return -1        
        value = self.bus.read_byte(self.address)
        return value
    
    def addWords(self, idNum, words):
        buf = [idNum]       
        for i in range(0, len(words)):
            buf.append(eval(hex(ord(words[i]))))
        self.bus.write_i2c_block_data(self.address, self.ASR_ADD_WORDS_ADDR, buf)
        time.sleep(0.05)
        
    def eraseWords(self):
        result = self.bus.write_byte_data(self.address, self.ASR_WORDS_ERASE_ADDR, 0)
        time.sleep(0.06)
        if result != 0:
           return False
        return True
    
    def setMode(self, mode): 
        result = self.bus.write_byte_data(self.address, self.ASR_MODE_ADDR, mode)
        if result != 0:
           return False
        return True
        
if __name__ == "__main__":
    addr = 0x79 #传感器iic地址
    asr = ASR(addr)
    if 1:
        asr.eraseWords()
        asr.setMode(1)
        # asr.addWords(1, 'ni hao')
        # asr.addWords(2, 'kai shi')
        asr.addWords(1,'miao le ge mi mi mi')  # 唤醒
        asr.addWords(2,'da kai kong tiao zhi leng')  # 打开空调制冷
        asr.addWords(3,'kong tiao zhi re kai')  # 空调制热开
        asr.addWords(4,'guan bi kong tiao') # 关闭空调
        asr.addWords(5,'mei shi zhao ni') # 用来关掉它
