def add_time(start, duration, day=''):
    
    #Variables declairation and initiation
    new_time = ''
    extra_days = 0
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

    #Splitting start time between time and am/pm
    start_time = start.split(' ')[0]
    ampm = start.split(' ')[1]

    #Splittng start time between hour and minute
    start_time_hr = int(start_time.split(':')[0])
    start_time_min = int(start_time.split(':')[1])

    #Splittng duration between hour and minute
    duration_hr = int(duration.split(':')[0])
    duration_min = int(duration.split(':')[1])

    #Adding hours from start time and duration
    new_time_hr = start_time_hr + duration_hr
    #Adding minutes from start time and duration
    new_time_min = start_time_min + duration_min

    #Adding extra 1 hour if minutes greater than 60
    if new_time_min >= 60:
        new_time_hr += 1
        new_time_min -= 60
    
    #While loop to calculate extra days
    while new_time_hr > 24:
        new_time_hr -= 24
        extra_days += 1
    
    #Logic to change am to pm and pm to am if required
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
 
    #Assigning formatted final values for hours, minutes and am/pm
    new_time = f"{new_time_hr}:{new_time_min:02} {ampm}"

    #If day argument is passed, calculating correct day
    if day > '':
        day = day[0].upper() + day[1:].lower()
        day_index = (days.index(day) + (extra_days % 7)) % 7
        new_time += ', ' + days[day_index]

    #Logic for extra days part
    if extra_days == 1:
        new_time += ' (next day)'
    elif extra_days > 1:
        new_time += f' ({extra_days} days later)'

    #Printing new time
    print(new_time)

    #Returning new time value
    return new_time

#Test case values
add_time('3:30 PM', '2:12')
add_time('11:55 AM', '3:12')
add_time('2:59 AM', '24:00')
add_time('11:59 PM', '24:05')
add_time('8:16 PM', '466:02')
add_time('8:16 PM', '0:00')
add_time('3:30 PM', '2:12', 'Monday')
add_time('2:59 AM', '24:00', 'saturDay')
add_time('11:59 PM', '24:05', 'Wednesday')
add_time('8:16 PM', '466:02', 'tuesday')