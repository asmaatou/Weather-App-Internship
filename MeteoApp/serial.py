import serial

SERIAL_PORT = '/dev/ttyAMA0'
SERIAL_RATE = 9600


def main():
    ser = serial.Serial(SERIAL_PORT, SERIAL_RATE)
    while True:
        reading = ser.readline().decode('utf-8')
        print(reading)


if __name__ == "__main__":
    main()