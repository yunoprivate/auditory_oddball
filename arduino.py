# arduino.py
import serial.tools.list_ports

def find_arduino():
    for port in serial.tools.list_ports.comports():
        if 'Arduino' in port.description or 'CH340' in port.description:
            print(f'Found Arduino on {port.device}')
            return port.device
    
    print('Arduino not found')
    return None
    
class TTLSender:
    def __init__(self, port: str, baudrate=115200):
        self.serial = serial.Serial(port, baudrate)

    def send(self, code: int):
        self.serial.write(bytes([code]))