"""PDF to MP3"""

import pdfplumber
from gtts import gTTS
from pathlib import Path
import os


def pdf_to_mp3(path='file.pdf', lang='ru'):
    if Path(path).is_file() and Path(path).suffix == '.pdf':
        with pdfplumber.PDF(open(file=path, mode='rb')) as pdf:
            pages = [page.extract_text() for page in pdf.pages]
            txt = ''.join(pages).replace('/n', '')

        my_audio = gTTS(text= txt, lang= lang, slow=False)
        file_name = Path(path).stem
        my_audio.save(f"{file_name}.mp3")
        print(f"[+] {file_name}.mp3 has saved successfully\n")
        return os.system(f"afplay {file_name}.mp3")

    else:
        return 'File does not exit'


def main():
    path = input("\nEnter the file's path:\n")
    print(pdf_to_mp3(path=path))


if __name__ == '__main__':
    main()
