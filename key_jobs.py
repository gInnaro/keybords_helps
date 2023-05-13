import serial
import keyboard
from db import btn_set
from threading import Thread


class Jobs():
    def __init__(self, status):
        super().__init__()
        self.status = status
        self.btn_set = btn_set('btn_setting.db')

    def starts(self, status='start'):
        global stop_threads
        stop_threads = False
        th2 = Thread(target=self.jobs, args=())
        if status == 'start':
            th2.start()

    def connect(self, ports):
        global port
        port = ports
        global ser
        try:
            ser = serial.Serial(port, 9600)
        except serial.serialutil.SerialException:
            self.status['text'] = 'Нет связи'
        else:
            self.starts()
            self.status['text'] = 'Подключено'


    def rules(self, key):
        var1, var2, var3 = key[0], key[1], key[2]
        if var1 != '':
            if var2 != '':
                if var3 != '':
                    keyboard.send(f'{var1}+{var2}+{var3}')
                else:
                    keyboard.send(f'{var1}+{var2}')
            else:
                if var3 != '':
                    keyboard.send(f'{var1}+{var3}')
                else:
                    keyboard.send(f'{var1}')
        else:
            if var2 != '':
                if var3 != '':
                    keyboard.send(f'{var2}+{var3}')
                else:
                    keyboard.send(f'{var2}')
            else:
                keyboard.send(f'{var3}')

    def jobs(self):
        while True:
            datas = ser.readline()
            data = datas.decode('utf-8').split('\r\n')[0]
            if data == "BTN_PIN_1":
                self.rules(self.btn_set.key_commands(1))
            if data == "BTN_PIN_2":
                self.rules(self.btn_set.key_commands(2))
            if data == "BTN_PIN_3":
                self.rules(self.btn_set.key_commands(3))
            if data == "BTN_PIN_4":
                self.rules(self.btn_set.key_commands(4))
            if data == "BTN_PIN_5":
                self.rules(self.btn_set.key_commands(5))
            if data == "BTN_PIN_6":
                self.rules(self.btn_set.key_commands(6))
            if data == "BTN_PIN_7":
                self.rules(self.btn_set.key_commands(7))
            if data == "BTN_PIN_8":
                self.rules(self.btn_set.key_commands(8))

    def check_led(self, led):
        if led == 'LED_1':
            ser.write(b'led_1')
        if led == 'LED_2':
            ser.write(b'led_2')
        if led == 'LED_3':
            ser.write(b'led_3')
        if led == 'LED_4':
            ser.write(b'led_4')
        if led == 'LED_5':
            ser.write(b'led_5')
        if led == 'LED_6':
            ser.write(b'led_6')
        if led == 'LED_7':
            ser.write(b'led_7')
        if led == 'LED_8':
            ser.write(b'led_8')

    def sends_color(self, commands):
        try:
            ser.write(commands.encode('utf-8'))
        except NameError:
            print('err')
        except serial.serialutil.SerialException:
            print('err')
        except serial.serialutil.SerialTimeoutException:
            print("err")