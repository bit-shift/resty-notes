#!/usr/bin/env python
import minirst
try:
    #from gi.repository import Gtk
    raise ImportError()
    import gui.gtk as gui
except:
    import gui.console as gui

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
            open("/home/bitshift/.notes2", "wU").write(minirst.from_dict(notes_dict))
