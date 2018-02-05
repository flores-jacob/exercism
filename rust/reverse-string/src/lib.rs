pub fn reverse(inputs: &str) -> String {
    // Solution lifted from https://stackoverflow.com/a/38083610
    return inputs.chars().rev().collect::<String>();
}
