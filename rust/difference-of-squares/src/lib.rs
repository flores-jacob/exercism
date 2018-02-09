pub fn square_of_sum(n: usize) -> usize {
    let mut total: usize = 0;
    for i in 1 .. n + 1{
        total += i;
    }

    return total.pow(2)
}

pub fn sum_of_squares(n: usize) -> usize {
    let mut total: usize = 0;
    for i in 1 .. n + 1{
        total += i.pow(2);
    }

    return total
}

pub fn difference(n: usize) -> usize {
    return square_of_sum(n) - sum_of_squares(n)
}
