pub fn factors(n:i64) -> Vec<i64>{

    let mut prime_factors:Vec<i64> = vec![];

    let mut input: i64 = n;

    for divisor in 2..n + 1 {
        if input % divisor == 0 {
            prime_factors.push(divisor);
            input = input/divisor;
            // recursively get factors of updated input
            prime_factors.extend(factors(input));
            break;
        };
    };

    return prime_factors
}
