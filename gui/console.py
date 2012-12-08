#!/usr/bin/env python
import helpers

def note_list(notes_dict):
    print("CONSOLE: " + ", ".join(notes_dict.keys()))

    return ("note_edit", notes_dict, notes_dict.keys()[0])

def note_edit(notes_dict, note_title):
    print("CONSOLE: " + "You wanted to edit \"" + note_title + "\"")

    return ("quit", notes_dict)
