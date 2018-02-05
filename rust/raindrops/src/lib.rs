// Solution is adapted from my previous C++ code. Open to corrections,
// especially regarding whether or not code is idiomatic Rust

pub fn raindrops(n: usize) -> String {
    let mut constructed_string = String::from("");

    if n % 3 == 0{ constructed_string += "Pling"; };
    if n % 5 == 0{ constructed_string += "Plang"; };
    if n % 7 == 0{ constructed_string += "Plong"; };

    if (constructed_string.is_empty()){
        constructed_string = n.to_string();
    };

    return constructed_string;
}
