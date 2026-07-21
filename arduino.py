# arduino.py
import serial
import serial.tools.list_ports
import time

class ArduinoHandlerBase:
    def wait_ready(self, timeout=5.0):
        pass

    def send(self, code: bytes):
        print(f'TTL send: {code}')

    def close(self):
        pass

class DummyTTL(ArduinoHandlerBase):
    def send(self, idx: int, code: bytes):
        print(f'{idx:>3} [Dummy] ', end='')
        super().send(code)

class TTLSender(ArduinoHandlerBase):
    def __init__(self, port: str, baudrate=115200):
        self.serial = serial.Serial(
            port,
            baudrate,
            write_timeout=0.1,
            timeout=0.1,
        )

    def wait_ready(self, timeout=5.0):
        start = time.time()

        while time.time() - start < timeout:
            data = self.serial.read(1)
            #print(data)

            if data == b'\xff':
                print('Arduino is ready.')
                return
            
        print('Arduino is not ready.')
        raise TimeoutError('Arduino is not ready.')

    def send(self, idx: int, code: bytes):
        self.serial.write(code)
        print(f'{idx:>3} [Arduino] ', end='')
        super().send(code)

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

def connect_arduino() -> TTLSender | DummyTTL:
    ports = [
        port
        for port in serial.tools.list_ports.comports()
        if 'Arduino' in port.description or 'CH340' in port.description
    ]

    if not ports:
        print(f'Arduino not found. Using DummyTTL.')
        return DummyTTL()
    
    print('=== Available Arduinos ===')
    print(
        f'{"Index":<6} '
        f'{"Device":<20} '
        f'{"Description":<20}'
    )
    print('-' * 48)
    for i, port in enumerate(ports):
        print(
            f'{i:<6} '
            f'{port.device:<20} '
            f'{port.description:<20}'
        )

    while True:
        try:
            idx = int(input('Select Arduino: '))
            if 0 <= idx < len(ports):
                break
            print('Invalid number.')
        except ValueError:
            print('Please enter an integer.')
    
    arduino = TTLSender(ports[idx].device)
    arduino.wait_ready()
    
    return arduino
        
if __name__ == '__main__':
    print("connect_arduino() test")
    arduino = connect_arduino()

    print('Sending TTL 1')
    arduino.send(b'\x01')
    time.sleep(1)

    print('Sending TTL 2')
    arduino.send(b'\x02')
    time.sleep(1)

    arduino.close()