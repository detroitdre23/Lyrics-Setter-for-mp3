from pathlib import Path
from lyricsgenius import Genius
import eyed3
import re
import os
# key = input("Key : ")
genius = Genius('5-u1onOZ-1iko0yEe-MXJymxRoOrCUsU8w5Z3tpMsWaXQIE-0P1RYymOyd1WO4cU')
# genius = Genius(key)
file_path = input("File Path : ")
file_paths = os.listdir(file_path)
for f in file_paths:
    if ".mp3" in f:
        start = f.find('-') + 2
        end = f.find('.mp3') 
        track = f[start:end]
        end = f.find('-') - 1
        artist = f[:end]
        song = genius.search_song(track, artist)
        start = song.lyrics.find('[') 
        song.lyrics = song.lyrics[start:]
        path = os.path.join(file_path, f)
        audio = eyed3.load(path)
        if audio.tag is None:
            audio.tag = eyed3.id3.Tag()
        audio.tag.artist = artist
        audio.tag.title = track
        audio.tag.lyrics.set(song.lyrics)
        audio.tag.save()
