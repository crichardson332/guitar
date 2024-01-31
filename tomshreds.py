import random

ss2s = {
    "Single String On Beat": [
        "Single String Ascending 1 (Chunk Only)",
        "Single String Ascending 1 (Expanded)",
        "Single String Descending 1 (Chunk Only)",
        "Single String Descending 1 (Expanded)",
        "Etude 1",
    ],
    "Single String Off Beat": [
        "Single String Ascending 2 (Chunk Only)",
        "Single String Ascending 2 (Expanded)",
        "Single String Descending 2 (Chunk Only)",
        "Single String Descending 2 (Expanded)",
        "Etude 2",
    ],
    "REH Lick": [
        "REH Lick (Chunk Only)",
        "REH Lick (Expanded)",
        "REH Lick w/ Pulloff (Chunk Only)",
        "REH Lick w/ Pulloff (Expanded)",
        "Etude 2",
    ],
    "Open String Licks": [
        "Trilogy Open String Lick",
        "Spellbound Open String Lick",
        "Etude 5",
        "Etude 6",
    ],
    "Economy Picking Two String Licks": [
        "7th Sign Lick (Chunk Only)",
        "7th Sign Lick (Expanded)",
        "Youtube Circular Lick",
        "Etude 3",
        "Etude 4",
    ],
    "5 and 7 Note Licks": [
        "Rising Force Ending Run (Chunk Only)",
        "Rising Force Ending Run (Expanded)",
        "Ascending 7s (Chunk Only)",
        "Ascending 7s (Expanded)",
        "Etude 7",
        "Etude 8",
    ],
}

asc_desc_456 = {
    "Three Notes per String": [
        "Ascending: Simple Run (Chunk Only)",
        "Ascending: Simple Run (Expanded)",
        "Ascending: Rising Force Melodic Minor Run",
        "Descending: Simple",
        "Ascending Descending: Simple",
        "Ascending: Etude 1",
        "Ascending: Etude 4",
        "Descending: Etude 1",
        "Descending: Etude 7",
        "Ascending Descending: Etude 1",
    ],
    "Offset": [
        "Ascending: Offset Run",
        "Descending: Offset",
        "Descending: Direction Switch",
        "Descending: Viking Sequence",
        "Ascending Descending: Offset",
        "Ascending: Etude 2",
        "Descending: Etude 2",
        "Descending: Etude 3",
        "Descending: Etude 4",
        "Ascending Descending: Etude 2",
    ],
    "Eddy": [
        "Ascending: Eddy Run",
        "Ascending: Volcano Style Run",
        "Descending: Trilogy Octave Repeating",
        "Descending: Vertical Descending 4s",
        "Descending: Vertical Descending 4s (Expanded)",
        "Descending: Vertical Descending 4s (Locked Position)",
        "Descending: Rising Force Ending Run Complete",
        "Ascending: Etude 3"
        "Descending: Etude 5",
        "Descending: Etude 6",
        "Descending: Etude 7",
        "Ascending Descending: Etude 3",
    ],
    "E Root": [
        "Ascending: E Root Run",
        "Descending: E Root Simple",
        "Descending: E Root + Simple String Run",
        "Descending: E Root + Ascending Lead In",
        "Descending: E Root Far Beyond",
        "Ascending Descending: E Root",
    ],
}

arpeggios = {
    "B Root": [
        "2 String: B String Root Part 1",
        "2 String: B String Root Part 2",
        "2 String: Diminished Inversions",
        "2 String: Etude 1",
        "3 String: B String Root (Part 1)",
        "3 String: B String Root (Part 2)",
        "3 String: B String Root (Part 3)",
        "3 String: B String Root (Part 4)",
        "3 String: Etude 2",
        "4, 5, 6: 5 String Arpeggio Alternate Shape",
    ],
    "E Root": [
        "2 String: E String Root",
        "2 String: Etude 2",
        "2 String: Etude 3",
        "2 String: Etude 4",
        "3 String: E String Root (Part 1)",
        "3 String: E String Root (Part 2)",
        "3 String: E String Root (Part 3)",
        "Disciples Shapes (Part 1)",
        "Disciples Shapes (Part 2)",
        "3 String: Etude 3",
        "3 String: Etude 4",
        "3 String: Etude 5",
        "4, 5, 6: 4 String Arpeggio (Badinerie)",
        "4, 5, 6: Etude 2",
    ],
    "G Root": [
        "3 String: G String Root (Part 1)",
        "3 String: G String Root (Part 2)",
        "3 String: G String Root (Part 3)",
        "3 String: G String Root (Part 4)",
        "3 String: Etude 1",
        "3 String: Etude 6",
        "4, 5, 6: 5 String Arpeggio Ascending",
        "4, 5, 6: 5 String Arpeggio Descending",
        "4, 5, 6: 5 String Arpeggio Complete",
        "4, 5, 6: 6 String Arpeggio",
        "4, 5, 6: Etude 1",
    ],

}


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

drills_2s_etudes = [
    "Etude 1",
    "Etude 2",
    "Etude 3",
    "Etude 4",
    "Etude 5",
    "Etude 6",
    "Etude 7",
    "Etude 8",
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

drills_asc_desc_etudes = [
    "Etude 1",
    "Etude 2",
    "Etude 3",
]

drills_bends = [
    "Bends on the E String",
    "Bends on the B String",
    "Bends on the G String",
    "Vibrato",
    "Trills",
    "Arpeggio Trills",
    "Slide Shrieks",
    "Etude 1",
    "Etude 2",
]

drills_bends_etudes = [
    "Etude 1",
    "Etude 2",
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
    "2 String Etudes": drills_2s_etudes, 
    "4, 5, & 6 String Ascending": drills_asc,
    "4, 5, & 6 String Descending": drills_desc, 
    "Ascending Descending": drills_asc_desc, 
    "Ascending Descending Etudes": drills_asc_desc_etudes, 
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