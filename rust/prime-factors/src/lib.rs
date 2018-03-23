pub fn factors(n:i64) -> Vec<i64>{

    let mut prime_factors:Vec<i64> = vec![];

    let mut current_num: i64 = n;

    for divisor in 2..n + 1 {
        if current_num % divisor == 0 {
            prime_factors.push(divisor);
            current_num = current_num/divisor;

            println!("factors are {:?}", prime_factors);
        }

    };

    return prime_factors
}
