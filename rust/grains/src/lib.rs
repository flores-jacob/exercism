// Answer adapted from my python solution

pub fn square(s: u32) -> u64 {
    if (s < 1) || (s > 64) {
        panic!("Square must be between 1 and 64");
    }

    return 2u64.pow(s - 1)
}

pub fn total() -> u64 {
    (1..64 + 1).fold(0, |accumulator, num| accumulator + square(num))
}
