// Solution adapted from earlier C++ implentation

pub fn nth(n: i32) -> Result <i32, &'static str>{
        if n == 0{
            return Err("must request at least the first prime number");
        };

        let mut discovered_primes: Vec<i32> = Vec::new();

        let mut current_int:i32 = 2;

        let mut divisible:bool;

        // while we have not yet discovered up to n prime numbers
        while discovered_primes.len() < n as usize{
            // assume that current int is not divisible
            divisible = false;
            // we loop through each of the primes we have already discovered
            for &prime in &discovered_primes{
                // we check if the current int in question is divisible by any of the already discovered ones
                if current_int % &prime == 0{
                    divisible = true;
                    // if it is divisible, then we increase the int count by one
                    current_int += 1;
                    // and we move on to the next item in the while loop
                    break;
                }
            };
            // if current int is not divisible by any of the previously discovered primes
            // then we add it to the discovered primes vector, and increase current_prime_count by one
            if divisible == false{
                discovered_primes.push(current_int);
            };
        };

        return Ok(discovered_primes[discovered_primes.len() -1]);
}
