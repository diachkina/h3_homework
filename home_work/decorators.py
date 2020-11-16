# Напишите декоратор для превращения функции print в генератор html-тегов
# Декоратор должен принимать список тегов italic, bold, underline
# Результатом работы декоратора с аргументами italic, bold должно быть преобразование
# из строки вида "test string" в "<i><b>test string</b></i>"

def str_to_html(tags):
    tags_list = tags
    def decorator(func):
        tag_base = {
            "italic": f"<i>%text%</i>",
            "bold": f"<b>%text%</b>",
            "underline": f"<u>%text%</u>",
        }
        def wrapper(text):
            html_str = f'<{tags_list[1][0]}><{tags_list[0][0]}>{text}</{tags_list[0][0]}></{tags_list[1][0]}>'
            print(html_str)
            return func
        return wrapper
    return decorator


@str_to_html(["italic", "bold"])
def get_text(text):
    return text

print(get_text('1234'))



# Напишите функцию, которая возвращает список файлов из директории.
# Напишите декоратор для этой функции, который прочитает все файлы с
# раширением .log из найденных

import os
def log_reading(func):
    def wrapper(*args):
        log_file_list = [x for x in os.listdir(*args) if x.endswith('.log')]
        for file in log_file_list:
            open(file)
        return func()
    return wrapper


@log_reading
def get_files():
    file_list = os.listdir()
    return file_list


print(get_files())