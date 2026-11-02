from address import Address
from mailing import Mailing

# Создаём адреса
from_addr = Address("125009", "Москва", "Тверская", "13", "5")
to_addr = Address("630099", "Новосибирск", "Красный проспект", "35", "12")

# Создаём почтовое отправление
mailing = Mailing(
    to_address=to_addr,
    from_address=from_addr,
    cost=420,
    track="RU123456789RU"
)

# Формируем и выводим строку по шаблону
print(
    f"Отправление {mailing.track} "
    f"из {mailing.from_address.index}, {mailing.from_address.city}, "
    f"{mailing.from_address.street}, "
    f"{mailing.from_address.house} - {mailing.from_address.apartment} "
    f"в {mailing.to_address.index}, {mailing.to_address.city}, "
    f"{mailing.to_address.street}, "
    f"{mailing.to_address.house} - {mailing.to_address.apartment}. "
    f"Стоимость {mailing.cost} рублей."
)
