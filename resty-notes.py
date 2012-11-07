#!/usr/bin/env python
import minirst
try:
    from gi.repository import Gtk
    have_gui = True
except:
    have_gui = False

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

notes_dict = minirst.to_dict(open("/home/bitshift/.notes", "rU").read())
print(notes_dict)
print(find_fuzzy_matches("to a", notes_dict.keys()))
if have_gui:
    print("We have GUI support! ...shame I didn't code one yet.")
