from itertools import accumulate
from PIL import Image
from src import global_values, image_url
import matplotlib.pyplot as plt


def equalize(img):
    """""
    Функция эквализации изображения.
    Входные параметры:
        input_img - объект исходного изображения
    Выходные параметры:
        output_pixels - список пикселей после эквализации
    """""
    # Получаем список пикселей исходного изображения
    gray_pixels_list = list(img.getdata())
    # Получаем гистограмму изображения
    img_histogram = img.histogram()
    # Создаем словарь из списка интенсивности пикселей (гистограммы)
    lib_histogram = {index: value for index, value in enumerate(img_histogram)}
    # Разбиваем словарь на элементы и индексы (в правильном порядке)
    val_list = [v for k, v in sorted(lib_histogram.items())]
    ind_list = [k for k, v in sorted(lib_histogram.items())]
    # Находим общее количество пикселей в изображении
    data_sum = len(gray_pixels_list)-1
    # Отображаем старые значения на интервал от 0 до 255
    cdf = [((index - 1)/data_sum)*255 for index in accumulate(val_list)]
    # Создаем словарь с эквализированными пикселями
    result = {index: value for index, value in zip(ind_list, cdf)}
    # Инициализируем выходной список пикселей изображения
    output_pixels = gray_pixels_list[:]
    # Производим замену значений
    for index, value in enumerate(gray_pixels_list):
        if value in result:
            output_pixels[index] = result[value]
    return output_pixels

if __name__ == "__main__":

    img_test = Image.open(image_url.get_url(global_values.INPUT_IMAGE)).convert("L")
    hist_data_test = img_test.histogram()

    equalized_pixels = equalize(img_test)

    eq_image = Image.new("L", img_test.size)
    eq_image.putdata(equalized_pixels)
    eq_image.save(image_url.get_url(global_values.IMAGE_EQUAL))
    hist_data_eq = eq_image.histogram()

    fig = plt.figure(1)
    plot = fig.add_subplot(2, 1, 1)
    plot.set_title('Эквализация гистограммы')
    plot.set_ylabel('кол-во пикселей')
    plot.bar([i for i in range(len(hist_data_test))], hist_data_test)

    plot = fig.add_subplot(2, 1, 2)
    plot.set_ylabel('кол-во пикселей')
    plot.set_xlabel('цвет пикселя [0..255]')
    plot.bar([i for i in range(len(hist_data_eq))], hist_data_eq)

    plt.show()
