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

input = "D"


# Function retrurns the notes that make up a major chord
# i.e., the first, third, and the fifth degrees
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
# i.e., the first, minor third, and the fifth degrees
def chord_notes_minor(note):
    value = note_values[note]
    third_num = value + 3
    if third_num > 12:
        third_num -= 12
    third = value_notes[third_num]
    fifth_num = value + 7
    if fifth_num > 12:
        fifth_num -= 12
    fifth = value_notes[fifth_num]
    return note, third, fifth

print(chord_notes_major(input))
print(chord_notes_minor(input))