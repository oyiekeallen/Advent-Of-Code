use utils::read_file;
use std::io::ErrorKind;

#[test]
    fn it_works() {
        let result = read_file("Cargo.toml");
        assert_eq!(result.is_ok(), true);
    }

    #[test]
    fn it_fails() {
        let result = read_file("");
        assert_eq!(result.is_err_and(|x| x.kind() == ErrorKind::NotFound), true);
    }
