def sun_angle(time):
    '''Функция возвращает угол солнца по времени'''
    current_time = time.split(':')
    hours = int(current_time[0])
    minutes = int(current_time[1])
    current_minutes = hours * 60 + minutes
    degree = 180 / 720
    if current_minutes < 360 or current_minutes > 1080:
        answer = 'I don\'t see the sun!'
    else:
        answer = degree * (current_minutes - 360)
    
    return answer

print(sun_angle('07:00'))