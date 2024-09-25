discount = 0.1
additional_discount = 0.05


def create_order(price: float | int, additional_discount_allowed: bool = False) -> str:
    start_price = price

    def apply_additional_discount():
        nonlocal price
        price *= 1 - additional_discount

    price *= 1 - discount

    if additional_discount_allowed:
        apply_additional_discount()

    return f'Початкова ціна: {start_price}, кінцева ціна зі знижкою 10%: {price}'


print(create_order(1000))  # Початкова ціна: 1000, кінцева ціна зі знижкою 10%: 900
print(create_order(1000, True))  # Початкова ціна: 1000, кінцева ціна зі знижкою 10%: 855
