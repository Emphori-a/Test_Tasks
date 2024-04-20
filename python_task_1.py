"""Перевести особенный номер в хороший номер."""
import re


def get_bad_num(text: str) -> list[str] | str:
    """Функция, выбирающая все особенные номера из текста."""
    # паттерн для поиска особенных номеров в тексте
    regex = r'(?:^|\s)(\d{2,4}\\\d{2,5})(?:\s|$|.)'

    bad_num = re.findall(regex, text)
    return bad_num if bad_num else 'В тексте нет особенных номеров.'


def get_good_num(bad_num: list[str]) -> list[str]:
    """Функция, для перевода особенного номера в хороший номер."""
    result = []
    for num in bad_num:
        first_part, second_part = num.split('\\')
        result.append(f'{first_part.zfill(4)}\\{second_part.zfill(5)}')
    return result


if __name__ == '__main__':
    input_string: str = 'Адрес 5467\\456. Номер 405\\549'  # input()
    bad_num: list[str] | str = get_bad_num(input_string)

    if isinstance(bad_num, list):
        print(*get_good_num(bad_num), sep='\n')
