"""Расстояния между банкоматами."""


def new_distance(k_atm: int, distances: list[int]) -> list[float]:
    """Функция для вычисления нового расстояния между банкоматами"""

    distances_len = len(distances)
    new_atm_in_idx = {idx: 1 for idx in range(distances_len)}

    while k_atm > 0:
        max_distance = 0
        idx_max_distance = 0

        for idx in range(distances_len):
            if distances[idx] / new_atm_in_idx[idx] > max_distance:
                max_distance = distances[idx] / new_atm_in_idx[idx]
                idx_max_distance = idx
        new_atm_in_idx[idx_max_distance] += 1
        k_atm -= 1

    new_distances = [round(dist / new_atm_in_idx[idx], 2)
                     for idx, dist in enumerate(distances)
                     for _ in range(new_atm_in_idx[idx])]

    return new_distances


if __name__ == '__main__':
    n: int = 5  # int(input())
    k: int = 3  # int(input())
    distances: list[int] = [100, 30, 20, 80]  # list(map(int, input(),split()))
    print('Новое расстояние между банкоматами:\n'
          f'{new_distance(k, distances)}')
