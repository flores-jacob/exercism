pub fn is_leap_year(year: i32) -> bool {
    // Solution is adapted from my earlier python interpretation
    (year % 4 == 0) && (! (year % 100 == 0) | (year % 400 == 0))
}
