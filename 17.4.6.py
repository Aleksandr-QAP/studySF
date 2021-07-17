def is_empty(): # очередь пуста?
    # да, если указатели совпадают и в них содержится ноль
    return head == tail and queue[head] == 0