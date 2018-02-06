pub fn reply(message: &str) -> &str {

    // This is based on my previous python solution for this problem
    let stripped_message = message.trim();

    let question: bool = stripped_message.chars().last() == Some('?');

    // If there are any uppercase letters, and no lower case letters
    // This is not redundant, as we also have to deal with special chars
    // and whitespace
    let exclamation: bool = stripped_message.chars().any(|c| c.is_uppercase())
        && stripped_message.chars().all(|c| !c.is_lowercase());

    if stripped_message.is_empty() {
        "Fine. Be that way!"
    }else if question && exclamation {
        "Calm down, I know what I'm doing!"
    } else if exclamation {
        "Whoa, chill out!"
    }else if question {
        "Sure."
    }else{
        "Whatever."
    }
}
