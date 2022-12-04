use std::fs::File;
use std::io::{self, BufRead, BufReader};

fn main() -> io::Result<()>  {
    let file = File::open("./input.txt")?;
    let reader = BufReader::new(file);
    let mut final_result: u32 = 0;

    for line in reader.lines() {
        if let Ok(line_value) = line {

            let mut plays_iter = line_value.split_whitespace();
            let opponent_play = plays_iter.next().unwrap();
            let my_play = plays_iter.next().unwrap();
            println!("My play {} , opponent play {}", my_play, opponent_play);

            let my_round_result = calculate_round_results(opponent_play, my_play);
            println!("Round Result {}", my_round_result);

            final_result = final_result + my_round_result;
        }
    }

    println!("Final Result {}", final_result);
    Ok(())
}

fn calculate_round_results(opponent_move: &str, my_move: &str) -> u32 {
    if opponent_move == "A" && my_move == "X" || opponent_move == "B" && my_move == "Y" || opponent_move == "C" && my_move == "Z" {
        println!("Round draw, play score {} ", get_play_score(my_move));
        return get_play_score(my_move) + 3;
    }

    if is_my_winning_move(opponent_move, my_move) {
        println!("I won the round! play score {}", get_play_score(my_move) );
        return get_play_score(my_move) + 6;
    }
    println!("Lost round! : play score {}", get_play_score(my_move));
    return get_play_score(my_move);

}

fn get_play_score(play: &str) -> u32 {
    if play == "X" || play == "A" {
        return 1;
    }
    else if play == "Y" || play == "B" {
        return 2;
    }
    else if play == "Z" || play == "C" {
        return 3;
    }
    else
    {
        panic!("Unrecognized play!");
    }
}

fn is_my_winning_move(opponent_move: &str, my_move: &str) -> bool {
    return (opponent_move == "A" && my_move == "Y") || (opponent_move == "C" && my_move == "X") || (opponent_move == "B" && my_move == "Z")
}