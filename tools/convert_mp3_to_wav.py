"""
Setup FFMPEG before!!!
https://www.ffmpeg.org/download.html#build-windows
"""

from pydub import AudioSegment

names = [
    'shot',
    'explosion',
    'explosion_1'
]

for name in names:
    sound = AudioSegment.from_mp3(f"../sound/{name}.mp3")
    sound.export(f"../sound/{name}.wav", format="wav")
