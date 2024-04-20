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


# Тесты

# 1
n_atm = 5
k_atm = 1
L = [100, 30, 20, 80]

print(f"Количество существующих банкоматов - {n_atm}")
print(f"Количество банкоматов, которые хотят добавить - {k_atm}")
print(f"Расстояние между банкоматами:\n{L}")
print(f"Новое расстояние между банкоматам:\n{new_distance(n_atm, k_atm, L)}\n")
print(L == [50.0, 50.0, 30, 20, 80])
print()

# 2
n_atm = 5
k_atm = 3
L = [100, 30, 20, 30]

print(f"Количество существующих банкоматов - {n_atm}")
print(f"Количество банкоматов, которые хотят добавить - {k_atm}")
print(f"Расстояние между банкоматами:\n{L}")

print(f"Новое расстояние между банками:\n{new_distance(n_atm, k_atm, L)}\n")
print(L == [25, 25, 25, 25, 30, 20, 30])
print()

# 3
n_atm = 5
k_atm = 10
L = [1000, 30, 20, 30]

print(f"Количество существующих банкоматов - {n_atm}")
print(f"Количество банкоматов, которые хотят добавить - {k_atm}")
print(f"Расстояние между банкоматами:\n{L}")

print(f"Новое расстояние между банками:\n{new_distance(n_atm, k_atm, L)}\n")
print(L == [90.91, 90.91, 90.91, 90.91, 90.91, 90.91, 90.91, 90.91, 90.91,
            90.91, 90.91, 30, 20, 30])
print()

# 4
n_atm = 2
k_atm = 3
L = [50]

print(f"Количество существующих банкоматов - {n_atm}")
print(f"Количество банкоматов, которые хотят добавить - {k_atm}")
print(f"Расстояние между банкоматами:\n{L}")

print(f"Новое расстояние между банками:\n{new_distance(n_atm, k_atm, L)}\n")
print(L == [12.5, 12.5, 12.5, 12.5])
print()

# 5
n_atm = 3
k_atm = 2
L = [50, 50]

print(f"Количество существующих банкоматов - {n_atm}")
print(f"Количество банкоматов, которые хотят добавить - {k_atm}")
print(f"Расстояние между банкоматами:\n{L}")

print(f"Новое расстояние между банками:\n{new_distance(n_atm, k_atm, L)}\n")
print(L == [25.0, 25.0, 25.0, 25.0])
print()
