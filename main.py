import serial
import time

try:
    lcd=serial.Serial("/dev/ttyUSB0",115200,timeout=0.5) #使用USB连接串行口
    if (lcd.isOpen()==True):
        print("串口打开成功")
    lcd.write("CLR(0);SBC(0);DC32(0,0,'零一二三四五六七八九',16);\r\n".encode('gbk'));
    time.sleep(1);
    lcd.write("DC32(0,32,'ABCDEFGHIJKLMNOPQRST',16);\r\n".encode('gbk'));
except Exception as e:
    print("串口打开异常:",e);
