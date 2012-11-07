===========
ReSTy Notes
===========

Summary
-------
Note-handling tool, currently still in development.

Fuller README will be forthcoming when more of the tool is done.

Plan
----
Loose plan is as follows:
  - Stores to/reads from a minimal reST-like format (**DONE**)
  - Finds titles by fuzzy-matching (**DONE**) or creates a new entry
    if no match (**NOT DONE**)
  - Save current note block as it's typed, for resilience against system
    crash or forgetting to save. (**NOT DONE**)
  - Has a minimal GUI for above features, so as to be able to be bound
    to a hotkey for quick access (**NOT DONE**)

Dependencies
------------
Python GObject Introspection
  **OPTIONAL**, needed for GUI. Can be obtained via:
  
  On Ubuntu or derivatives, run as root or via ``sudo``::

    apt-get install python-gi

  On Arch Linux, run as root, or via sudo (or adapt the command to use
  your favourite pacman wrapper)::

    pacman -Sy python-gobject

  On other distros, you're on your own for now, because I don't use
  them enough to have any idea what the package is called. If you work
  it out, though, just drop me a line at <bitshift@bigmacintosh.net>
  and I'll add it here for others' reference.
