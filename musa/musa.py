#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 2023

@author: iluzioDev

Musa is a simple tool for downloading and converting YouTube videos to MP3 or MP4.
"""
import PySimpleGUI as gui
import modules.constants as CONSTS
import modules.downloaders as DL

def main():
  """
  Starts the GUI and handles the events and features of musa.
  """
  gui.theme(CONSTS.THEME)
  window = gui.Window(title=CONSTS.PROGRAM_NAME, layout=CONSTS.LAYOUT, margins=(25, 25), background_color=CONSTS.BACKGROUND_COLOR)
  
  while True:
    event, *_ = window.read()
    if event == gui.WIN_CLOSED or event == "Exit":
      break
    
    if event == "Download Video":
      window["output"].update(DL.download_video(window["url"].get()))
    if event == "Download Audio":
      window["output"].update(DL.download_audio(window["url"].get()))
  return

if __name__ == '__main__':
  main()
