from itertools import accumulate


# Нахождение диапазона гистограммы
def find_range(input_data, threshold_value):
    """""
    Функция нахождения диапазона гистограммы.
    Входные параметры:
        input_data - массив интенсивности (гистограмма)
        threshold_value - значение порога
    Выходные параметры:
        start_index (end_index) - индекс крайнего элемента гистограммы
    """""
    data = input_data[:]
    data_rev = data[:]
    data_rev.reverse()

    sum_data = sum(data)
    ex = False
    start_index = end_index = cur_sum = 0
    size = len(data)

    while not ex:
        if data[start_index] > data_rev[end_index]:
            cur_sum = cur_sum + data_rev[end_index]
            if (cur_sum * 100) / sum_data > threshold_value:
                ex = True
            end_index = end_index + 1
        else:
            cur_sum = cur_sum + data[start_index]
            if (cur_sum * 100) / sum_data > threshold_value:
                ex = True
            start_index = start_index + 1
    end_index = size - end_index

    return start_index, end_index


def get_new_list(hist_data, threshold_value):
    """""
    Функция нахождения диапазона гистограммы.
    Входные параметры:
        hist_data - исходный массив интенсивности (гистограмма)
        threshold_value - значение порога
    Выходные параметры:
        ind_list - индексы выходного массива интенсивности (с учетом порога)
        lib_list - значения выходного массива интенсивности (с учетом порога)
        from_min - начало гистограммы
        from_max - конец гистограммы
         """""
    # Создаем словарь интенсивности{номер цвета:кол-во}
    hist_lib = {index: value for (index, value) in enumerate(hist_data)}
    # Нахождение диапазона исходной гистограммы
    from_min, from_max = find_range(hist_data, threshold_value)
    print(from_min, from_max)
    # Словарь состоящий из значений диапазона
    new_lib = {index: value for index, value in hist_lib.items() if from_min < index < from_max}
    # Опред. процент (задается параметром THRESHOLD_VALUE) самых светлых пикселей станут белыми
    max_lib = {index: 255 for index, value in hist_lib.items() if index > from_max}
    # Опред. процент (задается параметром THRESHOLD_VALUE)самых темных пикселей станут черными
    min_lib = {index: 0 for index, value in hist_lib.items() if index < from_min}
    # Объединяем словари
    hist_lib.update(new_lib)
    hist_lib.update(max_lib)
    hist_lib.update(min_lib)
    # Разбиваем словарь на элементы и индексы (в правильном порядке)
    lib_list = [v for k, v in sorted(hist_lib.items())]
    ind_list = [k for k, v in sorted(hist_lib.items())]
    return ind_list, lib_list, from_min, from_max


if __name__ == "__main__":
    test_data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 12, 19, 49, 93, 220, 488, 1061, 1747, 2160, 2718,
                 3259, 4039, 5108, 6395, 8463, 10610, 13530, 16115, 19125, 22186, 25696, 28701, 28324, 25759, 24369,
                 23578, 21775, 20385, 19839, 19781, 19445, 18856, 18457, 17906, 17917, 17806, 18485, 17680, 15799,
                 14163, 12812, 11576, 10751, 9899, 9380, 8863, 8399, 7404, 6403, 5911, 5591, 5150, 4610, 4320, 3860,
                 3616, 3430, 3063, 2649, 2213, 2046, 1859, 1692, 1484, 1362, 1290, 1153, 1232, 1300, 1520, 1384, 1527,
                 1735, 1851, 1532, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    ind, arr, min_ind, max_ind = get_new_list(test_data, 5)
    print("New array: ", arr)
    print("Min index: ", min_ind)
    print("Max index: ", max_ind)
