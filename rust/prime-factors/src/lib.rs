pub fn factors(n:i64) -> Vec<i64>{

    let mut prime_factors:Vec<i64> = vec![];
    let mut candidate_factor: i64 = 2;
    let mut dividend: i64 = n;

    while candidate_factor <= dividend{
        if dividend % candidate_factor == 0 {
            prime_factors.push(candidate_factor);
            dividend /= candidate_factor;
        }
        else {
            candidate_factor += 1;
        }
    }

    return prime_factors
}
