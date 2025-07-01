def add_time(start, duration, day=''):
    new_time = ''
    extra_days = 0
    days = ['SUNDAY', 'MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY']

    start_time = start.split(' ')[0]
    ampm = start.split(' ')[1]

    start_time_hr = int(start_time.split(':')[0])
    start_time_min = int(start_time.split(':')[1])

    duration_hr = int(duration.split(':')[0])
    duration_min = int(duration.split(':')[1])

    new_time_hr = start_time_hr + duration_hr
    new_time_min = start_time_min + duration_min

    if new_time_min >= 60:
        new_time_hr += 1
        new_time_min -= 60
    
    while new_time_hr > 24:
        new_time_hr -= 24
        extra_days += 1
    
    if new_time_hr >= 12 and new_time_hr > start_time_hr:
        if ampm == 'PM':
            if new_time_hr > 12:
                new_time_hr -= 12
            ampm = 'AM'
            extra_days += 1
        else:
            if new_time_hr > 12:
                new_time_hr -= 12
            ampm = 'PM'
 
    new_time = f"{new_time_hr}:{new_time_min:02}"

    new_time += ' ' + ampm

    if day > '':
        day = day[0].upper() + day[1:].lower()
        new_time += ', ' + day

    if extra_days == 1:
        new_time += ' (next day)'
    elif extra_days > 1:
        new_time += f' ({extra_days} days later)'
    print(new_time)
    return new_time

add_time('3:30 PM', '2:12')
add_time('11:55 AM', '3:12')
add_time('2:59 AM', '24:00')
add_time('11:59 PM', '24:05')
add_time('8:16 PM', '466:02')
add_time('8:16 PM', '0:00')
add_time('3:30 PM', '2:12', 'Monday')
add_time('2:59 AM', '24:00', 'saturDay')