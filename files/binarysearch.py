""""Экспоненциальный поиск"""
import timeit
import sys


def search(lst, item):
    """Поиск значение  в отсортированном массиве,
    алгоритм сравнивает item со значением среднего элемента массива, который мы будем называть mid.
    Если mid — это тот элемент, который мы ищем (в лучшем случае),
    мы возвращаем его индекс. Если нет, мы определяем,
    в какой половине массива мы будем искать item дальше, основываясь на том,
    меньше или больше значение val значения mid, и отбрасываем вторую половину массива.
    Затем мы рекурсивно или итеративно выполняем те же шаги, выбирая новое значение для mid,
    сравнивая его с item и отбрасывая половину массива на каждой итерации алгоритма.
    """
    low = 0
    high = len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = lst[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


lys = [1, 2, 3, 4, 5, 6, 7, 8, 9]
if __name__ == '__main__':
    print(search(lys, 5))
    print(timeit.timeit('search(lys, 1)',
                        setup='from __main__ import search, lys'), file=sys.stderr)
