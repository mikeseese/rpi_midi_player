#!/usr/bin/python

import os.path

media_user = "seese"
media_host = "192.168.1.202"

daemon_location = "/home/pi/midi_daemon/"

playlists = {
  "classics" : "/home/mike/media/midi/classics/",
  "holidays" : "/home/mike/media/midi/holidays/",
  "general" : "/home/mike/media/midi/general/",
}

current_playlist = "classics"

while True:
  next_playlist = current_playlist
  with open(daemon_location + 'current_playlist', 'r') as content_file:
    next_playlist = content_file.read()

  if(next_playlist != current_playlist):
    if(playlists.has_key(current_playlist):
      current_playlist = next_playlist
      # stop current song
      # remove songs
      # pull current song on new playlist
      # play song
      # pull other songs
    else:
      # the queued playlist doesn't exist to us, let's not change anything

  # check if we want to pause or play
  # MIDI_PLAY file says we want to play.
  # MIDI_PAUSE file is not used by script but exists for consistency
  play_music = os.path.isfile(daemon_location + "MIDI_PLAY");

  # check if we want to go previous or back
  go_previous = os.path.isfile(daemon_location + "MIDI_PREV")
  go_next = os.path.isfile(daemon_location + "MIDI_NEXT")
  if(go_next):
    # stop current song
    # get next song if necessary
    # play next song
    # remove previous song
    # rename current/next songs
    # grab next song
  elif(go_previous):
    # stop current song
    # get previous song if necessary
    # play previous song
    # remove next song
    # rename current/previous songs
    # grab previous song

  # remove flags for prev/next controls
  if(go_previous):
    os.remove(daemon_location + "MIDI_PREV");
  if(go_next):
    os.remove(daemon_location + "MIDI_NEXT");


  sleep(0.1)