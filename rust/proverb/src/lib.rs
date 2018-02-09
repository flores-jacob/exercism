pub fn build_proverb(list: Vec<&str>) -> String {

    if list.len() == 0{
        return String::from("");
    }

    let mut result_verse_list: Vec<String> = Vec::new();

    for index in 0.. list.len() -1 {
        result_verse_list.push(format!("For want of a {} the {} was lost.", list[index], list[index + 1]));
    }

    result_verse_list.push(format!("And all for the want of a {}.", list[0]));

    return String::from(result_verse_list.join("\n"))
}
