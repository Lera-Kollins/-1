# TODO Найдите количество книг, которое можно разместить на дискете

disk_byt = 1.44 * 1024 * 1024
books = 100 * 50 * 25 * 4
print("Количество книг, помещающихся на дискету:", int(disk_byt // books))
