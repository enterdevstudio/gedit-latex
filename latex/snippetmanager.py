# -*- coding: utf-8 -*-

#  Copyright (C) 2011 - Ignacio Casal Quinteiro
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 59 Temple Place, Suite 330,
#  Boston, MA 02111-1307, USA.

from gi.repository import Gtk, Gedit
from singleton import Singleton
import logging

_log = logging.getLogger("snippet manager")


class SnippetManager(Singleton):
    def __init_once__(self):
        pass

    def insert(self, editor, iter, text):
        view = editor.tab_decorator.tab.get_view()
        window = view.get_toplevel()
        bus = window.get_message_bus()

        if bus.is_registered('/plugins/snippets', 'parse-and-activate'):
            # FIXME: we miss the iter
            bus.send('/plugins/snippets', 'parse-and-activate',
                     trigger=text, view=view)

    def insert_at_cursor(self, editor, text):
        buf = editor.tab_decorator.tab.get_document()
        insert = buf.get_insert()
        iter = buf.get_iter_at_mark(insert)
        self.insert(editor, iter, text)

# vi:ex:ts=4:et: