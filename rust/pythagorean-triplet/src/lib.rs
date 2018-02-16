pub fn find() -> Option<u32> {
    for a in 2i32..500{
        for b in 2i32..500{
            let c_squared:i32 = a.pow(2u32) + b.pow(2u32);
            let c:f64 = (c_squared as f64).sqrt();
            if c == c.round(){
                if a + b + (c as i32) == 1000{
                    return Some((a * b * (c as i32)) as u32)
                }
            }
        }
    }
    return None
}
