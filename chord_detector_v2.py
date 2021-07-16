
note_values = {'A': 1, 'A#/Bb': 2, 'B': 3, 'C': 4, 'C#/Db': 5, 'D': 6, 'D#/Eb': 7, 'E': 8, 'F': 9, 
    'F#/Gb': 10, 'G': 11, 'G#/Ab': 12}

value_notes = {1: 'A', 2: 'A#/Bb', 3: 'B', 4: 'C', 5: 'C#/Db', 6: 'D', 7: 'D#/Eb', 8: 'E', 9: 'F', 
    10: 'F#/Gb', 11: 'G', 12: 'G#/Ab'}

string_value = {'E': 8, 'A': 1, 'D': 6, 'G': 11, 'B': 3, 'e': 8}

string_names = ['E', 'A', 'D', 'G', 'B', 'e']

# Input is the fret number for each string, will be a list

# Test inputs
test_fret = ["M", "M", 1, 2, 1, 2]
fret_input_v1 = [3, 5, 5, 4, 3, 3]
fret_input_v2 = [3, 2, 0, 0, 0, 3]
fret_input_v3 = ["M", 3, 2, 0, 1, 0]
fret_input_v4 = ["M", "M", 0, 2, 3, 1]
fret_input_v5 = [0, 0, 0, 0, 0, 0]

# STEP 1
# Find notes for each string
# input = list of fret numbers
# output = list of notes
# Refactor using previous function

test_list = fret_input_v5

def note_value(string, fret):
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


# This block assign notes to each item in the input list
# Muted string ('M') are assigned '0'  
string_count = 0
input_notes = []
for item in test_list:
    if type(item) is int:
        input_notes.append(note_value(string_names[string_count], item))
        string_count += 1
    else:
        input_notes.append("--")
        string_count += 1
print(f'Input Notes: {input_notes}')

note_list = [x for x in input_notes if x != "--"]
print(f'Note List: {note_list}')

# STEP 2
# Find root note 

# Iterate through note_list and find first note
for item in note_list:
    if type(item) is str:
        root_note = item
        break
    else:
        continue

print(f'Root Note: {root_note}')

# STEP 3
# Function to return all the degrees based on root note

def degrees(note):
    value = note_values[note]

    root = note

    minor_second_num = value + 1
    if minor_second_num > 12:
        minor_second_num -= 12
    minor_second = value_notes[minor_second_num]

    major_second_num = value + 2
    if major_second_num > 12:
        major_second_num -= 12
    major_second = value_notes[major_second_num]

    minor_third_num = value + 3
    if minor_third_num > 12:
        minor_third_num -= 12
    minor_third = value_notes[minor_third_num]

    major_third_num = value + 4
    if major_third_num > 12:
        major_third_num -= 12
    major_third = value_notes[major_third_num]

    perfect_fourth_num = value + 5
    if perfect_fourth_num > 12:
        perfect_fourth_num -= 12
    perfect_fourth = value_notes[perfect_fourth_num]

    dim_fifth_num = value + 6
    if dim_fifth_num > 12:
        dim_fifth_num -= 12
    dim_fifth = value_notes[dim_fifth_num]

    perfect_fifth_num = value + 7
    if perfect_fifth_num > 12:
        perfect_fifth_num -= 12
    perfect_fifth = value_notes[perfect_fifth_num]

    aug_fifth_num = value + 8
    if aug_fifth_num > 12:
        aug_fifth_num -= 12
    aug_fifth = value_notes[aug_fifth_num]

    minor_sixth_num = value + 8
    if minor_sixth_num > 12:
        minor_sixth_num -= 12
    minor_sixth = value_notes[minor_sixth_num]

    major_sixth_num = value + 9
    if major_sixth_num > 12:
        major_sixth_num -= 12
    major_sixth = value_notes[major_sixth_num]

    minor_seventh_num = value + 10
    if minor_seventh_num > 12:
        minor_seventh_num -= 12
    minor_seventh = value_notes[minor_seventh_num]

    major_seventh_num = value + 11
    if major_seventh_num > 12:
        major_seventh_num -= 12
    major_seventh = value_notes[major_seventh_num]


    return root, minor_second, major_second, minor_third, major_third, perfect_fourth, dim_fifth, perfect_fifth, aug_fifth, minor_sixth, major_sixth, minor_seventh, major_seventh

# Creates a Dictionary of degrees
degree_strings = ["Root", "Minor Second", "Major Second", "Minor Third", "Major Third", "Perfect Fourth", 
    "Diminished Fifth", "Perfect Fifth", "Augmented Fifth", "Minor Sixth", "Major Sixth", "Minor Seventh", 
    "Major Seventh"]
degree_dictionary = dict(zip(degree_strings, degrees(root_note)))
print(degree_dictionary)

