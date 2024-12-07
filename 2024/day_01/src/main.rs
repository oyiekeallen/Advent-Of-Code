use utils::read_file_lines;

use std::collections::{BinaryHeap, HashMap};
use std::cmp::Reverse;

fn main() {

    println!("Part A result is {} and Part B result is {}", part_a(), part_b())
}

pub fn part_a() -> String
{
    let mut first_col = BinaryHeap::new();
    let mut last_col = BinaryHeap::new();

    if let Ok(lines) = read_file_lines("./src/input.txt") {
        for line in lines.flatten() {
            let line_split = line.split_whitespace().collect::<Vec<_>>();

            if line_split.len()!= 2 {
                break;
            }

            first_col.push(Reverse(line_split[0].parse::<i64>().unwrap()));
            last_col.push(Reverse(line_split[1].parse::<i64>().unwrap()));
        }
    }

    let mut sum: i64 = 0;
    while !first_col.is_empty() || !last_col.is_empty() {
        sum += (first_col.pop().unwrap().0 - last_col.pop().unwrap().0).abs();
    }
  
    return format!("Result is {}", sum);
}

pub fn part_b() -> String
{
    let mut id_count : HashMap<i64, i64> = HashMap::new();
    let mut ids: Vec<i64> = Vec::new();

    if let Ok(lines) = read_file_lines("./src/input.txt") {
        for line in lines.flatten() {
            let line_split = line.split_whitespace().collect::<Vec<_>>();

            if line_split.len()!= 2 {
                break;
            }

            ids.push(line_split[0].parse::<i64>().unwrap());
            let id = line_split[1].parse::<i64>().unwrap();

            if id_count.contains_key(&id)
            {
                id_count.insert(id, id_count.get(&id).unwrap() + 1);
            }
            else
            {
                id_count.insert(id, 1);
            }
        }
    }

    let mut result: i64 = 0;
    
    for id in ids{
        match id_count.get(&id)
        {
            Some(count) => 
            {
                result += id * count;
            },
            _ => continue,
        }
    } 

    return format!("Result is {}", result);
}
