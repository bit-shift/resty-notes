#!/usr/bin/env python
import minirst, sys
gui_modules = {}
try:
    from gi.repository import Gtk
    from gui import gtk as gui_gtk
    gui_modules["gtk"] = gui_gtk
except ImportError:
    from gui import console as gui_console
    gui_modules["console"] = gui_console

if __name__ == "__main__":
    if "gtk" in gui_modules: # TODO: Don't hardcode this, use a parameter which defaults to gtk only if we have it
        active_gui = "gtk"
    else:
        active_gui = "console"

    state = ("init", )
    while state[0] != "quit":
        notes_dict = minirst.to_dict(open("/home/bitshift/.notes", "rU").read())

        if state[0] == "init":
            state = ("note_list", notes_dict)

        if hasattr(gui_modules[active_gui], state[0]):
            handler_func = getattr(gui_modules[active_gui], state[0])
            state = handler_func(*state[1:])
        else:
            sys.stderr.write("FATAL: Unhandled state {0}".format(state))
            sys.exit(1)

        if state[1] != notes_dict:
            notes_dict = state[1]
            open("/home/bitshift/.notes", "w").write(minirst.from_dict(notes_dict))
