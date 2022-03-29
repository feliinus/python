print('task #1')
'''
реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах
до минуты: <s> сек;
до часа: <m> мин <s> сек;
до суток: <h> час <m> мин <s> сек;
'''
# 1 минута
one_minute = 60
# 1 час
one_hour = 3600
# 1 день
one_day = 86400

duration = int(input('Ввести время в секундах: '))

# вывод информации до минуты:
if duration < one_minute:
    print('{} сек'.format(duration))

# вывод информации до часа:
elif one_minute <= duration < one_hour:
    my_minute = duration // one_minute
    my_second = duration % one_minute
    print('{} мин {} сек'.format(my_minute, my_second))
    # вывод информации до суток:
elif one_hour <= duration < one_day:
    my_hour = duration // one_hour
    duration = duration % one_hour
    my_minute = duration // one_minute
    my_second = duration % one_minute
    print ('{} час {} мин {} сек'.format(my_hour,my_minute,my_second));
