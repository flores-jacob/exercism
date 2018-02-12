// Adapted from my python solution to this problem
pub fn sum_of_multiples(limit: u32, factors: &[u32]) -> u32 {
    if factors.is_empty() {
        return 0
    }else {
        let mut multiple_sum:u32 = 0;

        for i in 1..limit {
            for factor in factors {
                if (i % factor) == 0 {
                    multiple_sum += i;
                    break;
                }
            }
        }
        return multiple_sum
    }
}
