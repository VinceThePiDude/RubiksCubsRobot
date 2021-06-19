import scrambler
import kociemba
import scrambleGenerator


moves_text = open('moves.txt', 'a+')

scramble = scrambleGenerator.gen_scramble()[:-4]
solve_string = scrambler.get_cube_string(scramble)
solve = kociemba.solve(solve_string)
degrees_of_motion = 360
turns = degrees_of_motion / 360 * 4

# Total turns
face_turns = {'U': 2, 'R': 2, 'F': 2, 'D': 2, 'L': 2, 'B': 2}
# Face position
face_pos = {'U': 2, 'R': 2, 'F': 2, 'D': 2, 'L': 2, 'B': 2}

for s in solve.split():
    # Checks if R2 etc.. goes over 4 moves
    if s[-1] == '2':
        if face_pos[s[0]] + 2 <= 4:
            face_pos[s[0]] += 2
        else:
            face_pos[s[0]] -= 2
        # Adds 2 moves onto face turns
        face_turns[s[0]] += 2

    if s[-1] != "'":
        # Checks if the position of the face is 4(unable to rotate further) and does 3 reverse turns to compensate
        if face_pos[s[0]] == 4:
            face_pos[s[0]] -= 3
            face_turns[s[0]] += 3

        else:
            face_pos[s[0]] += 1
            face_turns[s[0]] += 1

    if s[-1] == "'":
        # Checks if the position of the face is 0(unable to rotate further) and does 3 reverse turns to compensate
        if face_pos[s[0]] == 0:
            face_pos[s[0]] += 3
            face_turns[s[0]] += 3

        else:
            face_pos[s[0]] -= 1
            face_turns[s[0]] += 1

# Writes the total moves to a text document
moves_text.write(f"{sum(face_turns.values())}, ")
moves_text.seek(0)
total_moves = [int(x) for x in moves_text.readline().split(', ')[:-1]]
# Calculates the average moves
print(sum(total_moves) / len(total_moves))

print(scramble, solve_string, solve, sep = '\n')
print("U: {}\nR: {}\nF: {}\nD: {}\nL: {}\nB: {}".format(*face_turns.values()))
print("Total Moves:", sum(face_turns.values()))
# print("U: {}\nR: {}\nF: {}\nD: {}\nL: {}\nB: {}".format(*face_pos.values()))
