import serial


class SerialPort:
    def __init__(self, comport: str, baudrate: int = 9600, timeout: int = 1):
        self.serial_port = serial.Serial(port=comport, baudrate=baudrate, timeout=timeout)



if __name__ == '__main__':
    from serial.tools.list_ports import comports

    ports_avail = comports()
    for i, port in enumerate(ports_avail):
        print(i, str(port))
    index = int(input())

    serial_port = SerialPort(
        str(ports_avail[index]).split()[0]
    )

    flight_file_path = "/home/phoenix/Desktop/Projects/Radiosonde-Ground-Station-Software/src/export/sample"
    serial_port.read_port(flight_file_path)
