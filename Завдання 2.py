import random


def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    """Генерує набір унікальних випадкових чисел для лотереї."""
    if min < 1 or max > 1000 or quantity <= 0 or quantity > (max - min + 1):
        return []
    return sorted(random.sample(range(min, max + 1), quantity))


if __name__ == "__main__":
    print("Ваші лотерейні числа:", get_numbers_ticket(1, 49, 6))
