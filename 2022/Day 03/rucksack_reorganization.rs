use std::collections::{HashMap, HashSet};
use std::fs::File;
use std::io::{self, BufRead, BufReader};

fn main() -> io::Result<()>  {
    let file = File::open("./input.txt")?;
    let reader = BufReader::new(file);
    let mut final_result: u32 = 0;

    let mut letter_key: HashMap<&str, u32>  = HashMap::new();
    let mut counter: u32 = 0;
    for letter in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ".chars() {
        counter +=1;
        letter_key.insert(&letter.to_string(), counter);
    }


    for line in reader.lines() {
        if let Ok(line_value) = line {

            let (left_half, right_half) = line_value.split_at(line_value.len()/2);
            let left_half_set = HashSet::new();
            left_half_set.insert(left_half);
            mix deps.get
            let right_half_set = HashSet::new();
            right_half_set.insert(right_half);


            let mut common_items = left_half_set.intersection(&right_half_set);

            for item in common_items {
                match letter_key.get(&item) {
                    Some(priority) => {
                        final_result += priority;
                    }
                    None => {
                        panic!("Error retrieving value for {}", item);
                    }
                }
            }

        }
    }

    println!("Final Result {}", final_result);
    Ok(())
}