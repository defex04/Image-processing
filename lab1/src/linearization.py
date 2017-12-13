from PIL import Image
from src import threshold, global_values, image_url
import matplotlib.pyplot as plt
from collections import Counter



def linear_stretching(input_img, threshold_value):
    """""
    Функция линейного растяжения изображения.
    Входные параметры:
        input_img - объект исходного изображения
        threshold_value - значение порога
    Выходные параметры:
        output_pixels - список пикселей после эквализации
    """""
    # Получаем пиксели исходного изображения
    gray_pixels_list = list(input_img.getdata())
    # Определяем интенсивность пикселей (гистограмма)
    hist_data = input_img.histogram()
    # Нахождение диапазона исходной гистограммы
    index_list, value_list, from_min, from_max = threshold.get_new_list(hist_data, threshold_value)
    # Формула линейного растяжения
    linear_values = [((255 / (from_max - from_min)) * (pixel_in - from_min)) for pixel_in in
                     index_list]
    # Создаем словарь с эквализированными пикселями
    result = {index: value for index, value in zip(index_list, linear_values)}
    # Производим замену значений
    output_pixels = gray_pixels_list[:]
    for index, value in enumerate(gray_pixels_list):
        if value in result:
            output_pixels[index] = result[value]
    return output_pixels

if __name__ == "__main__":
    img_test = Image.open(image_url.get_url(global_values.INPUT_IMAGE)).convert("L")
    hist_data_test = img_test.histogram()

    # Реализация гистограмы
    new_histogram = {i: 0 for i in range(256)}
    hist_data = Counter(img_test.getdata())
    new_histogram.update(hist_data)
    histogram_data = [new_histogram[key] for key in sorted(new_histogram.keys())]
    #

    linear_pixels = linear_stretching(img_test, global_values.THRESHOLD_VALUE)

    lin_image = Image.new("L", img_test.size)
    lin_image.putdata(linear_pixels)
    lin_image.save(image_url.get_url(global_values.IMAGE_LIN))
    hist_data_lin = lin_image.histogram()

    fig = plt.figure(1)
    plot = fig.add_subplot(2, 1, 1)
    plot.set_title('Линейное растяжение')
    plot.set_ylabel('кол-во пикселей')
    plot.bar([i for i in range(len(hist_data_test))], hist_data_test)

    plot = fig.add_subplot(2, 1, 2)
    plot.set_ylabel('кол-во пикселей')
    plot.set_xlabel('цвет пикселя [0..255]')
    plot.bar([i for i in range(len(hist_data_lin))], hist_data_lin)

    plt.show()
