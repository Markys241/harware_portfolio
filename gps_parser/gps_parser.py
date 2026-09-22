def line_creator(line):
    if '$GPRMC' in line:
        try:
            line = line.strip()
            line = line.split(',')
            raw_time = line[1]
            lat = line[3]
            lon = line[5]
            if len(raw_time) < 6:
                return None
            time = f'{raw_time[0:2]}:{raw_time[2:4]}:{raw_time[4:6]}'
            fin_line = {'time': time,
                        'lat': lat,
                        'lon': lon}
            return(fin_line)
        except IndexError:
            return 'Invalid string'

error_counter = 0
all_cords = []
with open('cords.txt', 'r') as cords:
    for line in cords:
        result = line_creator(line)
        if result == 'Invalid string':
            error_counter += 1 
        elif result is not None:
            all_cords.append(result) 

            


print('=======================Лог координат=======================')
for item in all_cords:
    print(item)
print()
print(f'Некорректных строк в логе:{error_counter}')