import os
import sys
import re
from pathlib import Path

def main():
    # print( Path.cwd() )
    path_files = sys.argv[1]
    # print(os.listdir(path_files))

    # names_files = os.listdir(path_files)
    suffixes_videos = ['.mkv', '.mp4']
    suffix_subtitle = '.srt'
    video_info = {}
    name_file = []
    p = Path(path_files)
    temp = {}

    for file in p.glob('*'):
        if file.suffix in suffixes_videos:
            temp['video'] = file.stem
        if file.suffix == suffix_subtitle:
            temp['subtitle'] = file.stem
        if temp['video'] and temp['subtitle']:
            pass


    video_info['cap'] = temp

    print(video_info)

    # Determinar numero de capitulo
    # Determinar subtitulo del numero de capitulo


def obtener_temporada(name_file):
    temp_regex = re.compile(r'(S|s)\d\d')
    mo = temp_regex.search(name_file)
    print('La temporada es:', mo.group())

def obtener_capitulo(name_file):
    capitulo_regex = re.compile(r'(E|e)\d\d')
    mo = capitulo_regex.search(name_file)
    print('El capitulo es:', mo.group())




if __name__ == "__main__":
    main()
