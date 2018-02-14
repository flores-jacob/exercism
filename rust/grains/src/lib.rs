// Answer adapted from my python solution

pub fn square(s: u32) -> u64 {
    if (s < 1) || (s > 64) {
        panic!("Square must be between 1 and 64");
    }

    let mut square_val = 1;
    for _i in 2..s + 1 {
        square_val *= 2
    }
    return square_val
}

pub fn total() -> u64 {
    let mut total_grains = 0;

    for i in 1..65 {
        total_grains += square(i)
    }
    return total_grains;
}
