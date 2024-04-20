"""Конкатенация чисел."""


def max_concatenated_number(num_list: list[str]) -> str:
    """Функция вычисляющая максимальное число при конкатенации строк."""
    sorted_str_list: list[str] = sorted(
        num_list, key=lambda x: x * 3, reverse=True
    )

    max_num: str = ''.join(sorted_str_list)

    return max_num


if __name__ == '__main__':
    num_list: list[str] = ["41", "4", "005", "89"]  # input.split()
    print(max_concatenated_number(num_list))
