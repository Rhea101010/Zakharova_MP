# TODO Найдите количество книг, которое можно разместить на дискете
v = 1.44*1000000
stranitsy = 100
stroki = 50
symvoly = 25
symv = 4
kolvo = round((v / (stranitsy*stroki*symvoly*symv)),)

print("Количество книг, помещающихся на дискету:", kolvo)
