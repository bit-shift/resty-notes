#!/usr/bin/env python
from __future__ import print_function
import helpers, os, subprocess, tempfile

def note_list(notes_dict):
    query = ""
    while True:
        notes_list = []
        print()
        for note_title in helpers.find_fuzzy_matches(query, list(notes_dict.keys())):
            notes_list.append(note_title)
            print(str(len(notes_list)) + ". " + note_title)
        possible_id = helpers.versionless_raw_input("Enter a number to open that note, a ! to quit, or a string to display only those notes whose titles fuzzily match that string: ")
        try:
            return ("note_edit", notes_dict, notes_list[int(possible_id)-1])
        except ValueError:
            if possible_id == "!":
                return ("quit", notes_dict)
            else:
                query = possible_id

def note_edit(notes_dict, note_title):
    note_file = tempfile.NamedTemporaryFile(mode="w", prefix="note-", delete=False)
    note_file.write(notes_dict[note_title])
    note_file.close()

    editor_command = "vi"
    try:
        editor_command = os.environ["EDITOR"]
    except KeyError:
        pass
    subprocess.call([editor_command, note_file.name])

    notes_dict[note_title] = open(note_file.name, "rU").read().strip()
    os.remove(note_file.name)

    print("Updated!")

    return ("note_list", notes_dict)
