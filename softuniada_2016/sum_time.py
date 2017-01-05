import re
pattern = r'(?P<hour>\d+::|^)(?P<minutes>\d+):(?P<seconds>\d+)'
interval_a = input()
interval_b = input()

first_interval_match = re.fullmatch(pattern, interval_a)
hour_str = first_interval_match.group('hour')
if hour_str:
    hour_str = hour_str[:hour_str.index(':')]
first_hours = int(hour_str or '0')
first_minutes = int(first_interval_match.group('minutes'))
first_seconds = int(first_interval_match.group('seconds'))

second_interval_match = re.fullmatch(pattern, interval_b)
hour_str = second_interval_match.group('hour')
if hour_str:
    hour_str = hour_str[:hour_str.index(':')]
second_hours = int(hour_str or '0')
second_minutes = int(second_interval_match.group('minutes'))
second_seconds = int(second_interval_match.group('seconds'))

overall_seconds = first_seconds + second_seconds
if overall_seconds >= 60:
    overall_seconds -= 60
    second_minutes += 1

overall_minutes = first_minutes + second_minutes
if overall_minutes >= 24:
    overall_minutes -= 24
    second_hours += 1

overall_hours = first_hours + second_hours

add_second_zero = False
if overall_seconds < 10:
    add_second_zero = True
display_seconds = str(overall_seconds)
if add_second_zero:
    display_seconds = '0' + display_seconds


if overall_hours:
    print('{d}::{h}:{m}'.format(d=str(overall_hours), h=str(overall_minutes), m=display_seconds))
else:
    print('{h}:{m}'.format(h=str(overall_minutes), m=display_seconds))

