def checker(line):
    if '[CRITICAL]' in line or '[WARNING]' in line or '[ERROR]' in line:
        try:
            line = line.strip()
            line = line.split(' ')
            time = line[0]
            error = line[2:]
            if len(time) < 7:
                return f'Error! Incorrect time in {line}'
            fin_line = f"{time} | {' '.join(error)}"
            return(fin_line)
        except IndexError:
            return f'Invalid string in {line}'
fin_log = []



with open('log.txt','r') as log:
    for line in log:
        fin_line = checker(line)
        if fin_line is not None:
            fin_log.append(fin_line)
print('============Отчет об авариях и крит. предупреждениях============')
print()
for row in fin_log:
    print(row)