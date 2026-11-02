def month_to_season(month: int) -> str:
    """
    Возвращает название сезона по номеру месяца.
    Параметры:
        month (int): номер месяца (1–12)
    Возвращает:
        str: название сезона («Зима», «Весна», «Лето», «Осень»)
             или сообщение об ошибке, если номер некорректен.
    """
    if month in (12, 1, 2):
        return "Зима"
    elif month in (3, 4, 5):
        return "Весна"
    elif month in (6, 7, 8):
        return "Лето"
    elif month in (9, 10, 11):
        return "Осень"
    else:
        return "Некорректный номер месяца"

# Вызов функции
print(month_to_season(12))
