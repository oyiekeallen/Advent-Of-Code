

def read_file(file_name='input.txt'):
    file_data = open(file_name, 'r')
    return file_data

def count_trees(path):
    tree_count= 0
    position = 0
    for line in path:
        line = line.strip()
        unique = len(line)
        if position == 0:
            position = 3
            continue
        if position > 0:
            if line[(position % unique)] == '#':
                tree_count += 1
            position += 3

    print("Trees encountered = " + str(tree_count))


if __name__ == '__main__':
    count_trees(read_file())
