import kociemba
from scrambler import get_cube_string
from scrambleGenerator import gen_scramble
import serial
import time

def main():
    print("STARTING!")
    arduino = serial.Serial(port='/dev/ttyACM0', baudrate=115200, timeout=.1)
    scramble = gen_scramble()[:-4]
    cube = get_cube_string(scramble).upper()
    print("Scramble: " + scramble)
    print("Solution: " + kociemba.solve(cube)) # 54 letters as labled in notation.txt (example of solver : UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB )


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data
