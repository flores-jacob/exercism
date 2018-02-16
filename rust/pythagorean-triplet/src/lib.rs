// More readable solution, without the type wrangling
pub fn find() -> Option<u32> {
    for a in 2..500{
        for b in 2..500{
            let c = 1000 - a - b;
            if a * a + b * b == c * c {
                return Some(a * b * c)
            }
        }
    }
    return None
}
