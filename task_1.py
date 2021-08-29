
duration = int(input("Введите целое число в секундах: "))
day = duration // 86400
hour = duration // 3600 % 24
minute = duration // 60 % 60
seconds = duration % 60
if day % 10 == 1 and day % 100 != 11:
    print(day, 'день', end=" ")
elif 1 < day % 10 < 5 and not 11 < day % 100 < 15:
    print(day, 'дня', end=" ")
else:
    print(day, 'дней', end=" ")
if hour % 10 == 1 and hour % 100 != 11:
    print(hour, 'час', end=" ")
elif 1 < hour % 10 < 5 and not 11 < hour % 100 < 15:
    print(hour, 'часа', end=" ")
else:
    print(hour, 'часов', end=" ")
if minute % 10 == 1 and minute % 100 != 11:
    print(minute, 'минута', end=" ")
elif 1 < minute % 10 < 5 and not 11 < minute % 100 < 15:
    print(minute, 'минуты', end=" ")
else:
    print(minute, 'минут', end=" ")
if seconds % 10 == 1 and seconds % 100 != 11:
    print('и', seconds, 'секунда', end=" ")
elif 1 < seconds % 10 < 5 and not 11 < seconds % 100 < 15:
    print('и', seconds, 'секунды', end=" ")
else:
    print('и', seconds, 'секунд', end=" ")
# не знаю пока, как просклонять покороче
# простой вариант:
# duration = int(input("Введите целое число в секундах: "))
# seconds = [duration // 86400, duration // 3600 % 24, duration // 60 % 60, duration % 60]
#
# print(f'duration = {seconds[0]} дн {seconds[1]} час {seconds[2]} мин {seconds[3]} сек')

