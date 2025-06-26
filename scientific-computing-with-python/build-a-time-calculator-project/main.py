def add_time(start, duration):
    new_time = ''
    extra_days = 0

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

    while new_time_hr >= 12:
        if new_time_hr >= 24:
            new_time_hr -= 24
            extra_days += 1
            if new_time_hr > 24:
                pass
        
        if new_time_hr >= 12 and new_time_hr > start_time_hr:
            if ampm == 'AM':
                ampm = 'PM'
            else:
                ampm = 'AM'
                extra_days += 1
            new_time_hr -= 12
 
    new_time = f"{new_time_hr}:{new_time_min:02}"

    new_time += ' ' + ampm
    if extra_days == 1:
        new_time += ' (next day)'
    elif extra_days > 1:
        new_time += f' ({extra_days} days later)'
    print(new_time)
    return new_time

add_time('2:59 AM', '24:00')