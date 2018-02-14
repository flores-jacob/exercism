pub fn square(s: u32) -> u64 {
//    if (s < 1) || (s > 64):
//        raise ValueError("input square should be between 1 and 64");

    let mut square_val = 1;
    for i in 2..s + 1 {
        square_val *= 2
    }
    return square_val
}

pub fn total() -> u64 {
    unimplemented!();
}
