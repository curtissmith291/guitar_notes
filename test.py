# input_notes = ['G', 'B', 'D', 'G', 'B', 'G']
# dict_chords =   {'Major': ['G', 'B', 'D'], 
#                 'Minor': ['G', 'A#/Bb', 'D'], 
#                 'Augmented': ['G', 'B', 'D#/Eb'], 
#                 'Diminished': ['G', 'A#/Bb', 'C#/Db'],
#                 '5': ['G', 'D'],
#                 '6': ['G', 'B', 'D', 'E'],
#                 'sus4': ['G', 'C', 'D'],
#                 'sus2': ['G', 'A', 'D'],
#                 'm6': ['G', 'A#/Bb', 'D', 'E'],
#                 '7': ['G', 'B', 'D', 'F'],
#                 'maj7': ['G', 'B', 'D', 'F#/Gb'],
#                 'm7': ['G', 'A#/Bb', 'D', 'F'],
#                 'm(maj)7': ['G', 'A#/Bb', 'D', 'F#/Gb'],
#                 '7(#5) (minor-major seventh)': ['G', 'B', 'D#/Eb', 'F'],
#                 'dim7': ['G', 'A#/Bb', 'C#/Db', 'E'],
#                 'm7(b5) (half-diminished seventh)': ['G', 'A#/Bb', 'C#/Db', 'F']
#                 }

# for item in dict_chords.items():
#     check = all([i in input_notes for i in item[1]]) and all([i in item[1] for i in input_notes])
#     if check == True:
#         print(f'{input_notes[0]} {item[0]} chord')
#     if check == False:
#         print(f'not {input_notes[0]} {item[0]} chord')


# input_notes2 = ['G', 'B', 'D', 'G', 'B', 'G']
# five = ['G', 'D']
# check = all(item in input_notes2 for item in five)
# print(check)

# input_notes2 = ['G', 'B', 'D', 'G', 'B', 'G']
# six = ['G', 'B', 'D', 'E']
# check = all(item in input_notes2 for item in six)
# print(check)

# input_notes2 = ['G', 'B', 'D', 'G', 'B', 'G']
# five = ['G', 'D']
# check = all(item in five for item in input_notes2)
# print(check)

# input_notes2 = ['G', 'B', 'D', 'G', 'B', 'G']
# six = ['G', 'B', 'D', 'E']
# check = all(item in six for item in input_notes2)
# print(check)

# bleh = [item in six for item in input_notes2]
# print(bleh)



# checkBoth = all([item in six for item in input_notes2]) and all([item in input_notes2 for item in six])
# print(checkBoth)

# bleh = [item in five for item in input_notes2]
# print(bleh)

# test = ['B']
# five = ['G', 'D']
# check = all(item in test for item in five)
# print(check)

# test = ["B"] in ['G', 'D']
# print(test)


# set_input = set(input_notes)
# print(set_input)
# set_chord = set(dict_chords['Major'])
# print(set_chord)

# x = set_input == set(dict_chords['Major'])
# print(x)

x, y = 0, 0
print(x)
print(y)