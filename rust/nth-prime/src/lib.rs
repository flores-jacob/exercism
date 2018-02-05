pub fn nth(n: i32) -> Result <i32, &'static str>{
        if n == 0{
            return Err("must request at least the first prime number");
        };

        let mut discovered_primes: Vec<i32> = Vec::new();

        let mut current_int:i32 = 2;

        // while we have not yet discovered up to n prime numbers
        while discovered_primes.len() < n as usize{

            // if the current integer is not divisible by any of the
            // previously discovered prime numbers, then it is prime
            if !discovered_primes.iter().any(|&p| current_int % p == 0){
                discovered_primes.push(current_int)
            };
            current_int += 1;
        };
        // return the last prime discovered
        return Ok(discovered_primes[discovered_primes.len() -1]);
}
