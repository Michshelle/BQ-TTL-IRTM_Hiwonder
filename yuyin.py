# encoding: utf-8
'''
'''
#使用例程
import smbus
import time
import serial
import json

ser = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate=115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
    )

class Controllers:
    
    #gree_ac_YAP0F3_BQ-TTL-IRTM
    def __init__(self):
        self.greeac_dict = {
                            "close" : 
                            [0xFE,0xFD,0x03,0x85,0x01,0xC0,0x40,0xA5,0x41,0x37,0x40,0x37,0x41,0x36,0x41,0xA5,0x41,0xA5,0x41,0x36,0x41,0x36,0x41,0xA5,0x41,0xA5,0x41,0x36,0x41,0xA5,0x41,0x36,0x41,0x37,0x41,0x36,0x41,0x37,0x41,0x36,0x41,0x36,0x42,0x36,0x41,0x36,0x41,0x37,0x41,0xA5,0x41,0x36,0x41,0x37,0x40,0x37,0x44,0x33,0x41,0x37,0x41,0x36,0x41,0xA5,0x41,0x37,0x43,0xA2,0x41,0x37,0x41,0x36,0x41,0xA5,0x41,0x36,0x41,0x07,0xCE,0x41,0x36,0x41,0x36,0x41,0x37,0x41,0x36,0x41,0x37,0x41,0x36,0x41,0x37,0x41,0x36,0x41,0x37,0x41,0x36,0x41,0x37,0x41,0x36,0x41,0x37,0x41,0x36,0x41,0x37,0x40,0x37,0x41,0x36,0x41,0x37,0x41,0x36,0x41,0x37,0x41,0x36,0x41,0x36,0x42,0x36,0x41,0x36,0x41,0x37,0x41,0x36,0x41,0x37,0x41,0x36,0x44,0x34,0x41,0xA4,0x41,0xA5,0x41,0x36,0x41,0x0F,0x9F,0x03,0x85,0x01,0xBD,0x41,0xA4,0x44,0x34,0x43,0x34,0x44,0x34,0x43,0xA2,0x44,0xA2,0x44,0x33,0x44,0x34,0x44,0xA2,0x43,0xA2,0x44,0x34,0x43,0xA2,0x44,0x34,0x44,0x33,0x44,0x34,0x44,0x33,0x44,0x34,0x43,0x34,0x44,0x34,0x44,0x33,0x44,0x34,0x44,0xA1,0x44,0x34,0x43,0x34,0x44,0x34,0x43,0x34,0x44,0x34,0x43,0x34,0x44,0xA2,0x44,0xA1,0x44,0xA2,0x44,0x34,0x44,0x33,0x44,0xA2,0x43,0x34,0x44,0x07,0xCA,0x44,0x34,0x44,0x33,0x44,0x34,0x44,0x33,0x44,0x34,0x44,0x33,0x44,0x33,0x44,0x34,0x44,0x34,0x43,0x34,0x44,0x34,0x43,0x34,0x44,0x33,0x44,0x34,0x43,0x34,0x44,0x34,0x44,0x33,0x44,0x34,0x44,0x33,0x44,0x34,0x44,0x33,0x44,0x34,0x46,0x9F,0x44,0x34,0x44,0x33,0x44,0x34,0x44,0x33,0x44,0x34,0x44,0x33,0x44,0xA2,0x44,0x33,0x44,0xA2,0x44,0xFF],
                            "cooler26_4" : 
                            [0xFE, 0xFD, 0x03, 0x85, 0x01, 0xBD, 0x43, 0xA2, 0x44, 0x34, 0x43, 0x34, 0x44, 0xA2, 0x43, 0xA2, 0x44, 0xA2, 0x44, 0x33, 0x44, 0x34, 0x44, 0x34, 0x43, 0xA2, 0x43, 0x34, 0x44, 0xA2, 0x43, 0x34, 0x44, 0x33, 0x44, 0x34, 0x43, 0x34, 0x44, 0x34, 0x43, 0x34, 0x44, 0x34, 0x43, 0x34, 0x44, 0x34, 0x43, 0xA2, 0x44, 0x33, 0x44, 0x34, 0x43, 0x34, 0x44, 0x34, 0x43, 0x34, 0x44, 0x34, 0x43, 0xA2, 0x44, 0x34, 0x43, 0xA2, 0x44, 0x34, 0x43, 0x34, 0x44, 0xA2, 0x43, 0x34, 0x43, 0x07, 0xCA, 0x44, 0x34, 0x43, 0x34, 0x44, 0x34, 0x43, 0x34, 0x43, 0x35, 0x43, 0x34, 0x41, 0x36, 0x44, 0x34, 0x43, 0x34, 0x43, 0x34, 0x44, 0x34, 0x43, 0x34, 0x44, 0x34, 0x43, 0x34, 0x43, 0x35, 0x43, 0x34, 0x41, 0x36, 0x44, 0x34, 0x41, 0x36, 0x44, 0x34, 0x41, 0x36, 0x41, 0x37, 0x40, 0x37, 0x41, 0x36, 0x44, 0x34, 0x41, 0x36, 0x43, 0x35, 0x40, 0x37, 0x41, 0xA5, 0x43, 0x34, 0x41, 0xA5, 0x40, 0xA6, 0x42, 0x0F, 0x9C, 0x03, 0x84, 0x01, 0xBE, 0x40, 0xA5, 0x43, 0x34, 0x43, 0x35, 0x43, 0xA2, 0x43, 0xA3, 0x43, 0xA3, 0x42, 0x35, 0x43, 0x34, 0x43, 0x35, 0x43, 0xA3, 0x42, 0x35, 0x43, 0xA3, 0x42, 0x35, 0x40, 0x37, 0x41, 0x37, 0x43, 0x34, 0x43, 0x35, 0x40, 0x37, 0x43, 0x35, 0x43, 0x34, 0x41, 0x37, 0x42, 0xA3, 0x42, 0x35, 0x40, 0x38, 0x40, 0x37, 0x43, 0x34, 0x43, 0x35, 0x40, 0x37, 0x43, 0xA3, 0x43, 0xA2, 0x43, 0xA3, 0x43, 0x34, 0x43, 0x35, 0x42, 0xA3, 0x43, 0x35, 0x42, 0x07, 0xCC, 0x42, 0x35, 0x42, 0x35, 0x43, 0x35, 0x42, 0x35, 0x43, 0x35, 0x42, 0x35, 0x41, 0x37, 0x42, 0x35, 0x42, 0x35, 0x43, 0x35, 0x42, 0x35, 0x43, 0x35, 0x42, 0x35, 0x43, 0x35, 0x42, 0x35, 0x43, 0x35, 0x42, 0x35, 0x43, 0x35, 0x42, 0x35, 0x43, 0x35, 0x42, 0x35, 0x43, 0x35, 0x42, 0xA3, 0x43, 0x35, 0x42, 0x35, 0x43, 0x35, 0x42, 0x35, 0x42, 0x35, 0x43, 0xA3, 0x42, 0x35, 0x43, 0x35, 0x42, 0x35, 0x42, 0xFF],
                            "hot27_4" : [0xFE, 0xFD, 0x03, 0x85, 0x01, 0xBD, 0x43, 0x34, 0x44, 0x34, 0x43, 0xA2, 0x44, 0xA2, 0x43, 0x34, 0x44, 0x34, 0x43, 0x34, 0x44, 0x34, 0x43, 0xA2, 0x44, 0xA2, 0x44, 0x34, 0x43, 0xA2, 0x44, 0x34, 0x43, 0x34, 0x44, 0x34, 0x43, 0x34, 0x44, 0x34, 0x43, 0x34, 0x44, 0x34, 0x43, 0x34, 0x44, 0x34, 0x43, 0xA2, 0x44, 0x34, 0x43, 0x34, 0x44, 0x33, 0x44, 0x34, 0x43, 0x34, 0x44, 0x34, 0x43, 0xA2, 0x44, 0x34, 0x43, 0xA2, 0x44, 0x34, 0x43, 0x34, 0x44, 0xA2, 0x43, 0x34, 0x44, 0x07, 0xCB, 0x43, 0x34, 0x43, 0x34, 0x44, 0x34, 0x43, 0x34, 0x44, 0x34, 0x43, 0x34, 0x43, 0x34, 0x43, 0x35, 0x43, 0x34, 0x44, 0x34, 0x43, 0x34, 0x43, 0x35, 0x43, 0x34, 0x43, 0x34, 0x44, 0x34, 0x43, 0x34, 0x44, 0x34, 0x43, 0x34, 0x43, 0x35, 0x43, 0x34, 0x44, 0x34, 0x43, 0x34, 0x43, 0x34, 0x44, 0x34, 0x43, 0x34, 0x44, 0x34, 0x43, 0x34, 0x41, 0xA5, 0x41, 0xA4, 0x44, 0x34, 0x43, 0x34, 0x44, 0x34, 0x43, 0x0F, 0x9C, 0x03, 0x85, 0x01, 0xBD, 0x43, 0x34, 0x43, 0x35, 0x43, 0xA2, 0x43, 0xA3, 0x43, 0x34, 0x44, 0x34, 0x43, 0x34, 0x43, 0x35, 0x43, 0xA2, 0x43, 0xA3, 0x43, 0x34, 0x44, 0xA2, 0x43, 0x34, 0x44, 0x34, 0x43, 0x34, 0x43, 0x35, 0x43, 0x34, 0x43, 0x35, 0x43, 0x34, 0x43, 0x35, 0x43, 0x34, 0x43, 0xA3, 0x43, 0x34, 0x43, 0x35, 0x43, 0x34, 0x44, 0x34, 0x43, 0x34, 0x43, 0x35, 0x43, 0xA2, 0x43, 0xA3, 0x43, 0xA2, 0x44, 0x34, 0x43, 0x34, 0x44, 0xA2, 0x43, 0x34, 0x43, 0x07, 0xCC, 0x43, 0x34, 0x43, 0x35, 0x43, 0x34, 0x43, 0x35, 0x43, 0x34, 0x43, 0x35, 0x43, 0x34, 0x43, 0x34, 0x44, 0x34, 0x43, 0x35, 0x43, 0x34, 0x43, 0x34, 0x44, 0x34, 0x43, 0x34, 0x43, 0x35, 0x43, 0x34, 0x43, 0x35, 0x43, 0x34, 0x43, 0x35, 0x43, 0x34, 0x43, 0x35, 0x43, 0x34, 0x43, 0x35, 0x43, 0x34, 0x43, 0x35, 0x43, 0x34, 0x43, 0x35, 0x43, 0x34, 0x43, 0xA3, 0x43, 0x34, 0x43, 0x35, 0x43, 0x34, 0x43, 0xFF],
                            "dryer25" : 
                            [0xFE, 0xFD, 0x03, 0x7E, 0x01, 0xC4, 0x3C, 0x3B, 0x3D, 0xA8, 0x3D, 0x3B, 0x3D, 0xA8, 0x3D, 0xA9, 0x3D, 0x3A, 0x3D, 0x3B, 0x3D, 0x3A, 0x3D, 0xA9, 0x3D, 0x3A, 0x3D, 0x3B, 0x3D, 0xA8, 0x3D, 0x3B, 0x3D, 0x3A, 0x3D, 0x3B, 0x3D, 0x3A, 0x3D, 0x3B, 0x3D, 0x3A, 0x3D, 0x3B, 0x3D, 0x3A, 0x3D, 0x3B, 0x3D, 0xA8, 0x3D, 0x3B, 0x3D, 0x3B, 0x3C, 0x3B, 0x3D, 0x3B, 0x3C, 0x3B, 0x3D, 0x3A, 0x3D, 0xA9, 0x3D, 0x3A, 0x3D, 0xA9, 0x3D, 0x3A, 0x3D, 0x3B, 0x3D, 0xA9, 0x3C, 0x3B, 0x3D, 0x07, 0xD1, 0x3D, 0x3A, 0x3D, 0x3B, 0x3D, 0x3A, 0x3D, 0x3B, 0x3D, 0x3A, 0x3D, 0x3B, 0x3C, 0x3B, 0x3D, 0x3A, 0x3D, 0x3B, 0x3D, 0x3A, 0x3D, 0x3B, 0x3D, 0x3A, 0x3D, 0x3B, 0x3D, 0x3A, 0x3D, 0x3B, 0x3C, 0x3B, 0x3D, 0x3A, 0x3D, 0x3B, 0x3D, 0x3A, 0x3D, 0x3B, 0x3D, 0x3A, 0x3D, 0x3B, 0x3D, 0x3A, 0x3D, 0x3B, 0x3C, 0x3B, 0x3D, 0x3A, 0x3D, 0x3B, 0x3D, 0x3A, 0x3D, 0xA9, 0x3D, 0x3A, 0x3D, 0xA9, 0x3D, 0xA8, 0x3D, 0x0F, 0xA2, 0x03, 0x7E, 0x01, 0xC3, 0x3D, 0x3A, 0x3D, 0xA9, 0x3D, 0x3A, 0x3E, 0xA8, 0x3D, 0xA9, 0x3C, 0x3B, 0x3D, 0x3A, 0x3D, 0x3B, 0x3D, 0xA8, 0x3E, 0x3A, 0x3D, 0x3A, 0x3D, 0xA9, 0x3D, 0x3A, 0x3D, 0x3B, 0x3D, 0x3A, 0x3D, 0x3B, 0x3D, 0x3A, 0x3D, 0x3A, 0x40, 0x38, 0x3D, 0x3A, 0x3E, 0x3A, 0x3D, 0xA8, 0x40, 0x38, 0x3F, 0x38, 0x40, 0x38, 0x3D, 0x3A, 0x40, 0x38, 0x40, 0x37, 0x40, 0xA6, 0x40, 0xA6, 0x3F, 0xA6, 0x40, 0x38, 0x3F, 0x38, 0x40, 0xA6, 0x3F, 0x38, 0x40, 0x07, 0xCE, 0x40, 0x37, 0x40, 0x38, 0x40, 0x37, 0x41, 0x37, 0x41, 0x36, 0x41, 0x37, 0x40, 0x37, 0x41, 0x37, 0x43, 0x34, 0x40, 0x38, 0x42, 0x35, 0x40, 0x37, 0x43, 0x35, 0x40, 0x37, 0x43, 0x35, 0x43, 0x34, 0x43, 0x34, 0x43, 0x35, 0x43, 0x34, 0x44, 0x34, 0x43, 0xA2, 0x44, 0x34, 0x43, 0x34, 0x44, 0x34, 0x43, 0x34, 0x44, 0x33, 0x44, 0x34, 0x44, 0x33, 0x47, 0x31, 0x44, 0xA2, 0x43, 0xA2, 0x44, 0xA2, 0x43, 0xFF],
                            }

class ASR:

    # Global Variables
    address = None
    bus = None
    
    ASR_RESULT_ADDR = 100

    ASR_WORDS_ERASE_ADDR = 101

    ASR_MODE_ADDR = 102

    ASR_ADD_WORDS_ADDR = 160

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
    def setMode(self, mode): 
        result = self.bus.write_byte_data(self.address, self.ASR_MODE_ADDR, mode)
        if result != 0:
           return False
        return True
        
if __name__ == "__main__":
    addr = 0x79 #传感器iic地址
    ir = Controllers()
    asr = ASR(addr)
    
    asr.setMode(2)
    while 1:
        data = asr.getResult()
        if data == 2:
            ser.write(serial.to_bytes(ir.greeac_dict['cooler26_4']))
        elif data == 3:
            ser.write(serial.to_bytes(ir.greeac_dict['hot27_4']))
        elif data == 4:
            ser.write(serial.to_bytes(ir.greeac_dict['close']))
        elif data == 5:
            asr.setMode(3)
            time.sleep(0.2)
            asr.setMode(2)
        else:
            continue
        time.sleep(0.5)
