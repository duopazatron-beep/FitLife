# Проект FitLife - MVP версия 1.0

# Воды на кг в мл
WATER_PER_KG = 30

# Заглушки разделители
sep_big = (("-" * 15) + ("=" * 30) + ("-" * 15))
sep_small = (("-" * 3) + ("=" * 5) + ("-" * 3))


# Задаёт вопрос и принимает в ответ только цифры (float)
def chek_answer(question):
    while True:

        try:

            ask = input(question)
            return float(ask)

        except ValueError:

            print(f'''{sep_big}
                  Неверный формат ввода!
{sep_big}''')


# Получение имени и возрастапше
print(f'''{sep_big}
            Приветствую! Бот FitLife готов помочь!
{sep_big}''')
ask_name = input(f"{sep_small} Как Вас зовут?: ")
user_name = ask_name.capitalize()
print(sep_big)
user_age = chek_answer(f"{sep_small} Сколько Вам лет, {user_name}?: ")
user_age = int(user_age)
print(sep_big)

# Сбор данных
print(f'''           Уточним некоторые данные для расчётов.
{sep_big}''')
user_weight = chek_answer(f"{sep_small} Укажите свой вес в киллограммах: ")
user_weight = round(user_weight, 2)
print(sep_big)
user_height = chek_answer(f"{sep_small} Укажите свой рост в метрах: ")
user_height = round(user_height, 2)

# Расчёт ИМТ: вес / рост в квадрате
bmi = (user_weight * 100) / ((user_height ** 2) * 100)
bmi = round(bmi, 1)
# Расчёт воды: вес * 30 мл
water_needed = (user_weight * WATER_PER_KG) / 1000
water_needed = round(water_needed, 1)

# Вывод результата: Имя, Возраст, ИМТ, Норма воды.
print(f'''{sep_big}
                Вот Ваш результат, {user_name}!
{sep_big}
{sep_small} Ваш возраст -------------------- {user_age}
{sep_small} Ваш Индекс Массы Тела ---------- {bmi}
{sep_small} Норма потребление воды в день -- {water_needed} л
{sep_big}
        Не забывайте думать о себе! Приятного дня.
{sep_big}''')
