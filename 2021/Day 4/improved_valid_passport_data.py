import re

def read_file(file_name= './input.txt'):
    return open(file_name, 'r')

def validate_byr(byr):
    if len(byr) != 4:
        return False

    if int(byr) >= 1920 and int(byr) <= 2002:
        return True

    return False

def validate_iyr(iyr):
    if len(iyr) != 4:
        return False

    if int(iyr) >= 2010 and int(iyr) <= 2020:
        return True
    
    return False

def validate_eyr(eyr):
    if len(eyr) != 4:
        return False
    if int(eyr) >= 2020 and int(eyr) <= 2030:
        return True

    return False

def validate_hgt(hgt):
    match =re.match('^[0-9]{2,3}[in|cm]+$', hgt)
    if match :
        mathes = re.split('(\d+)', match.string)
        delimiter = match.string[-2:]
        if delimiter.lower() == 'cm':
            if int(match.string[:-2]) >= 150 and  int(match.string[:-2]) <= 193:
                return True
        if delimiter.lower() == 'in':
            if int(match.string[:-2]) >= 59 and  int(match.string[:-2]) <= 76:
                return True 
    return False

def validate_hcl(hcl):
    if re.match('^#[0-9a-f]{6}$', hcl):
        return True
    return False

def validate_ecl(ecl):
    if ecl.lower() in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return True
    return False

def validate_pid(pid):
    if re.match('^[0-9]{9}$', pid):
        return True
    return False

def validate_entry(entry):
    if entry[0].lower() == 'byr':
        return validate_byr(entry[-1])
    
    if entry[0].lower() == 'iyr':
        return validate_iyr(entry[-1])
    
    if entry[0].lower() == 'eyr':
        return validate_eyr(entry[-1])
    
    if entry[0].lower() == 'hgt':
        return validate_hgt(entry[-1])
    
    if entry[0].lower() == 'hcl':
        return validate_hcl(entry[-1])
    
    if entry[0].lower() == 'ecl':
        return validate_ecl(entry[-1])

    if entry[0].lower() == 'pid':
        return validate_pid(entry[-1])

    return True
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
            if validate_entry(items):
                passport[items[0].strip().lower()] = items[-1]
    passport.pop('cid')
    if None not in passport.values():
        print(" Passport Data " + str(passport))
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
