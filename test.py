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

note_values = {'A': 1, 'A#/Bb': 2, 'B': 3, 'C': 4, 'C#/Db': 5, 'D': 6, 'D#/Eb': 7, 'E': 8, 'F': 9, 
    'F#/Gb': 10, 'G': 11, 'G#/Ab': 12}

value_notes = {1: 'A', 2: 'A#/Bb', 3: 'B', 4: 'C', 5: 'C#/Db', 6: 'D', 7: 'D#/Eb', 8: 'E', 9: 'F', 
    10: 'F#/Gb', 11: 'G', 12: 'G#/Ab'}

string_value = {'E': 8, 'A': 1, 'D': 6, 'G': 11, 'B': 3, 'e': 8}

string_names = ['E', 'A', 'D', 'G', 'B', 'e']

# Quick Testing
string_low_e = "3"
string_a = '2'
string_d = '0'
string_g = '0'
string_b = '0'
string_high_e = '2'

# string_low_e = ""
# string_a = ''
# string_d = ''
# string_g = ''
# string_b = ''
# string_high_e = ''


def note_value(string, fret):
    '''
    This functon converts the fret number to a numerical note value
    '''
    note_num = string_value[string] + fret
    # checks if number is >12, if so, subtracts 12 until it's 12 or lower
    while True:
        if note_num > 12:
            note_num = note_num - 12
            continue
        else:
            break
    note = value_notes[note_num]
    return note

def note_converter2(list_to_check):
    '''
    This funtion iterates through input fret values and assigns note to numerical inputs and '--' to muted strings
    '''
    string_count = 0
    inputs_fret_values = []
    for item in list_to_check:
        try:
            x = int(item)
            inputs_fret_values.append(note_value(string_names[string_count], x))
            string_count += 1
        except:
            inputs_fret_values.append("--")
            string_count += 1
    print(inputs_fret_values)
    if inputs_fret_values == ['--', '--', '--', '--', '--', '--']:
        list_of_input_notes = "NA"
        root = "NA"
        print("need to enter at least one fret")
        return inputs_fret_values, list_of_input_notes, root
    else:
        list_of_input_notes = [x for x in inputs_fret_values if x != "--"]
        root = list_of_input_notes[0]
        return inputs_fret_values, list_of_input_notes, root


string_list = [string_low_e, string_a, string_d, string_g, string_b, string_high_e]
print(string_list)

# Checks input for empty (muted) strings, assigns them '--', assigns notes to input values
input_notes, note_list, root_note = note_converter2(string_list)
print(input_notes)
print(note_list)
print(root_note)



def note_converter(list_to_check):
    '''
    This funtion iterates through input fret values and assigns note to numerical inputs and '--' to muted strings
    '''
    string_count = 0
    inputs_fret_values = []
    for item in list_to_check:
        print(f'Item: {item}')
        print(type(item))
        print(f'StringCount: {string_count}')
        print(f'input_frets_values: {inputs_fret_values}')
        if type(item) is int:
            inputs_fret_values.append(note_value(string_names[string_count], item))
            string_count += 1
        else:
            inputs_fret_values.append("--")
            string_count += 1
    list_of_input_notes = [x for x in inputs_fret_values if x != "--"]
    root = list_of_input_notes[0]
    return inputs_fret_values, list_of_input_notes, root