"""
Setup FFMPEG before!!!
https://www.ffmpeg.org/download.html#build-windows
"""
import pathlib
from os import listdir

from pydub import AudioSegment

my_path = '../sound'

black_list = ('background.mp3')

for file_name in listdir(my_path):
    if file_name not in black_list and pathlib.Path(file_name).suffix.upper() == '.MP3':
        name = pathlib.Path(file_name).stem
        sound = AudioSegment.from_mp3(f"../sound/{file_name}")
        sound.export(f"../sound/{name}.wav", format="wav")
