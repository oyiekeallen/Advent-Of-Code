def read_file(file_name='./input.txt'):
    return open(file_name, 'r')

def get_row(boarding_pass):
    lower_band = 0
    upper_band = 127

    for value in boarding_pass:
        if value.lower() == 'f':
            upper_band = (lower_band + upper_band ) //2
        
        if value.lower() == 'b':
            lower_band =  (lower_band +  upper_band) // 2
    return upper_band

def get_column(boarding_pass):
    lower_band = 0
    upper_band = 7

    for value in boarding_pass:
        
        if value.lower() == 'l':
            upper_band = (lower_band + upper_band ) //2
        
        if value.lower() == 'r':
            lower_band = (lower_band+upper_band) // 2

    
    return upper_band

def calculate_sid(boarding_pass):
    row= get_row(boarding_pass[:7])
    column= get_column(boarding_pass[-3:])
    return (row * 8) + column


def highest_sid():
    data = read_file()
    highest_sid = 0

    for b_pass in data:
        curr_sid =  calculate_sid(b_pass.strip())
        if curr_sid > highest_sid:
            highest_sid = curr_sid

    print('Highest SID is %d' % highest_sid)
if __name__ == '__main__':
    highest_sid()

    #print(get_column('RRR'))
    #print(get_column('LLL'))
    #print(get_column('RLL'))
    #print('%d equals %d' % (get_row('FBFBBFF'),44))
    #print('%d equals %d' % (get_row('BFFFBBF'),70))
    #print('%d equals %d' % (get_row('FFFBBBF'),14))
    #print('%d equals %d' % (get_row('BBFFBBF'),102))
