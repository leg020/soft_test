import serial

class ScanerWindow:

    def __init__(self, port: str, baudrate: int):
        self.port = serial.Serial(port=port, baudrate=baudrate, timeout=0)

    def add_mark(self, mark: str):
        mark = mark.encode('utf-8')
        self.port.write(mark)

    def close_port(self):
        self.port.close()
