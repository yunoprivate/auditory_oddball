# arduino.py
import serial.tools.list_ports

class DummyTTL:
    def send(self, code: bytes):
        print(f'[DummyTTL] send: {code}')
    
    def close(self):
        pass

class TTLSender:
    def __init__(self, port: str, baudrate=115200):
        self.serial = serial.Serial(port, baudrate)

    def send(self, code: bytes):
        self.serial.write(code)

    def close(self):
        self.serial.close()

def find_arduino():
    for port in serial.tools.list_ports.comports():
        if 'Arduino' in port.description or 'CH340' in port.description:
            return port.device
        
    return None

def create_ttl():
    port = find_arduino()

    if port:
        print(f'Found Arduino on {port}')
        return TTLSender(port)
    else:
        print('Arduino not found. Using DummyTTL.')
        return DummyTTL()

if __name__ == '__main__':
    import time
    print('create_ttl() test')
    ttl = create_ttl()
    time.sleep(2)
    print('send TTL 1')
    ttl.send(b'1')
    time.sleep(2)
    print('send TTL 2')
    ttl.send(b'2')

    ttl.close()