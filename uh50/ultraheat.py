"""UltraHeat 50 class"""
from time import sleep

import serial


class Uh50:  # pylint: disable=R0903,C0301
    """Create a class to comminicate with Ultraheat 50"""

    def __init__(self, comport) -> None:
        self.ser = serial.Serial()
        self.ser.baudrate = 300
        self.ser.bytesize = serial.SEVENBITS
        self.ser.parity = serial.PARITY_EVEN
        self.ser.stopbits = serial.STOPBITS_TWO
        self.ser.xonxoff = 0
        self.ser.rtscts = 0
        self.ser.timeout = 20
        self.ser.port = str(comport)
        try:
            self.ser.open()
        except Exception as exc:
            raise Exception(f"error while opening comport {self.ser.port}") from exc

        # Wake up
        self.ser.setRTS(False)
        self.ser.setDTR(False)
        sleep(5)
        self.ser.setDTR(True)
        self.ser.setRTS(True)

    def readdata(self):
        """open comport"""

        ir_command = "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x2F\x3F\x21\x0D\x0A"  # noqa: E501
        self.ser.write(ir_command.encode("utf-8"))
        sleep(1.5)

        # Initialize
        ir_command = "/?!\x0D\x0A"
        self.ser.write(ir_command.encode("utf-8"))
        self.ser.flush()

        # Wait for initialize confirmation
        ir_buffer = ""
        while "/LUGCUH50\r\n" not in ir_buffer:
            ir_buffer = str(self.ser.readline(), "utf-8")

            if "/?!\x0D\x0A" in ir_buffer:
                ir_buffer = str(self.ser.readline(), "utf-8")

        # Set to 2400baud
        self.ser.baudrate = 2400

        # Wait for data
        ir_buffer = ""
        ir_lines = []
        etx = False
        while not etx:
            ir_buffer = str(self.ser.readline(), "utf-8")
            if "\x03" in ir_buffer:
                etx = True
            # Strip the STX character
            ir_buffer = (
                ir_buffer.replace("\x02", "").replace("!", "").replace("\x03", "")
            )
            ir_lines.extend(ir_buffer.strip().split("\r\n"))

        # Close port and show status
        try:
            self.ser.close()
        except Exception as exc:
            raise Exception(f"could not close port {self.ser.port}") from exc

        return ir_lines
