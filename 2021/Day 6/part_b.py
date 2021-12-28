def read_file(file_name='./input.txt'):
    return open(file_name, 'r')


def preprocess_input(data):
    return data.read().split('\n\n')

def count_answers(data):
    answers_count= 0
    for item in data:
        item = item.replace('\n', ' ')
        
        group_answers_arr = item.strip().split(' ')
        common_ans = ''.join(sorted(group_answers_arr[0]))
        common_ans =  common_ans.lower()
        for i_ans in group_answers_arr:
            tmp = ''.join(sorted(i_ans)).lower()
            common_ans = set(common_ans).intersection(set(tmp))

        answers_count += len(common_ans)

    print('Answers count is %d' % (answers_count))
if __name__ == '__main__':
    count_answers(preprocess_input(read_file()))

