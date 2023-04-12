#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 2023

@author: iluzioDev

This document contains the constants used in Musa.
"""
import PySimpleGUI as gui

PROGRAM_NAME = "Musa v0.1.0"
THEME = "DarkBlack"
BACKGROUND_COLOR = "#2D3640"
BOX_COLOR = "#64778D"
BUTTON_COLOR = "#283B5B"
FONT = "Helvetica"

INPUT = [[gui.InputText(key="url", font=(FONT, 15))]]

OPTIONS = [[gui.Button("Download Video", font=(FONT, 15), button_color=BUTTON_COLOR),
            gui.Button("Download Audio", font=(FONT, 15), button_color=BUTTON_COLOR)]]

EXIT = [[gui.Button("Exit", font=(FONT, 15), button_color=BUTTON_COLOR)]]

LAYOUT = [[gui.Frame(title="Insert a YouTube Video URL", layout=INPUT, font=(FONT, 15), background_color=BOX_COLOR, border_width=2, pad=(0, 10))],
          [gui.Column([[gui.Frame(title="Options", layout=OPTIONS, font=(FONT, 15), background_color=BOX_COLOR, border_width=2)]]),
           gui.VSeparator(),
           gui.Column([[gui.Frame(title="Result", layout=[[gui.Text(key="output", font=(FONT, 12), background_color=BOX_COLOR)]], font=(FONT, 15), background_color=BOX_COLOR, border_width=2, size=(175, 75))]]),
           gui.VSeparator(),
           gui.Column(EXIT, element_justification="right", background_color=BACKGROUND_COLOR)]
          ]

OUTPUT_PATH = "downloads"

NO_URL = "Please, enter a URL!"

SUCCESS = "Download completed!"

INVALID_URL = "Invalid URL!"
UNAVAILABLE = "This video is unavailable for the moment"
