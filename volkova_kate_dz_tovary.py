goods = []
to_be_continued = True

nazvanie = []
cena = []
kolichestvo = []
edinicy = []
data_for_goods = {"название": nazvanie, "цена": cena, "количество": kolichestvo, "ед": edinicy}

while to_be_continued == True:
    descriptions = []
    n = int(input('Введите номер товара: '))
    descriptions.append(n)

    d = {}
    name = input('Введите название товара: ')
    d['name'] = name
    price = int(input('Введите цену товара: '))
    d['price'] = price
    amount = int(input('Введите количество товара: '))
    d['amount'] = amount
    ed = input('Введите единицы измерения количества товара: ')
    d['ed'] = ed

    descriptions.append(d)
    descriptions = tuple(descriptions)

    goods.append(descriptions)

    c = input('Вы хотите продолжить? (д/н) ')
    if c == 'д':
        to_be_continued = True
    else:
        to_be_continued = False

    data_for_goods["название"] = nazvanie.append(name)
    data_for_goods["цена"] = cena.append(price)
    data_for_goods["количество"] = kolichestvo.append(amount)
    data_for_goods["ед"] = edinicy.append(ed)

print(goods)
print(data_for_goods)

