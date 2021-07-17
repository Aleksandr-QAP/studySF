def size(): # получаем размер очереди
    if is_empty(): # если она пуста
        return 0 # возвращаем ноль
    elif head == tail: # иначе, если очередь не пуста, но указатели совпадают
        return N_max # значит очередь заполнена
    elif head > tail: # если хвост очереди сместился в начало списка
        return N_max - head + tail
    else: # или если хвост стоит правее начала
        return tail - head