def get_angle(hours=12, minutes=00):
    if hours >= 12:
        if hours == 24:
            hours = 0
        else:
            hours -= 12

    angle = 30 * hours + 0.5 * minutes - 6 * minutes
    if angle > 0:
        return angle
    else:
        return -angle

hours = float(input('Введите количество часов '))
minutes = float(input('Введите количество минут '))
print(get_angle(hours, minutes))