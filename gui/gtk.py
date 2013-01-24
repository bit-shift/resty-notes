#!/usr/bin/env python
from gi.repository import Gtk
import helpers

def note_list(notes_dict):
    note_list.result = ("quit", notes_dict)

    note_list_window = Gtk.Window(title="Resty Notes")
    note_list_window.connect("delete-event", Gtk.main_quit)

    note_list_layout = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
    note_list_window.add(note_list_layout)

    note_search_area = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
    note_search_entry = Gtk.Entry()
    note_search_area.pack_start(note_search_entry, expand=True, fill=True, padding=3)
    note_list_layout.pack_start(note_search_area, expand=False, fill=False, padding=3)

    note_iters = {}
    note_list_store = Gtk.ListStore(str)
    for note_title in notes_dict:
        note_iters[note_title] = note_list_store.append([note_title])
    note_list_filter = note_list_store.filter_new()
    note_list_view = Gtk.TreeView(note_list_filter)
    note_list_view_column = Gtk.TreeViewColumn("Note titles", Gtk.CellRendererText(), text=0)
    note_list_view_column.set_sort_column_id(0)
    note_list_view.append_column(note_list_view_column)
    note_list_view_scroll = Gtk.ScrolledWindow()
    note_list_view_scroll.add(note_list_view)
    note_list_layout.pack_start(note_list_view_scroll, expand=True, fill=True, padding=3)

    def filter_list(model, treeiter, data):
        return len(helpers.find_fuzzy_matches(note_search_entry.get_text(), [model.get_value(treeiter, 0)])) > 0

    note_list_filter.set_visible_func(filter_list)

    note_search_entry.connect("changed", (lambda w: note_list_filter.refilter()))

    def select_note_by_entry(entry):
        matches = helpers.find_fuzzy_matches(entry.get_text(), notes_dict)
        if len(matches) == 1:
            note_list.result = ("note_edit", notes_dict, matches[0])
            Gtk.main_quit()
        elif len(matches) == 0:
            note_list.result = ("note_edit", notes_dict, entry.get_text())
            Gtk.main_quit()

    def select_note_by_list(treeview, row_path, view_column):
        note_list.result = ("note_edit", notes_dict, note_list_filter.get_value(note_list_filter.get_iter_from_string(str(row_path)), 0))
        Gtk.main_quit()

    note_search_entry.connect("activate", select_note_by_entry)
    note_list_view.connect("row-activated", select_note_by_list)

    note_list_window.show_all()
    Gtk.main()

    return note_list.result

def note_edit(notes_dict, note_title):
    # TODO: Actual GUI function for this handler.
    print("GTK: " + "You wanted to edit \"" + note_title + "\"")

    return ("quit", notes_dict)
