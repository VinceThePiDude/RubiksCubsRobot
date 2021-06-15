import kociemba
from scrambler import get_cube_string
from scrambleGenerator import gen_scramble

def main():
    print("STARTING!")
    scramble = gen_scramble()[:-4]
    cube = get_cube_string(scramble).upper()
    cube = cube.replace("G", "F")
    cube = cube.replace("W", "U")
    cube = cube.replace("Y", "D")
    cube = cube.replace("O", "L")
    print("Scramble: " + scramble)
    print("Solution: " + kociemba.solve(cube)) # 54 letters as labled in notation.txt (example of solver : UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB )


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

