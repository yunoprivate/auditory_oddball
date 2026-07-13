# arduino.py
import serial
import serial.tools.list_ports
import time

class DummyTTL:
    ''''''
    def send(self, code: bytes):
        print(f'[DummyTTL] send: {code}')
    
    def close(self):
        pass

class TTLSender:
    def __init__(self, port: str, baudrate=115200):
        self.serial = serial.Serial(
            port,
            baudrate,
            write_timeout=0.1,
        )

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

def connect_arduino() -> TTLSender | DummyTTL:
    ports = [
        port
        for port in serial.tools.list_ports.comports()
        if 'Arduino' in port.description or 'CH340' in port.description
    ]

    if not ports:
        print(f'Arduino not found. Using DummyTTL.')
        return DummyTTL()
    
    print('Available Arduinos:')
    for i, port in enumerate(ports):
        print(f"[{i}] {port.device} - {port.description}")

    while True:
        try:
            idx = int(input('Select Arduino: '))
            if 0 <= idx < len(ports):
                break
            print('Invalid number.')
        except ValueError:
            print('Please enter an integer.')
    
    arduino = serial.Serial(
        ports[idx].device,
        115200,
        write_timeout=0.1,
    )

    start = time.time()
    response = False

    while time.time() - start < 100.0:
        data = arduino.read(1)
        if data == b'\xff':
            print("responded")
            response = True
            break
    
    if not response:
        print("not responded")
        exit(1)
    
    return TTLSender(ports[idx].device)
        
if __name__ == '__main__':
    import time
    
    print('create_ttl() test')
    ttl = create_ttl()
    time.sleep(2)
    time.sleep(2)
    print('send TTL 1')
    ttl.send(b'1')
    time.sleep(2)
    print('send TTL 2')
    ttl.send(b'2')

    ttl.close()

    print("connect_arduino() test")
    arduino = connect_arduino()
    arduino.close()