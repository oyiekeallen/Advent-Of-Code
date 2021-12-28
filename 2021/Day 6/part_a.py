def read_file(file_name='./input.txt'):
    return open(file_name, 'r')


def preprocess_input(data):
    return data.read().split('\n\n')

def count_answers(data):
    answers_count= 0
    for item in data:
        item = item.replace('\n', ' ')
        group_answers = len(set(''.join(item).replace(' ', '')))
        answers_count += group_answers

    print('Answers count is %d' % (answers_count))
if __name__ == '__main__':
    count_answers(preprocess_input(read_file()))

