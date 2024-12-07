use std::io;

fn main() {

  let file_contents = fs::read_to_string("./input.txt").expect("Unable to read file!");
  let mut result: i32 = 0;

  for line in file_contents.lines() {
    let game_id: String;
    let game_id_split =  line.split(':').collect();
    
    match game_id_split.first() {
      Some(value) => {
        game_id = value[&3..].to_string().clone();
      },
      _ => panic!("Input line has no game id!");
    }

    let draws = game_id_split.last().split(';');

    for draw in draws.into_iter() {
      
    }
  }
}
