



def get_values(file_name="./input.txt"):
    values = {}
    file_data = open(file_name, 'r')
    
    for line in file_data:
        line = line.strip()
        if line in values:
            values[line]=1
        else:
            values[line] =+ 1
    return  values

if __name__ == '__main__':
    values =get_values()
    for value in values:
        complement_value = 2020 - int(value)

        if str(complement_value) in list(values.keys()):
            print('Result is %s and %s which equal %d ' %(complement_value, value,(int(complement_value) * int(value))))
            exit()
    print('No suitable anser found')
