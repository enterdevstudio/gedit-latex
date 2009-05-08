#!/bin/sh

# This file is part of the Gedit LaTeX Plugin
#
# Copyright (C) 2009 Michael Zeising
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public Licence as published by the Free Software
# Foundation; either version 2 of the Licence, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public Licence for more 
# details.
#
# You should have received a copy of the GNU General Public Licence along with
# this program; if not, write to the Free Software Foundation, Inc., 51 Franklin
# Street, Fifth Floor, Boston, MA  02110-1301, USA

#
# install the plugin
#

PLUGINS = ~/.gnome2/gedit/plugins
NAME = "GeditLaTeXPlugin"

#  ensure that the plugin directory exists
mkdir --parents $PLUGINS/$NAME
# copy all resources
cp --recursive * $PLUGINS/$NAME
# copy the plugin definition
cp $NAME.gedit-plugin $PLUGINS