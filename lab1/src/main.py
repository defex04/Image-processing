from PIL import Image
import matplotlib.pyplot as plt
from src import equalization, linearization, image_url, global_values


# Преобразование цветного изображения в оттенки серого
def rgb_to_gray(r, g, b):
    return 0.2989 * r + 0.5876 * g + 0.1148 * b

# Выполнение лабораторной работы №1

# Задание №1. Преобразование изображение в оттенки серого
# Открытие изображения
img = Image.open(image_url.get_url(global_values.INPUT_IMAGE)).convert('RGB')

# Изменение цвета пикселей в оттенки серого
pixels = list(img.getdata())
gray_pixel = [rgb_to_gray(*pixel) for pixel in pixels]

# Сохранение изображения в оттенках серого с одним каналом (L)
gray_image = Image.new("L", img.size)
gray_image.putdata(gray_pixel)
gray_image.save(image_url.get_url(global_values.IMAGE_GRAY))

hist_data = gray_image.histogram()

# Задание №2. Линейное растяжение гистограммы
lin_pixels = linearization.linear_stretching(gray_image, global_values.THRESHOLD_VALUE)
lin_image = Image.new("L", img.size)
lin_image.putdata(lin_pixels)
lin_image.save(image_url.get_url(global_values.IMAGE_LIN))
hist_data_lin = lin_image.histogram()


# Задание №3. Эквализация изображения
equalized_pixels = equalization.equalize(gray_image)
eq_image = Image.new("L", img.size)
eq_image.putdata(equalized_pixels)
eq_image.save(image_url.get_url(global_values.IMAGE_EQUAL))
hist_data_eq = eq_image.histogram()

# Построение графиков
fig = plt.figure(1)
plot = fig.add_subplot(3, 1, 1)
plot.set_title('Гистограмма исходного изображения')
plot.bar([i for i in range(len(hist_data))], hist_data)

plot = fig.add_subplot(3, 1, 2)
plot.set_title('Линейное растяжение гистограммы')
plot.set_ylabel('кол-во пикселей')
plot.bar([i for i in range(len(hist_data_lin))], hist_data_lin)

plot = fig.add_subplot(3, 1, 3)
plot.set_title('Эквализация')
plot.set_xlabel('цвет пикселя [0..255]')
plot.bar([i for i in range(len(hist_data_eq))], hist_data_eq)

plt.subplots_adjust(hspace=0.5)

plt.show()
