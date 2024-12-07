use std::fs::File;
use std::io::{self, BufRead, Error};

pub fn read_file_lines(filename: &str) -> Result<io::Lines<io::BufReader<File>>, Error> {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}
