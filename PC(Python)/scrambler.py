import pycuber as pc

# Cube
def get_cube_string(scramble):
    # Gets cube visualisation
    vis_cube = pc.Cube()
    vis_cube = str(vis_cube("z2 " + scramble)).upper()

    # Filters the string for letters(colors) only
    ls_cube = [val for val in list(vis_cube) if val != ' ' and val != '[' and val != ']' and val != '\n']
    U = ''.join(ls_cube[:9])
    D = ''.join(ls_cube[-9:])
    middle_cube = ls_cube[9:-9]

    # Sorts the middle part of the cube into L, F, R, B
    middle_cube = ''.join(sum([middle_cube[i + j : i + j + 3] for i in range(0, 12, 3) for j in range(0, 25, 12)], []))

    # Formats it for solver
    str_cube = U + middle_cube[18: 27] + middle_cube[9: 18] + D + middle_cube[0:9] + middle_cube[27:36]

    str_cube = str_cube.replace("G", "F")
    str_cube = str_cube.replace("W", "U")
    str_cube = str_cube.replace("Y", "D")
    str_cube = str_cube.replace("O", "L")
    return str_cube
