#!/usr/bin/env python
import helpers

def note_list(notes_dict):
    print("GTK: " + ", ".join(notes_dict.keys()))

    return ("note_edit", notes_dict, list(notes_dict.keys())[0])

def note_edit(notes_dict, note_title):
    print("GTK: " + "You wanted to edit \"" + note_title + "\"")

    return ("quit", notes_dict)
