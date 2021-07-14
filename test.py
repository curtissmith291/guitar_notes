input_notes = ['G', 'B', 'D', 'G', 'B', 'G']
dict_chords =   {'Major': ('G', 'B', 'D'), 
                'Minor': ('G', 'A#/Bb', 'D'), 
                'Augmented': ('G', 'B', 'D#/Eb'), 
                'Diminished': ('G', 'A#/Bb', 'C#/Db')}

# check = all(item in input_notes for item in dict_chords["Major"])
# print(check)

# for item in dict_chords.items():
#     check2 = all(i in input_notes for i in item[1])
#     if check2 == True:
#         print(f'{input_notes[0]} {item[0]} chord')

print(len(dict_chords))