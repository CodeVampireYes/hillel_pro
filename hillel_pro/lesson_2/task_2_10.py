def create_product(name: str, price: float, quantity: int):
    product = {
        'name': name,
        'price': price,
        'quantity': quantity
    }

    def update_price(new_price: float) -> str:
        product['price'] = new_price
        return f"Ціну '{product['name']}' було оновлено до {product['price']}."

    def get_product_info() -> dict:
        return product

    return update_price, get_product_info


update_price, get_product_info = create_product("Laptop", 1500.00, 5)

print(get_product_info())
print(update_price(1400.00))
print(get_product_info())
