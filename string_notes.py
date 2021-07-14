note_values = {'A': 1, 'A#/Bb': 2, 'B': 3, 'C': 4, 'C#/Db': 5, 'D': 6, 'D#/Eb': 7, 'E': 8, 'F': 9, 
    'F#/Gb': 10, 'G': 11, 'G#/Ab': 12}

value_notes = {1: 'A', 2: 'A#/Bb', 3: 'B', 4: 'C', 5: 'C#/Db', 6: 'D', 7: 'D#/Eb', 8: 'E', 9: 'F', 
    10: 'F#/Gb', 11: 'G', 12: 'G#/Ab'}

string_value = {'E': 8, 'A': 1, 'D': 6, 'G': 11, 'B': 3, 'e': 8}

string_names = ['E', 'A', 'D', 'G', 'B', 'e']
# Input is the fret number for each string, will be a list

# Need to allow for muted strings...
# Make value 'M'?
fret_input_v1 = [0, 0, 0, 0, 0, 0]
fret_input_v2 = [3, 2, 0, 0, 0, 3]
fret_input_v3 = ["M", 3, 2, 0, 1, 0]

# Step 1: find notes for each string
# input = list of fret numbers
# output = list of notes
# Refactor using previous function

test_list = fret_input_v3

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
print(note_list)



