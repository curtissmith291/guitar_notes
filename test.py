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

# x, y = 0, 0
# print(x)
# print(y)



# x = "2"
# y = int(x)
# print (y)

# note_values = {'A': 1, 'A#/Bb': 2, 'B': 3, 'C': 4, 'C#/Db': 5, 'D': 6, 'D#/Eb': 7, 'E': 8, 'F': 9, 
#     'F#/Gb': 10, 'G': 11, 'G#/Ab': 12}

# value_notes = {1: 'A', 2: 'A#/Bb', 3: 'B', 4: 'C', 5: 'C#/Db', 6: 'D', 7: 'D#/Eb', 8: 'E', 9: 'F', 
#     10: 'F#/Gb', 11: 'G', 12: 'G#/Ab'}

# string_value = {'E': 8, 'A': 1, 'D': 6, 'G': 11, 'B': 3, 'e': 8}

# string_names = ['E', 'A', 'D', 'G', 'B', 'e']

# # Quick Testing
# string_low_e = "3"
# string_a = '2'
# string_d = '0'
# string_g = '0'
# string_b = '0'
# string_high_e = '2'

# # string_low_e = ""
# # string_a = ''
# # string_d = ''
# # string_g = ''
# # string_b = ''
# # string_high_e = ''


# def note_value(string, fret):
#     '''
#     This functon converts the fret number to a numerical note value
#     '''
#     note_num = string_value[string] + fret
#     # checks if number is >12, if so, subtracts 12 until it's 12 or lower
#     while True:
#         if note_num > 12:
#             note_num = note_num - 12
#             continue
#         else:
#             break
#     note = value_notes[note_num]
#     return note

# def note_converter2(list_to_check):
#     '''
#     This funtion iterates through input fret values and assigns note to numerical inputs and '--' to muted strings
#     '''
#     string_count = 0
#     inputs_fret_values = []
#     for item in list_to_check:
#         try:
#             x = int(item)
#             inputs_fret_values.append(note_value(string_names[string_count], x))
#             string_count += 1
#         except:
#             inputs_fret_values.append("--")
#             string_count += 1
#     print(inputs_fret_values)
#     if inputs_fret_values == ['--', '--', '--', '--', '--', '--']:
#         list_of_input_notes = "NA"
#         root = "NA"
#         print("need to enter at least one fret")
#         return inputs_fret_values, list_of_input_notes, root
#     else:
#         list_of_input_notes = [x for x in inputs_fret_values if x != "--"]
#         root = list_of_input_notes[0]
#         return inputs_fret_values, list_of_input_notes, root


# string_list = [string_low_e, string_a, string_d, string_g, string_b, string_high_e]
# print(string_list)

# # Checks input for empty (muted) strings, assigns them '--', assigns notes to input values
# input_notes, note_list, root_note = note_converter2(string_list)
# print(input_notes)
# print(note_list)
# print(root_note)

# def note_converter(list_to_check):
#     '''
#     This funtion iterates through input fret values and assigns note to numerical inputs and '--' to muted strings
#     '''
#     string_count = 0
#     inputs_fret_values = []
#     for item in list_to_check:
#         print(f'Item: {item}')
#         print(type(item))
#         print(f'StringCount: {string_count}')
#         print(f'input_frets_values: {inputs_fret_values}')
#         if type(item) is int:
#             inputs_fret_values.append(note_value(string_names[string_count], item))
#             string_count += 1
#         else:
#             inputs_fret_values.append("--")
#             string_count += 1
#     list_of_input_notes = [x for x in inputs_fret_values if x != "--"]
#     root = list_of_input_notes[0]
#     return inputs_fret_values, list_of_input_notes, root

# low = 0 
# high = 3
# # add check to make sure high is greater than low

# note_range = list(range(low, high + 1))
# print(note_range)

# for i in range(0, 7):
# root_note = "a"
# current_chord_structure = []
# for i in range(0, 1):
#     current_chord_structure.append("--")
# current_chord_structure.append(root_note)
# print(current_chord_structure)

import itertools

iterable = ["C", "E", "G"]
# x = list(itertools.combinations(iterable, 3))
# print(x)

# y = []
# for L in range(0, len(iterable)+1):
#     for subset in itertools.permutations(iterable, L):
#         if len(subset) == len(iterable):
#             y.append(subset)

# print(y)

# y = []
# for x in itertools.product(iterable, repeat=4):
#     y.append(list(x))

# print(y)

# y = [list(x) for x in itertools.product(iterable, repeat=4)]

# print(y)

# z = ['C']
# # print(type(z))
# new_list = []
# for i in y:
#     temp_list = z + i
#     new_list.append(temp_list)
# print(new_list)

# low = 0 
# high = 3
# fret_range = [low, high]
# print(fret_range)


# key = "A#/Bb"

# if len(key) == 5:
#     print(True)
#     key_html = key[0] + "&#9837" + key[2] + key[3] + "&#9839"

# print(key_html)

dictionary = {
'C': {'note': 'C', 'type': 'Major', 'structures': [['--', 3, 2, 0, 1, 0], ['--', 3, 2, 0, 1, 3]]}, 
'D': {'note': 'D', 'type': 'Minor', 'structures': [['--', '--', 0, 2, 3, 1]]}, 
'E': {'note': 'E', 'type': 'Minor', 'structures': [[0, 2, 2, 0, 0, 0], [0, 2, 2, 0, 0, 3], [0, 2, 2, 4, 0, 3], ['--', '--', 2, 0, 0, 0], ['--', '--', 2, 0, 0, 3], ['--', '--', 2, 4, 0, 3]]}, 
'F': {'note': 'F', 'type': 'Major', 'structures': [[1, 0, 3, 2, 1, 1], [1, 3, 3, 2, 1, 1], ['--', '--', 3, 2, 1, 1]]}, 
'G': {'note': 'G', 'type': 'Major', 'structures': [[3, 2, 0, 0, 0, 3], [3, 2, 0, 0, 3, 3], [3, 2, 0, 4, 0, 3], [3, 2, 0, 4, 3, 3]]}, 
'A': {'note': 'A', 'type': 'Minor', 'structures': [['--', 0, 2, 2, 1, 0], ['--', '--', '--', 2, 1, 0]]}, 
'B': {'note': 'B', 'type': 'Diminished', 'structures': [['--', 2, 0, 4, 0, 1], ['--', 2, 0, 4, 3, 1], ['--', 2, 3, 4, 3, 1], ['--', '--', '--', 4, 3, 1]]}}

list_of_dicts = []
# for x in dictionary.values():
#     list_of_dicts.append(x)

list_of_dicts = [x for x in dictionary.values()]

print(list_of_dicts)

