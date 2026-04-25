# Проект FitLife - MVP версия 1.0
# 1. Знакомство # Ввод данных пользователя Имя /возраст
print('Добрый день! Вас приветствует Ваш лучший Фитнес-тренер!')


# 2. Сбор данных: запрос возраста(int), веса в кг (float) и роста в м (float)
def ask_user(ask):
    if ask != 'Представьтесь, пожалуйста!   ':
        while True:
            try:
                user_parametr = float(input(ask))
                break
            except ValueError:
                print('Ошибка: Введите число!')
    else:
        user_parametr = input(ask)
    return user_parametr


user_name = ask_user('Представьтесь, пожалуйста!   ')


user_age = int(ask_user('Сколько лет Вам исполнилось последний раз?  '))


user_weight = ask_user('Введите, пожалуйста, Ваш вес в формате XX.X  ')


user_height = ask_user('Введите, пожалуйста, Ваш рост '
                       'в метрах в формате Y.YY  ')


# 3. Логика расчетов (Функции как "черный ящик": используем арифметику)
# Формула ИМТ: вес разделить на (рост в квадрате)
bmi = user_weight / user_height ** 2

# Подсчет воды: вес * 30 мл
WATER_PER_KG = 30  # мл на 1 кг норма воды
ML_IN_LITER = 1000  # мл в 1 литре
# Расчёт нормы потребления воды
water_needed = user_weight * WATER_PER_KG / ML_IN_LITER


# 4. Вывод красивого результата
print(f"Приятно познакомиться, {user_name}!")
print(f"В Ваш замечательный возраст {user_age} лет ИМТ составляет: {bmi:.1f}")
# Вывод возраста, ИМТ и нормы воды.
print(f"Норма потребления воды составляет: {water_needed:.1f} л. в день.")
print('Расчет окончен. Будьте здоровы!')
