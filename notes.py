notes_flats = ['A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab']
notes_sharps = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']

string_names = {1: 'e', 2: 'B', 3: 'G', 4: 'G', 5: 'A', 6: 'E'}
string_values = {'E': 6, 'A': 5, 'D': 4, 'G': 3, 'B': 2, 'e': 1}

# These threee are inconsistant, FIX!!, All need to start at "A"
note_values_flats = {'A': 1, 'Bb': 2, 'B': 3, 'C': 4, 'Db': 5, 'D': 6, 'Eb': 7, 'E': 8, 'F': 9, 
    'Gb': 10, 'G': 11, 'Ab': 12}

note_values_sharps = {'A': 1, 'A#': 2, 'B': 3, 'C': 4, 'C#': 5, 'D': 6, 'D#': 7, 'E': 8, 'F': 9, 
    'F#': 10, 'G': 11, 'G#': 12}

note_values = {'A': 1, 'A#/Bb': 2, 'B': 3, 'C': 4, 'C#/Db': 5, 'D': 6, 'D#/Eb': 7, 'E': 8, 'F': 9, 
    'F#/Gb': 10, 'G': 11, 'G#/Ab': 12}

value_notes_sharps = {1: 'A', 2: 'A#', 3: 'B', 4: 'C', 5: 'C#', 6: 'D', 7: 'D#', 8: 'E', 9: 'F', 
    10: 'F#', 11: 'G', 12: 'G#'}

value_notes = {1: 'A', 2: 'A#/Bb', 3: 'B', 4: 'C', 5: 'C#/Db', 6: 'D', 7: 'D#/Eb', 8: 'E', 9: 'F', 
    10: 'F#/Gb', 11: 'G', 12: 'G#/Ab'}

value_notes_flats = {1: 'A', 2: 'Bb', 3: 'B', 4: 'C', 5: 'Db', 6: 'D', 7: 'Eb', 8: 'E', 9: 'F', 
    10: 'Gb', 11: 'G', 12: 'Ab'}

string_value = {'E': 8, 'A': 1, 'D': 6, 'G': 11, 'B': 3, 'e': 8}

string_names = ['E', 'A', 'D', 'G', 'B', 'e']


# User inputs string name, checks if valid input
while True:
    string_input = input("Enter String Name (E, A, D, G, B, e) ")
    if string_input not in string_names:
        print("Please enter a string name")
        continue
    else:
        break

# User inputs fret number
# Any fret number is technically valid as the pattern is infinately repeating
while True:
    try:
        # If input if not an integer, an error occurs and the "except" path is taken
        fret_input = int(input("Enter fret number "))
        break
    except:
        print("Please enter a valid fret number")
        continue
  

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

print(note_value(string_input, fret_input))