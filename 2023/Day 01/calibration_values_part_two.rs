use std::fs;
use std::collections::BTreeMap;

fn main() {

  let file_contents = fs::read_to_string("./input.txt").expect("Unable to read file!");
  let mut sum = 0;
  let possible_values: Vec<&str> = vec!["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"];

  for line in file_contents.lines() {
    sum += get_numbers(&line.to_lowercase(), &possible_values);
    print!("Current total: {sum}\n");
  }

  print!("{sum}");
}

fn get_numbers(input: &str, possible_values: &Vec<&str>) -> i32 {
  let mut numbers: BTreeMap<i32, String> = BTreeMap::new();

  println!("\nInput : {input}");
  for (key, value) in possible_values.into_iter().enumerate() {
    let value_found = input.find(value);

    match value_found {
      Some(i) => {
        println!("Match found for {value} at position {i}");
        numbers.insert(i as i32, key.to_string());
      },
      _ => (),
    }
  }

  for (key, character) in input.chars().enumerate() {
    if character.is_digit(10) {
      println!("Match found for {character} at position {key}");
      let character_str : String =  character.to_string();
      numbers.insert(key as i32, character_str);
    }
  }

  print!("Retrieved numbers: ");
  for (key, value) in &numbers {
    print!("value:{value} at position:{key}\t");
  }
  println!("");

  let mut result = String::from("");
  let Some((_, first_value)) = numbers.pop_first() else { panic!("No first in map!")};
  result.push_str(&first_value);

  let last_value: String;
  match numbers.pop_last() {
    Some((_, value)) => {
      last_value = value;
    },
    None => {
      println!("Last value absent!");
      last_value = first_value.clone();
    }
  }
  result.push_str(&last_value);

  println!("Result: {result}");
  return result.parse::<i32>().unwrap()
}