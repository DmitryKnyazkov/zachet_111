def will_it_be_enough(list_):
    # sorted(list_, key=lambda x: x[0])
    list_.sort()
    print(list_)
    for_comparison = []
    for i in range(1, len(list_)):
        if list_[i-1][1] <= list_[i][0]:
            for_comparison.append(list_[i-1])
    for_comparison.append(list_[-1])

    if for_comparison == list_:
        return print("Да")
    else:
        return print("Нет")



if __name__ == "__main__":
    list_ = [(4, 6), (3,4), (12, 16), (18, 24)]
    will_it_be_enough(list_)
