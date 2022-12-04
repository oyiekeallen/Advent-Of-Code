use std::fs::File;
use std::io::{self, BufRead, BufReader};

fn main() -> io::Result<()>  {
    
    let file = File::open("./input.txt")?;
    let reader = BufReader::new(file);
    let mut largest_cargo : u32 = u32::MIN;
    let mut cargo_sum: u32 = 0;
    let mut cargo_sizes = Vec::new();

    for line in reader.lines() {

        if let Ok(ip) = line {
            if ip.is_empty() {
                if cargo_sum > largest_cargo {
                    largest_cargo = cargo_sum;
                } 

                cargo_sizes.push(cargo_sum);

                cargo_sum = 0;
                continue;
            }

            cargo_sum = cargo_sum + ip.parse::<u32>().unwrap();
        }
    }

    println!("Largest Cargo {}", largest_cargo);

    cargo_sizes.sort();

    if cargo_sizes.is_empty() {
        return Ok(())
    }

    println!("Top 3 Cargo sum : {} ", cargo_sizes.pop().unwrap()  + cargo_sizes.pop().unwrap() +  cargo_sizes.pop().unwrap());

    Ok(())
}