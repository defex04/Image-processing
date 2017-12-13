from PIL import Image, ImageOps
from math import fabs
from src.edge_detection import borders_operators, borders_filter, norm
from src import image_url, global_values


# Преобразование цветного изображения в оттенки серого
def rgb_to_gray(r, g, b):
    return 0.2989 * r + 0.5876 * g + 0.1148 * b


# Выполнение лабораторной работы №3

# Матрица Лапласиана для выдиления границ
laplasian = [-1, -1, -1, -1, 8, -1, -1, -1, -1]
# Фильтр Гаусса
gauss_filt = [1, 2, 1, 2, 4, 2, 1, 2, 1]

# Преобразование изображение в оттенки серого
# Открытие изображения
img = Image.open(image_url.get_url(global_values.INPUT_IMAGE)).convert('RGB')

# Изменение цвета пикселей в оттенки серого
pixels = list(img.getdata())
gray_pixel = [rgb_to_gray(*pixel) for pixel in pixels]

# Сохранение изображения в оттенках серого с одним каналом (L)
gray_image = Image.new("L", img.size)
gray_image.putdata(gray_pixel)
gray_image.save(image_url.get_url(global_values.IMAGE_GRAY))

# Задаем рамку исходному изображению (1 пиксель)
image_with_empty_border = ImageOps.expand(gray_image, border=1, fill=255)

# Получаем количество пикселей по осям X, Y
x = image_with_empty_border.size[0]
y = image_with_empty_border.size[1]

img_without_border = list(gray_image.getdata())

# Инициализируем матрицу изображения размером изображения без рамки
g = img_without_border[:]
img_input = g[:]

# Получаем список пикселей изображения с пустой рамкой
img_with_border = list(image_with_empty_border.getdata())

# Заполняем рамку изображения соседними цветами
for i in range(x):
    img_with_border[i] = img_with_border[i + x]
    img_with_border[i + x * (y - 1)] = img_with_border[i + x * (y - 2)]

for i in range(y):
    img_with_border[i * x] = img_with_border[i * x + 1]
    img_with_border[i * x + x - 1] = img_with_border[i * x + x - 2]


# Задание №1. Фильтр Гаусса
image_gauss = borders_filter(x, y, gauss_filt, img_with_border)

# Сохранение изображений в оттенках серого с одним каналом (L)
gauss_image = Image.new("L", img.size)
gauss_image.putdata(image_gauss)
gauss_image.save(image_url.get_url(global_values.IMAGE_GAUSSFIL))

# Задание №2. Применение Лапласиана для выдиления границ

img_ga = Image.open(image_url.get_url(global_values.IMAGE_GAUSSFIL)).convert('L')


# Задаем рамку исходному изображению (1 пиксель)
image_with_empty_border_fill = ImageOps.expand(img_ga, border=1, fill=255)


# Получаем количество пикселей по осям X, Y
x2 = image_with_empty_border_fill.size[0]
y2 = image_with_empty_border_fill.size[1]

# Получаем список пикселей изображения с пустой рамкой
img_with_border2 = list(image_with_empty_border_fill.getdata())

# Заполняем рамку изображения соседними цветами
for i in range(x):
    img_with_border2[i] = img_with_border2[i + x]
    img_with_border2[i + x * (y - 1)] = img_with_border2[i + x * (y - 2)]

for i in range(y):
    img_with_border2[i * x] = img_with_border2[i * x + 1]
    img_with_border2[i * x + x - 1] = img_with_border2[i * x + x - 2]


# Умножаем каждый пиксель изображения на матрицу оператора
g_lap = borders_operators(x, y, laplasian, img_with_border2)

# Сохранение изображений в оттенках серого с одним каналом (L)
lap_image = Image.new("L", img.size)
lap_image.putdata(g_lap)
lap_image.save(image_url.get_url(global_values.IMAGE_LAPLASIAN))


img_la = Image.open(image_url.get_url(global_values.IMAGE_LAPLASIAN)).convert('L')

img_lap = list(img_la.getdata())

# Задание №3. Повышение резкости на 30%
print(min(img_lap), max(img_lap))
image_norm = norm(img_lap, high=1.5, low=1)

result = [x for x in map(lambda x, y: x*y, image_norm, img_input)]

# Сохранение изображений в оттенках серого с одним каналом (L)
res_image = Image.new("L", img.size)
res_image.putdata(result)
res_image.save(image_url.get_url(global_values.IMAGE_RESULT))