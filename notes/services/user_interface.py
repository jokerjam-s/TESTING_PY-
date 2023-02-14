'''
    взаимодействие с пользователем

'''
import datetime
import re


class UserIterface:
    # Отображает пользовательское меню
    #   menu_dict - словарь с пунктами меню формата {int => str, ... }
    #   где ключевые значения соответствуют еомеру, заправшиваемому у пользователя
    #   если будет введено значение вне диапазока ключей - вернет 0
    def show_menu(self, menu_dict: dict):
        for i in menu_dict.keys():
            print(i, " - ", menu_dict[i])

        try:
            menu = int(input("> "))
        except:
            menu = 0

        if menu in menu_dict.keys():
            return menu

        return 0

    # запрашивает строковое значенееи у пользователя
    #      message - сообщение для пользователя
    def ask_str(self, message):
        return input(message)

    # заправшивает целочисленное значение у пользователя
    #   message - сообщенеи для пользователя
    def ask_int(self, message):
        str_value = input(message)
        value = 0
        try:
            value = int(str_value)
        except:
            print("Ошибка, неверный ввод. По умолчанию значение 0")

        return value

    # запращивает дату у пользователя в формате ДД.ММ.ГГГГ
    #   message - сообщенеи для пользователя
    def ask_date(self, message):
        now_date = datetime.datetime.date()

        value = self.__ask_pattern__(message,
                                     "^(0?[1-9]|[12][0-9]|3[01])[.](0?[1-9]|1[012])[.](\\d{4})$",
                                     "Ошибка, неверный ввод. По умолчанию текущая дата",
                                     now_date.strftime("%d.%m.%Y"))

        return value

    # запрашивает время у пользователя в формате ЧЧ:ММ
    #   message - сообщение для пользователя
    def ask_time(self, mesage):
        now_time = datetime.datetime.time()

        value = self.__ask_pattern__(mesage,
                                     "^([0-1][0-9]|2[0-3]):([0-5][0-9])$",
                                     "Ошибка, неверный ввод. По умолчанию текущее время",
                                     now_time.strftime("%HH:MM"))
        return value

    # Запрашивает значение у пользователя согласно шаблона в случае ошибки
    # возвращает значение по умолчанию с выводом сообщения об ошибке
    def __ask_pattern__(self, message, pattern, err_message, default_val):
        value = input(message)
        validator = re.compile(pattern)

        if (validator.match(value)):
            return value

        print(err_message)
        return default_val
