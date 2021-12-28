import re

def read_policy(file_name='./input.txt'):
    file_data = open(file_name, 'r')
    valid_policy_count = 0
    for line in file_data:
        line = line.strip()

        if policy_valid(line):
            valid_policy_count += 1

    print("Valid policies : " + str(valid_policy_count) )
def policy_valid(policy):
    policy_data = re.split("\s", policy)
    lower_limit, upper_limit = re.split('-' ,policy_data[0])
    
    occurence = policy_data[-1].count(policy_data[1][0])
    if occurence >= int(lower_limit) and occurence <= int(upper_limit):
        return True
    
    return False
if __name__ == '__main__':
    read_policy()
