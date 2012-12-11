#!/usr/bin/env python

def versionless_xrange(*largs, **kwargs):
    """Calls the generator-based range method regardless of Python version."""
    try:
        return xrange(*largs, **kwargs)
    except NameError:
        return range(*largs, **kwargs)

def versionless_raw_input(*largs, **kwargs):
    """Calls the raw input method regardless of Python version."""
    try:
        return raw_input(*largs, **kwargs)
    except NameError:
        return input(*largs, **kwargs)

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
        return strings 
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
