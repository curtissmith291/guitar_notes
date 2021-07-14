notes_flats = ['A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab']
notes_sharps = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
all_notes = ['Ab', 'A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'A#', 'C#', 'D#', 'F#', 'G#']

string_names = {1: 'e', 2: 'B', 3: 'G', 4: 'G', 5: 'A', 6: 'E'}
string_values = {'E': 6, 'A': 5, 'D': 4, 'G': 3, 'B': 2, 'e': 1}

note_values_flats = {'Ab': 1, 'A': 2, 'Bb': 3, 'B': 4, 'C': 5, 'Db': 6, 'D': 7, 'Eb': 8, 'E': 9, 
    'F': 10, 'Gb': 11, 'G': 12}

value_notes_sharps = {1: 'A', 2: 'A#', 3: 'B', 4: 'C', 5: 'C#', 6: 'D', 7: 'D#', 8: 'E', 9: 'F', 
    10: 'F#', 11: 'G', 12: 'G#'}

value_notes_flats = {1: 'A', 2: 'Bb', 3: 'B', 4: 'C', 5: 'Db', 6: 'D', 7: 'Eb', 8: 'E', 9: 'F', 
    10: 'Gb', 11: 'G', 12: 'Ab'}

string_chrom_value = {'E': 8, 'A': 1, 'D': 6, 'G': 11, 'B': 3, 'e': 8}

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
        fret_input = int(input("Enter fret number "))
        break
        # if type(fret_input) != int:
        #     print("Please enter a valid fret number")
        #     continue
        # else:
        #     break
    except:
        print("Please enter a valid fret number")
        continue
  

def note_value(string, fret):
    note_num = string_chrom_value[string] + fret
    # checks if number is >12, if so, subtracts 12 until it's 12 or lower
    while True:
        if note_num > 12:
            note_num = note_num - 12
            continue
        else:
            break
    note = value_notes_sharps[note_num]
    return note

print(note_value(string_input, fret_input))