#!/usr/bin/env python
import minirst
import testingui as gui
try:
    #from gi.repository import Gtk
    raise ImportError()
    import gui.gtk as gui
except:
    import gui.console as gui

def fancy_str(obj, dict_indent_width=4):
    """fancy_str(obj, dict_indent_width=4) -> string

Turns an object, obj, into a pretty-printed string, with each level of
nested dicts being indented dict_indent_width characters further in."""
    if isinstance(obj, dict):
        if len(obj.keys()) == 0:
            out_str = "{}"
        else:
            out_str = "{\n"
            for key in obj:
                if out_str != "{\n":
                    out_str = out_str[:-1] + ",\n"
                out_str += "\n".join([(" "*dict_indent_width + line) for line in "{0}: {1}".format(fancy_str(key, dict_indent_width), fancy_str(obj[key], dict_indent_width)).split("\n")]) + "\n"
            out_str += "}"
    elif isinstance(obj, str):
        out_str = "'{0}'".format(obj)
    elif isinstance(obj, list):
        out_str = "[{0}]".format(", ".join([fancy_str(elem, dict_indent_width) for elem in obj]))
    else:
        out_str = "{0}".format(obj)
    return out_str

def find_fuzzy_matches(fragment, strings, case_sensitive=False):
    """find_fuzzy_matches(fragment, [string], case_sensitive=False) -> [string]

Given a list of strings, return a list of those where the non-empty
fragment has all its characters appear in order. If case_sensitive is
False (default), uppercase characters will match lowercase versions,
and vice versa."""
    if len(fragment) == 0:
        return []
    matches = []
    for string in strings:
        fragment_index = 0
        for char in string:
            if (case_sensitive and char == fragment[fragment_index]) or ((not case_sensitive) and char.lower() == fragment[fragment_index].lower()):
                fragment_index += 1
            if fragment_index == len(fragment): # all chars existed in order, this is a fuzzy match
                matches.append(string)
                break
    return matches

def main():
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

main()
