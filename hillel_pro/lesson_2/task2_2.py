subscribers = []


def subscribe(name: str):
    subscribers.append(name)

    def confirm_subscription():
        print(f"Підписка підтверджена для {name}")
    return confirm_subscription()


def unsubscribe(name):
    if name in subscribers:
        subscribers.remove(name)
        return f'{name} успішно відписаний'


subscribe("Олена")
subscribe("Ігор")
print(subscribers)  # ['Олена', 'Ігор']
print(unsubscribe("Ігор"))  # 'Ігор успішно відписаний'
print(subscribers)  # ['Олена']



