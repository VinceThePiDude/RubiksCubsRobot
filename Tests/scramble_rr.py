import pycuber as pc

vis_cube = [] * 36
scramble = "z2 R U R' U' R' F R2 U' R' U' R U R' F'"
# Cube
cube = pc.Cube()
cube = str(cube(scramble))
ls_cube = [val for val in list(cube) if val != ' ' and val != '[' and val != ']' and val != '\n']
U = ''.join(ls_cube[:9])
D = ''.join(ls_cube[-9:])
middle_cube = ls_cube[9:-9]
middle_cube = ''.join(sum([middle_cube[i + j : i + j + 3] for i in range(0, 12, 3) for j in range(0, 25, 12)], []))
str_cube = U + middle_cube[18: 27] + middle_cube[9: 18] + D + middle_cube[0:9] + middle_cube[27:36]
print(str_cube)


