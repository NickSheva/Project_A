"""Find words more or equalse four letters"""
## Зависимости
import re
from typing import Union
from art import *


tprint('find length', font='random')
## Данные
poem = """
Call me Ishmael. Some years ago - never mind how long precisely - having
little or no money in my purse, and nothing particular to interest me
on shore, I thought I would sail about a little and see the watery part
of the world. It is a way I have of driving off the spleen, and regulating
the circulation. - Moby Dick"""


def find_len() -> Union[str, list]:
    """ Найти слова больше и равные четырем буквам в тексте"""
    parser = re.findall(r'\w+', poem)
    word = [x for x in parser if len(x) >= 4]
    ## результат
    return f"{poem = }\n\n\033[34m{word = }\033[0m\n\n{len(word)}"


if __name__ == "__main__":
    print(find_len())
