
def counting(n: int, m: int):
    '''
    функция путем деления и получения остатка определяет, кто вышел за этот цикл
    :param n: количество людей
    :param m: количество слогов
    :return: рекурсия. принимает теже аргументы только за минусом одного человека
    '''
    if len(list_people) == 1:
        return list_people[0]

    print(list_people)
    a = len(list_people)
    cycles = m % a
    print("cycles", cycles)

    list_people.pop(cycles-1)
    print(list_people)


    return counting(n-1, m)


if __name__ == "__main__":
    people = int(input("задайте количество людей "))
    slogi = int(input("задайте количество слогов "))
    list_people = [x for x in range(people)]
    print(counting(people, slogi))


#ygfugf