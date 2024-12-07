use std::fs;
use std::io;

fn main() {

  let file_contents = fs::read_to_string("./input.txt").expect("Unable to read file!");
  let mut sum = 0;

  for line in file_contents.lines() {
    let mut ints_in_string = String::from("");

    for character in line.chars() {
      if character.is_digit(10) {
        ints_in_string.push(character);
      }
    }

    let mut value: String = (&ints_in_string[..1]).to_string();
    value.push_str(&ints_in_string[ints_in_string.len()-1..]);

    let calibration_value = value.to_string().parse::<i32>().unwrap();
    sum += calibration_value;
  }

  println!("{sum}");

}