def validate_password(password):
    # :( как сделать так,чтобы "причины ошибок" отображались в одном списке,когда их 2 и 3, а не вот это вот всё...
    invalid_password = list()
    if not _validate_symbols(password):
        invalid_password.append('Содержит запрещенные символы')
        return invalid_password
    if _validate_letters_even(password):
        invalid_password.append('Содержит нечётное количество букв')
        return invalid_password
    if _validate_numbers_odd(password):
        invalid_password.append('Содержит чётное количество цифр')
        return invalid_password
    return True


def _validate_symbols(input_str):
    for symbol in input_str:
        if symbol.isalpha() or symbol.isdigit():
            continue
        return False
    return True


def _validate_letters_even(input_str):
    symbol_letter_str = (''.join(symbol for symbol in input_str if symbol.isalpha()))
    if len(symbol_letter_str) % 2:
        return True
    return False


def _validate_numbers_odd(input_str):
    symbol_number_str = (''.join(symbol for symbol in input_str if symbol.isdigit()))
    if not len(symbol_number_str) % 2:
        return True
    return False


password = 'Qwer5q1use684'
result = validate_password(password)
print(result)
