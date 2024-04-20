"""Расстояния между банкоматами."""


def new_distance(n_atm: int, k_atm: int, distances: list[int]) -> list[int]:
    """Функция для вычисления нового расстояния между банкоматами."""
    new_amount_atm: int = n_atm+k_atm-1

    for _ in range(k_atm):
        highest_distance: int = max(distances)
        index_of_highest_distance = distances.index(highest_distance)
        distances.remove(max(distances))
        if len(distances) == 0:
            for _ in range(k_atm+1):
                distances.append(round(highest_distance/(k_atm+1), 2))
            return distances
        if (highest_distance / k_atm + 1 > max(distances)/2
            and highest_distance != max(distances)*2
                and highest_distance != max(distances)):
            for _ in range(k_atm + 1):
                distances.insert((index_of_highest_distance),
                                 round(highest_distance / (k_atm+1), 2))
            return distances
        elif (highest_distance / k_atm + 1 <= max(distances)/2
              and highest_distance != max(distances)):
            distances.insert(index_of_highest_distance, highest_distance)
            distances[index_of_highest_distance] = round(
                highest_distance / k_atm, 2)
            for _ in range(k_atm - 1):
                distances.insert((index_of_highest_distance),
                                 round(highest_distance / k_atm, 2))
            k_atm -= k_atm - 1
        else:
            distances[index_of_highest_distance:index_of_highest_distance] = [
                highest_distance/2, highest_distance/2]
            k_atm -= 1
        if len(distances) == new_amount_atm:
            return distances
    return distances


if __name__ == '__main__':
    n: int = 5  # int(input())
    k: int = 3  # int(input())
    distances: list[int] = [100, 30, 20, 80]  # list(map(int, input(),split()))
    print('Новое расстояние между банкоматами:\n'
          f'{new_distance(n, k, distances)}')
