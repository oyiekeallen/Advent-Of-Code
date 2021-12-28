import re

def read_file(file_name= './input.txt'):
    return open(file_name, 'r')

def validate_passport_data(data):
    passport = {
            'byr': None,
            'iyr': None,
            'eyr': None,
            'hgt': None,
            'hcl': None,
            'ecl': None,
            'pid': None,
            'cid': None,
            }

    data = data.split(" ")
    for item in data:
        items = item.split(":")
        
        if len(items) > 1  and items[0].strip().lower() in passport.keys() :
            passport[items[0].strip().lower()] = items[1]

    passport.pop('cid')

    if None not in passport.values():
        return True
    
    return False

def count_valid_passports():
    records = read_file().read()
    records = records.split('\n\n')
    valid_count= 0
    for record in records:
        record = record.replace('\n',' ')
        if validate_passport_data(record):
            valid_count +=1

    print("Has %d valid records" % (valid_count))

if __name__ == '__main__':
    count_valid_passports() 
