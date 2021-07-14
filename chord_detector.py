note_values = {'A': 1, 'A#/Bb': 2, 'B': 3, 'C': 4, 'C#/Db': 5, 'D': 6, 'D#/Eb': 7, 'E': 8, 'F': 9, 
    'F#/Gb': 10, 'G': 11, 'G#/Ab': 12}

value_notes = {1: 'A', 2: 'A#/Bb', 3: 'B', 4: 'C', 5: 'C#/Db', 6: 'D', 7: 'D#/Eb', 8: 'E', 9: 'F', 
    10: 'F#/Gb', 11: 'G', 12: 'G#/Ab'}

string_value = {'E': 8, 'A': 1, 'D': 6, 'G': 11, 'B': 3, 'e': 8}

string_names = ['E', 'A', 'D', 'G', 'B', 'e']

# Input is the fret number for each string, will be a list

# Need to allow for muted strings...
# Make value 'M'?
fret_input_v1 = [3, 5, 5, 4, 3, 3]
fret_input_v2 = [3, 2, 0, 0, 0, 3]
fret_input_v3 = ["M", 3, 2, 0, 1, 0]
fret_input_v4 = ["M", "M", 0, 2, 3, 1]
fret_input_v5 = [0, 2, 2, "M", "M", "M"]

# STEP 1
# Find notes for each string
# input = list of fret numbers
# output = list of notes
# Refactor using previous function

test_list = fret_input_v2

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
note_list = []
for item in test_list:
    if type(item) is int:
        note_list.append(note_value(string_names[string_count], item))
        string_count += 1
    else:
        note_list.append(0)
        string_count += 1
print(f'Input Notes: {note_list}')

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
# Return list of notes for major/minor chords

# Function retrurns the notes that make up a major chord
# i.e., the first/root, third, and the fifth degrees
def chord_notes_major(note):
    value = note_values[note]
    third_num = value + 4
    if third_num > 12:
        third_num -= 12
    third = value_notes[third_num]
    fifth_num = value + 7
    if fifth_num > 12:
        fifth_num -= 12
    fifth = value_notes[fifth_num]
    return note, third, fifth

# Function retrurns the notes that make up a minor chord
# i.e., the first/root, minor third, and the fifth degrees
def chord_notes_minor(note):
    value = note_values[note]
    min_third_num = value + 3
    if min_third_num > 12:
        min_third_num -= 12
    third = value_notes[min_third_num]
    fifth_num = value + 7
    if fifth_num > 12:
        fifth_num -= 12
    fifth = value_notes[fifth_num]
    return note, third, fifth

# Function retrurns the notes that make up a augmented chord
# i.e., the first/root, third, and the augmented fifth degrees
def chord_notes_aug(note):
    value = note_values[note]
    third_num = value + 4
    if third_num > 12:
        third_num -= 12
    third = value_notes[third_num]
    aug_fifth_num = value + 8
    if aug_fifth_num > 12:
        aug_fifth_num -= 12
    fifth = value_notes[aug_fifth_num]
    return note, third, fifth

# Function retrurns the notes that make up a diminished chord
# i.e., the first/root, minor third, and the diminished fifth degrees
def chord_notes_dim(note):
    value = note_values[note]
    min_third_num = value + 3
    if min_third_num > 12:
        min_third_num -= 12
    third = value_notes[min_third_num]
    dim_fifth_num = value + 6
    if dim_fifth_num > 12:
        dim_fifth_num -= 12
    fifth = value_notes[dim_fifth_num]
    return note, third, fifth

# Function retrurns the notes that make up a minor chord
# i.e., the first/root and the fifth degrees
def chord_notes_fifth(note):
    value = note_values[note]
    fifth_num = value + 7
    if fifth_num > 12:
        fifth_num -= 12
    fifth = value_notes[fifth_num]
    return note, fifth

# List of tuples containing all list of chord notes
all_chord_notes = []

major_notes = chord_notes_major(root_note)
all_chord_notes.append(major_notes)


minor_notes = chord_notes_minor(root_note)
all_chord_notes.append(minor_notes)


augmented_notes = chord_notes_aug(root_note)
all_chord_notes.append(augmented_notes)


diminished_notes = chord_notes_dim(root_note)
all_chord_notes.append(diminished_notes)

fifth_notes = chord_notes_fifth(root_note)
all_chord_notes.append(fifth_notes)

# STEP 4
# Create a dictionary of the tuples of chord notes
chord_strings = ["Major", "Minor", "Augmented", "Diminished", "5/Power"]
chord_notes_dict = dict(zip(chord_strings, all_chord_notes))
print(chord_notes_dict)


# STEP 5
# !!! Only matches chords where the root note = first degree
# More complex chords can have a different root note
# Match input notes to chord lists returned in step 3

# 5.1 Iterate through chord dictionary
counter = 0
for item in chord_notes_dict.items():
    check = all(i in note_list for i in item[1])
    if check == True:
        print(f'{root_note} {item[0]} chord')
    if check == False:
        counter += 1
        if counter == len(chord_notes_dict):
            print("Input notes do not match a chord")
            break
        else: 
            continue
    