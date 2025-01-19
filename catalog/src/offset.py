def offset_product(offset_:int, count:int, quantity_per_page:int) -> tuple:
    """ Создает список странци (максимум count)
     начигая с числа на 4 меньше текущего зничения
     и на 4 больше текущего значения """

    offset_min = offset_ - 4
    if offset_min < 1:
        offset_min = 1
        data_offset_min = 0
    else:
        data_offset_min = 1
    offset_max = offset_ + 5
    if offset_max >= count // quantity_per_page + 2:
        offset_max = count // quantity_per_page + 2
        data_offset_max = False
    else:
        data_offset_max = count // quantity_per_page + 1

    data_offset = [i if i != offset_ else False for i in range(offset_min, offset_max)]

    return data_offset,data_offset_min,data_offset_max