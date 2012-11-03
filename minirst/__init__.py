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

    last_line = ""
    in_lines = r.split("\n")
    in_lines.append("")  # pad to avoid special-casing final line
    for line in in_lines:
        if (len(line) > 0) and (len(line) == len(last_line)) and (line.count("=") == len(last_line)):
            if len(blocks) > 0: # last block would have consumed the title, remove it
                blocks[-1] = [blocks[-1][0], "\n".join(blocks[-1][1].split("\n")[:-1])]
            blocks.append([last_line, ""])
        elif len(blocks) > 0:
            if blocks[-1][1] != "":
                blocks[-1][1] = blocks[-1][1] + "\n" + line
            else:
                blocks[-1][1] = line
        last_line = line

    return dict(blocks)
