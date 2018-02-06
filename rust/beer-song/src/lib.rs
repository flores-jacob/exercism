// This is based on the C++ solution I used earlier


fn generate_generic_verse(n: i32) -> String {
    return format!("{} bottles of beer on the wall, {} bottles of beer.\n\
     Take one down and pass it around, {} bottles of beer on the wall.\n", n, n, n-1 );
}


pub fn verse(n: i32) -> String {
    let mut song = String::new();

    if n == 0{
        song = String::from("No more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall.\n")
    }else if n == 1{
        song = String::from("1 bottle of beer on the wall, 1 bottle of beer.\nTake it down and pass it around, no more bottles of beer on the wall.\n")
    }else if n == 2{
        song = String::from("2 bottles of beer on the wall, 2 bottles of beer.\nTake one down and pass it around, 1 bottle of beer on the wall.\n")
    }else{
        song = generate_generic_verse(n)
    }

    return song

}

pub fn sing(start: i32, end: i32) -> String {

    let mut song = String::new();

    for n in (end..start + 1).rev(){
        song.push_str(&verse(n));
        if n != end {
            song.push_str("\n");
        };
    };

    return song;

}
