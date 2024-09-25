events = []


def event_calendar():
    def add_event(event):
        events.append(event)
        print(f"Подію '{event}' додано.")

    def remove_event(event):
        if event in events:
            events.remove(event)
            print(f"Подію '{event}' видалено.")
        else:
            print(f"Події '{event}' немає в списку.")

    def view_events():
        count = 1
        for event in events:
            if len(events) >= 1:
                print(f'{count}: {event}')
                count += 1
            else:
                print('"Немає запланованих подій."')
    return add_event, remove_event, view_events


add_event, remove_event, view_events = event_calendar()

add_event("Зустріч з клієнтом о 10:00")
add_event("Лекція в hillel о 15:00")
view_events()
remove_event("Зустріч з клієнтом о 10:00")
view_events()



