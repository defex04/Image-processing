def borders_operators(width, row, k, img_with_border):

    if len(k) == 4:
        v = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        v[0] = k[0]
        v[1] = k[1]
        v[3] = k[2]
        v[4] = k[3]
        k.clear()
        k.extend(v)

    # Выходное изображение без рамки
    g_out = [0 for _ in range((width - 2) * (row - 2))]
    # Умножаем каждый пиксель на оператор
    for i in range(1, row - 1):
        for j in range(1, width - 1):
            g_out[(width - 2) * (i - 1) + (j - 1)] = img_with_border[width * (i - 1) + (j - 1)] * k[0] + \
                                                 img_with_border[width * (i - 1) + j] * k[1] + \
                                                 img_with_border[width * (i - 1) + (j + 1)] * k[2] + \
                                                 img_with_border[width * i + (j - 1)] * k[3] + \
                                                 img_with_border[width * i + j] * k[4] + \
                                                 img_with_border[width * i + (j + 1)] * k[5] + \
                                                 img_with_border[width * (i + 1) + (j - 1)] * k[6] + \
                                                 img_with_border[width * (i + 1) + j] * k[7] + \
                                                 img_with_border[width * (i + 1) + (j + 1)] * k[8]
    return g_out


def borders_filter(width, row, k, img_with_border):

    # Выходное изображение без рамки
    g_out = [0 for _ in range((width - 2) * (row - 2))]
    # Умножаем каждый пиксель на оператор
    for i in range(1, row - 1):
        for j in range(1, width - 1):
            g_out[(width - 2) * (i - 1) + (j - 1)] = (img_with_border[width * (i - 1) + (j - 1)] * k[0] + \
                                                 img_with_border[width * (i - 1) + j] * k[1] + \
                                                 img_with_border[width * (i - 1) + (j + 1)] * k[2] + \
                                                 img_with_border[width * i + (j - 1)] * k[3] + \
                                                 img_with_border[width * i + j] * k[4] + \
                                                 img_with_border[width * i + (j + 1)] * k[5] + \
                                                 img_with_border[width * (i + 1) + (j - 1)] * k[6] + \
                                                 img_with_border[width * (i + 1) + j] * k[7] + \
                                                 img_with_border[width * (i + 1) + (j + 1)] * k[8])/16
    return g_out


def norm(rawpoints, high, low):
    OldMax = max(rawpoints)
    OldMin = min(rawpoints)
    OldRange = (OldMax - OldMin)

    NewRange = (high - low)
    NewValue = [(((OldValue - OldMin) * NewRange) / OldRange) + low for OldValue in rawpoints]
    return NewValue

if __name__ == "__main__":

    input = [1, -1, 2, 0, 0, 1, -1]
    print(norm(input, 1.3, 1.0))