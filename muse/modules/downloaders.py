#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 2023

@author: iluzioDev

This document contains the functions used to download videos and audios from YouTube with muse.
"""
import os
import pytube
import PySimpleGUI as gui
import modules.constants as CONSTS

def download_video(url):
  """
  Downloads a video from youtube (MP4 format and highest resolution possible).
  Said video is saved in the output path.
  See `modules.constant.OUTPUT_PATH` for more information.

  Args:
    url (str): The URL of the video to be downloaded.
      
  Returns:
    str: A message indicating whether the download was successful or not.
  """
  if not url or not isinstance(url, str):
    gui.popup(CONSTS.NO_URL, title=CONSTS.PROGRAM_NAME)
    
  try:
    video = pytube.YouTube(url)
    video.streams.get_highest_resolution().download(output_path=CONSTS.OUTPUT_PATH)
    return CONSTS.SUCCESS
  except pytube.exceptions.RegexMatchError:
    return CONSTS.INVALID_URL
  except pytube.exceptions.VideoUnavailable:
    return CONSTS.UNAVAILABLE
    
def download_audio(url):
  """
  Downloads the audio from a video from youtube (in MP3 format).
  Said audio is saved in the output path.
  See `modules.constant.OUTPUT_PATH` for more information.

  Args:
    url (str): The URL of the video to be downloaded.
    
  Returns:
    str: A message indicating whether the download was successful or not.
  """
  if not url or not isinstance(url, str):
    gui.popup(CONSTS.NO_URL, title=CONSTS.PROGRAM_NAME)
    
  try:
    video = pytube.YouTube(url)
    mp4file = video.streams.get_audio_only().download(output_path=CONSTS.OUTPUT_PATH)
    base, *_ = os.path.splitext(mp4file)
    mp3file = base + ".mp3"
    if os.path.exists(mp3file):
      os.remove(mp3file)
    os.rename(mp4file, mp3file)
    return CONSTS.SUCCESS
  except pytube.exceptions.RegexMatchError:
    return CONSTS.INVALID_URL
  except pytube.exceptions.VideoUnavailable:
    return CONSTS.UNAVAILABLE
