def read_file(file_name='input.txt'):
    file_data = open(file_name, 'r')
    return file_data

def is_tree_in_path(line, position ,repeat_sequence):
    line = line.strip()
    unique = len(line)

    if position > 0:
        if line[(position % unique)] == '#':
            return True
    return False

def count_trees(path, column_offset, row_offset):
    trees_count= 0
    position = 0 
    rows_covered = 1
    for line in path:
        repeat_sequence = len(line)
        rows_covered +=1
        if position == 0:
            position = column_offset
            continue
        
        if rows_covered  % row_offset == 0 and int(row_offset) != 1 :
            continue
        
        if is_tree_in_path(line, position, repeat_sequence ):
            trees_count += 1 
        
        position += column_offset
    print("Trees encountered = " + str(trees_count))

    return trees_count

if __name__ == '__main__':
    
    slopes = [[1,1], [3,1],[5,1],[7,1],[1,2]]
    answer = 1
    for values in slopes:
        result = count_trees(read_file(),values[0], values[1]) 
        if result > 0 : answer *=result 

    print("Result is %d "% (answer) )
