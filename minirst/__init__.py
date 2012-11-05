#!/usr/bin/env python

def from_dict(d):
    """from_dict(d) -> string

Convert a dict, d, of title:block into a minimal reST-like format."""
    out_blocks = []
    for title in d:
        out_blocks.append("\n".join((title, "="*len(title), d[title])))
    return "\n\n".join([block.strip() for block in out_blocks])

def to_dict(r):
    """to_dict(r) -> dict

Parse a minimal reST-like document, r, into a dict of title:block."""
    blocks = []
    in_lines = r.split("\n")
    for n in xrange(len(in_lines)):
        if n < (len(in_lines) - 1) and len(in_lines[n]) == len(in_lines[n+1]) and len(in_lines[n]) == in_lines[n+1].count("="):
            blocks.append([in_lines[n], ""])
        elif n < len(in_lines) and len(in_lines[n-1]) == len(in_lines[n]) and len(in_lines[n-1]) == in_lines[n].count("="):
            continue
        elif len(blocks) > 0:
            blocks[-1][1] += in_lines[n] + "\n"

    return dict(blocks)
