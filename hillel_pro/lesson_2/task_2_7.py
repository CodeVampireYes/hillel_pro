total_expense = 0


def add_expense(expense):
    global total_expense
    total_expense += expense
    return total_expense


run = True
while run:
    try:
        input_expense = float(input('Введіть суму витрат:'))
        print(f'Загальна сума витрат: {add_expense(input_expense)} \n ---Для виходу натисніть будь-яку букву---')
    except ValueError:
        print('До наступної зустрічі')
        run = False

