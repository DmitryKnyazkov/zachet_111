import random

def sort_sort(list_: list) -> list:
    """
    сортирует список
    :param list_: список
    :return: отсортированный список
    """
    if not list_:
        return list_
    max_ = max(list_)
    counts = [0] * (max_+1)

    for value in list_:
        counts[value] += 1
    print(counts)
    result = []
    for i, co in enumerate(counts):
        result += [i] *co
    return result


if __name__ == "__main__":
    list_ = [random.randint(13, 25) for _ in range(20)]
    print(list_)
    print(sort_sort(list_))
