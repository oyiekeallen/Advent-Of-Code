def get_values(file_name="./input.txt"):
    values = []
    file_data = open(file_name, 'r')
    
    for line in file_data:
        line = line.strip()
        if int(line) < 2020:
            values.append(line)

    return list(set(values))

if __name__ == '__main__':
    values = get_values()

    for idx,value in enumerate(values):
        for idx_i, value_i in enumerate(values):
            for idx_j, value_j in enumerate(values):
                total = int(value) + int(value_i) + int(value_j)
                if total == 2020:
                    print('The values are %d, %d, %d and result is %d', value, value_i, value_j, (int(value) * int(value_i) * int(value_j)))
