def catalog_finder(url_list):
    """
    Дописать функцию, которая принимает список URL, а возвращает
    список только тех URL, в которых есть /catalog/
    """
    result_list = list()
    for url in url_list:
        if '/' in url:
            result_list.append(url)
    return result_list

# вопрос: как мне сказать интерпретатору, что меня интересует именно '/',а не '//'?
url_list = ['www.worldwildlife.org', 'https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/',
            'https://xn--80ahcjeib4ac4d.xn--p1ai/information/python_object_oriented_programming_oop/',
            'rezka.ag', 'friends.in.ua']
print(catalog_finder(url_list))


def get_str_center(input_str):
    """
    Дописать функцию, которая вернет Х символов из середины строки
    (2 для четного кол-ва символов, 3 - для нечетного).
    """
    for index in range(len(input_str)):
        index = int(len(input_str)/2)
        if len(input_str) % 2 == 0:
            return input_str[index-1], input_str[index]
        else:
            return input_str[index-1], input_str[index], input_str[index+1]


print(get_str_center('qwerty'))


def count_symbols(input_str):
    """
    Дописать функцию, которая считает сколько раз каждая из букв
    встречается в строке, разложить буквы в словарь парами
    {буква:количество упоминаний в строке}
    """
    sep_string = list(input_str)
    output_dict = {}
    for key_word in sep_string:
        value_quantity = sep_string.count(key_word)
        output_dict[key_word] = value_quantity

    return output_dict


print(count_symbols('cfkhdrkjgsjbldgs'))


def mix_strings(str1, str2):
    """
    Дописать функцию, которая будет принимать 2 строки и вставлять вторую
    в середину первой
    """
    result_str = f'{str1.split()[0]} {str2} {str1.split()[1]}'
    return result_str


print(mix_strings('Fryderyk Chopin', 'Franciszek'))


def even_int_generator():
    """
    Сгенерировать список из диапазона чисел от 0 до 100 и записать
    в результирующий список только четные числа.
    """
    even_int_list = [x for x in range(100) if not x % 2]
    return even_int_list


print(even_int_generator())
