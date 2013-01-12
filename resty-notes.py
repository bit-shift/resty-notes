#!/usr/bin/env python
import minirst, sys
try:
    from gi.repository import Gtk
    if len(sys.argv) == 1 or sys.argv[1] != "console":
        from gui import gtk as gui
    else:
        raise ImportError()
except ImportError:
    from gui import console as gui

if __name__ == "__main__":
    state = ("init", )
    while state[0] != "quit":
        notes_dict = minirst.to_dict(open("/home/bitshift/.notes", "rU").read())

        if state[0] == "init":
            state = ("note_list", notes_dict)
        if state[0] == "note_list":  # ("note_list", notes_dict)
            state = gui.note_list(state[1])
        elif state[0] == "note_edit":  # ("note_edit", notes_dict, note_title)
            state = gui.note_edit(*state[1:])

        if state[1] != notes_dict:
            notes_dict = state[1]
            open("/home/bitshift/.notes", "w").write(minirst.from_dict(notes_dict))
