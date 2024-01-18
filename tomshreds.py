import random

drills_2s = [
    "Single String Ascending 1",
    "Single String Ascending 2",
    "Single String Decending 1",
    "Single String Decending 2",
    "REH Lick",
    "Trilogy Open String Lick",
    "7th Sign Lick",
    "Youtube Circular Lick",
    "Rising Force Ending Run",
    "Ascending 7s",
]

drills_asc = [
    "Simple Run",
    "Offset Run",
    "Eddy Run",
    "Volcano Style Run",
    "Rising Force Melodic Minor Run",
    "E Root Run",
]

drills_desc = [
    "Simple",
    "Offset",
    "E Root Simple",
    "E Root + Simple String Run",
    "E Root + Ascending Lead In",
    "E Root Far Beyond",
    "Viking Sequence",
    "Trilogy Octave Repeating",
    "Vertical Descending 4s (Expanded)",
    "Vertical Descending 4s (Locked Position)",
    "Direction Switch",
    "Rising Force Ending Run Complete",
]

drills_asc_desc = [
    "Simple",
    "Offset",
    "E Root",
]

drills_2sa = [
    "Picking",
    "B String Root Part 1",
    "B String Root Part 2",
    "E String Root",
    "Diminished Inversions",
]

drills_3sa = [
    "Picking (Part 1)",
    "Picking (Part 2)",
    "B String Root (Part 1)",
    "B String Root (Part 2)",
    "B String Root (Part 3)",
    "B String Root (Part 4)",
    "G String Root (Part 1)",
    "G String Root (Part 2)",
    "G String Root (Part 3)",
    "G String Root (Part 4)",
    "E String Root (Part 1)",
    "E String Root (Part 2)",
    "E String Root (Part 3)",
    "Disciples Shapes (Part 1)",
    "Disciples Shapes (Part 2)",
]

drills_456sa = [
    "5 String Arpeggio Ascending",
    "5 String Arpeggio Descending",
    "5 String Arpeggio Complete",
    "5 String Arpeggio Alternate Shape",
    "6 String Arpeggio",
    "4 String Arpeggio (Badinerie)",
]

drills_pt = [
    "Simple Pedal Expanded",
    "Simple Pedal Diminished Descending",
    "Simple Pedal Diminished Ascending",
    "Melodic Minor Pedal",
    "Fire Pedal Expanded",
]

drills_cp = [
    "Chord Progression 1",
    "Chord Progression 2",
    "Chord Progression 3",
    "Chord Progression 4",
    "Chord Progression 5",
]

drills_riff = [
    "Riff 1",
    "Riff 2",
    "Riff 3",
    "Riff 4",
    "Riff 5",
]

drills = {
    "2 String": drills_2s, 
    "4, 5, & 6 String Ascending": drills_asc,
    "4, 5, & 6 String Descending": drills_desc, 
    "Ascending Descending": drills_asc_desc, 
    "2 String Arpeggios": drills_2sa, 
    "3 String Arpeggios": drills_3sa, 
    "4, 5, & 6 String Arpeggios": drills_456sa, 
    "Pedal Tones": drills_pt, 
    "Chord Progressions": drills_cp, 
    "Riff Concepts": drills_riff
}

def get_practice_routine():
    # get one random drill from each category
    print("\nPractice Routine:\n-----------------")
    for key,val in drills.items():
        print(f"{key:27} : {random.choice(val)}")

if __name__ == "__main__":
    get_practice_routine()