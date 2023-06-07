"""Линейный поиск"""


def linear(spisok, item):
    """Найти первое вхождение элементаю
    Временная сложность линейного поиска равна O(n)."""
    for i, j in enumerate(spisok):
        if j == item:
            return i
    return None


lst = [1, 3, 5, 6, 2, 4]
if __name__ == '__main__':
    print(linear(lst, 3))