# loop to return chord structures based of dictionary
for item in degree_dictionary.items():
    major_chord = [degree_dictionary["Root"], degree_dictionary["Major Third"], degree_dictionary["Perfect Fifth"]]
    minor_chord = [degree_dictionary["Root"], degree_dictionary["Minor Third"], degree_dictionary["Perfect Fifth"]]
    augmented_chord = [degree_dictionary["Root"], degree_dictionary["Major Third"], degree_dictionary["Augmented Fifth"]]
    diminished_chord = [degree_dictionary["Root"], degree_dictionary["Minor Third"], degree_dictionary["Diminished Fifth"]]
    fifth_chord = [degree_dictionary["Root"], degree_dictionary["Perfect Fifth"]]
    suspended4_chord = [degree_dictionary["Root"], degree_dictionary["Perfect Fourth"], degree_dictionary["Perfect Fifth"]]
    suspended2_chord = [degree_dictionary["Root"], degree_dictionary["Major Second"], degree_dictionary["Perfect Fifth"]]
    major_sixth_chord = [degree_dictionary["Root"], degree_dictionary["Major Third"], degree_dictionary["Perfect Fifth"], degree_dictionary["Major Sixth"]]
    minor_sixth_chord = [degree_dictionary["Root"], degree_dictionary["Minor Third"], degree_dictionary["Perfect Fifth"], degree_dictionary["Major Sixth"]]
    dominant_seventh_chord = [degree_dictionary["Root"], degree_dictionary["Major Third"], degree_dictionary["Perfect Fifth"], degree_dictionary["Minor Seventh"]]
    major_seventh_chord = [degree_dictionary["Root"], degree_dictionary["Major Third"], degree_dictionary["Perfect Fifth"], degree_dictionary["Major Seventh"]]
    minor_seventh_chord = [degree_dictionary["Root"], degree_dictionary["Minor Third"], degree_dictionary["Perfect Fifth"], degree_dictionary["Minor Seventh"]]
    minor_major_seventh_chords = [degree_dictionary["Root"], degree_dictionary["Minor Third"], degree_dictionary["Perfect Fifth"], degree_dictionary["Major Seventh"]]
    augmented_seventh_chords = [degree_dictionary["Root"], degree_dictionary["Major Third"], degree_dictionary["Augmented Fifth"], degree_dictionary["Minor Seventh"]]
    diminished_seventh_chords = [degree_dictionary["Root"], degree_dictionary["Minor Third"], degree_dictionary["Diminished Fifth"], degree_dictionary["Major Sixth"]]
    half_diminished_seventh_chords = [degree_dictionary["Root"], degree_dictionary["Minor Third"], degree_dictionary["Diminished Fifth"], degree_dictionary["Minor Seventh"]]

# # STEP 4
# # Create a dictionary of the lists of chord notes
chord_list = [major_chord, minor_chord, augmented_chord, diminished_chord, fifth_chord, suspended4_chord, suspended2_chord, major_sixth_chord, minor_sixth_chord, 
    dominant_seventh_chord, major_seventh_chord, minor_seventh_chord, minor_major_seventh_chords, augmented_seventh_chords, diminished_seventh_chords, 
    half_diminished_seventh_chords]
chord_strings = "Major, Minor, Augmented, Diminished, 5/Power, sus4, sus2, 6, m6, 7, maj7, m7, m(maj)7, 7(#5) (minor-major seventh), dim7, m7(b5) (half-diminished seventh)"
chord_strings = chord_strings.split(", ")
chord_dictionary = dict(zip(chord_strings, chord_list))
print(chord_dictionary)

# # STEP 5
# # !!! Only matches chords where the root note = first degree
# # More complex chords can have a different root note

# 5.1 Iterate through chord dictionary
# counter = 0
# for item in chord_dictionary.items():
#     check = all([i in note_list for i in item[1]]) and all([i in item[1] for i in note_list])
#     if check == True:
#         print(f'{root_note} {item[0]} chord')
#     if check == False:
#         counter += 1
#         if counter == len(chord_dictionary):
#             print("Input notes do not match a chord")
#             break
#         else: 
#             continue
    

def chord_detector(root, list_of_notes, dictionary_of_chords):
    counter = 0
    for item in dictionary_of_chords.items():
        check = all([i in list_of_notes for i in item[1]]) and all([i in item[1] for i in list_of_notes])
        if check == True:
            # print(f'{root_note} {item[0]} chord')
            x = (f'{root} {item[0]} chord')
            return x
        if check == False:
            counter += 1
            if counter == len(dictionary_of_chords):
                # print("Input notes do not match a chord")
                y = ("Input notes do not match a chord")
                return y
            else: 
                continue

print(chord_detector(root_note, note_list, chord_dictionary))