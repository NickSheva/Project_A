"""PDF to MP3"""

import pdfplumber
from gtts import gTTS
from pathlib import Path


def pdf_to_mp3(path='file.pdf', lang='ru'):
    if Path(path).is_file() and Path(path).suffix == '.pdf':
        return "Yes"
    else:
        return 'File does not exit'


def main():
    path = input("\nEnter the file's path:\n")
    print(pdf_to_mp3(path=path))


if __name__ == '__main__':
    main()
