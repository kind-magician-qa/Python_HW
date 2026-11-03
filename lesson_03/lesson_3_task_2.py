from smartphone import Smartphone

# Создаём список catalog
catalog = []

# Добавляем 5 разных экземпляров класса Smartphone  в список. (метод "append")
catalog.append(Smartphone("Samsung", "Galaxy S23", "+79001112233"))
catalog.append(Smartphone("Apple", "iPhone 15", "+79004445566"))
catalog.append(Smartphone("Xiaomi", "Redmi Note 12", "+79007778899"))
catalog.append(Smartphone("Huawei", "P60 Pro", "+79002223344"))
catalog.append(Smartphone("Google", "Pixel 8", "+79005556677"))

# Цикл, который печатает весь каталог в формате
# <марка> - <модель>. <номер телефона>
for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")
