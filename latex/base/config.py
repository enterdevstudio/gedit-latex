# -*- coding: utf-8 -*-

# This file is part of the Gedit LaTeX Plugin
#
# Copyright (C) 2010 Michael Zeising
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

"""
base.config
"""

# actions

from ..latex.actions import LaTeXMenuAction, LaTeXNewAction, LaTeXChooseMasterAction, \
        LaTeXItemizeAction, LaTeXEnumerateAction, LaTeXFontFamilyAction, LaTeXFontFamilyMenuAction, LaTeXBoldAction, \
        LaTeXItalicAction, LaTeXEmphasizeAction, LaTeXDescriptionAction, LaTeXStructureMenuAction, LaTeXPartAction, LaTeXChapterAction, \
        LaTeXSectionAction, LaTeXSubsectionAction, LaTeXParagraphAction, LaTeXSubparagraphAction, LaTeXStructureActionDefault, \
        LaTeXGraphicsAction, LaTeXUseBibliographyAction, LaTeXTableAction, LaTeXListingAction, LaTeXJustifyLeftAction, \
        LaTeXJustifyMenuAction, LaTeXJustifyActionDefault, \
        LaTeXJustifyCenterAction, LaTeXJustifyRightAction, LaTeXMathMenuAction, LaTeXMathActionDefault, LaTeXMathAction, LaTeXDisplayMathAction, \
        LaTeXEquationAction, LaTeXUnEqnArrayAction, LaTeXEqnArrayAction, LaTeXUnderlineAction, LaTeXSmallCapitalsAction, \
        LaTeXRomanAction, LaTeXSansSerifAction, LaTeXTypewriterAction, LaTeXCloseEnvironmentAction, LaTeXBlackboardBoldAction, \
        LaTeXCaligraphyAction, LaTeXFrakturAction, LaTeXBuildImageAction, LaTeXSaveAsTemplateAction, \
        LaTeXBuildAction, LaTeXBuildMenuAction

from ..bibtex.actions import BibTeXMenuAction, BibTeXNewEntryAction

ACTIONS = [LaTeXMenuAction, LaTeXNewAction, LaTeXChooseMasterAction,
        LaTeXItemizeAction, LaTeXEnumerateAction, LaTeXFontFamilyAction, LaTeXFontFamilyMenuAction, LaTeXBoldAction,
        LaTeXItalicAction, LaTeXEmphasizeAction, LaTeXDescriptionAction, LaTeXStructureMenuAction, LaTeXPartAction, LaTeXChapterAction,
        LaTeXSectionAction, LaTeXSubsectionAction, LaTeXParagraphAction, LaTeXSubparagraphAction, LaTeXStructureActionDefault,
        LaTeXGraphicsAction, LaTeXUseBibliographyAction, LaTeXTableAction, LaTeXListingAction, LaTeXJustifyLeftAction,
        LaTeXJustifyMenuAction, LaTeXJustifyActionDefault,
        LaTeXJustifyCenterAction, LaTeXJustifyRightAction, LaTeXMathMenuAction, LaTeXMathActionDefault, LaTeXMathAction, LaTeXDisplayMathAction,
        LaTeXEquationAction, LaTeXUnEqnArrayAction, LaTeXEqnArrayAction, LaTeXUnderlineAction, LaTeXSmallCapitalsAction,
        LaTeXRomanAction, LaTeXSansSerifAction, LaTeXTypewriterAction, LaTeXCloseEnvironmentAction, LaTeXBlackboardBoldAction,
        LaTeXCaligraphyAction, LaTeXFrakturAction, LaTeXBuildImageAction, LaTeXSaveAsTemplateAction,
        LaTeXBuildAction, LaTeXBuildMenuAction,
        BibTeXMenuAction, BibTeXNewEntryAction]

# views

from ..views import IssueView
from ..latex.views import LaTeXSymbolMapView, LaTeXOutlineView
from ..bibtex.views import BibTeXOutlineView


#WINDOW_SCOPE_VIEWS = {".tex": {"LaTeXSymbolMapView": LaTeXSymbolMapView}}
#
#EDITOR_SCOPE_VIEWS = {".tex": {"IssueView": IssueView,
#                                 "LaTeXOutlineView": LaTeXOutlineView},
#
#                       ".bib": {"IssueView": IssueView,
#                                 "BibTeXOutlineView": BibTeXOutlineView}}

from ..preferences import Preferences
LATEX_EXTENSIONS = Preferences().get("latex-extensions").split(",")
BIBTEX_EXTENSIONS = [".bib"]

WINDOW_SCOPE_VIEWS = {}
EDITOR_SCOPE_VIEWS = {}

for e in LATEX_EXTENSIONS:
    WINDOW_SCOPE_VIEWS[e] = {"LaTeXSymbolMapView": LaTeXSymbolMapView}
    EDITOR_SCOPE_VIEWS[e] = {"IssueView": IssueView, "LaTeXOutlineView": LaTeXOutlineView}

for e in BIBTEX_EXTENSIONS:
    EDITOR_SCOPE_VIEWS[e] = {"IssueView": IssueView, "BibTeXOutlineView": BibTeXOutlineView}


# editors

from ..latex.editor import LaTeXEditor
from ..bibtex.editor import BibTeXEditor

EDITORS = [LaTeXEditor, BibTeXEditor]


# ex:ts=4:et:
