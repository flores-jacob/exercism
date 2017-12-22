#include <string>

namespace beer
{

    std::string verse_one = "";
    std::string verse_generic = "8 bottles of beer on the wall, 8 bottles of beer.\n"
        "Take one down and pass it around, 7 bottles of beer on the wall.\n";

    std::string generate_generic_verse(int verse_number)
    {
        return std::to_string(verse_number)
         + " bottles of beer on the wall, "
         + std::to_string(verse_number)
         + " bottles of beer.\n"
         + "Take one down and pass it around, "
         + std::to_string(verse_number - 1)
         + " bottles of beer on the wall.\n";
    };

    std::string verse(int verse_number)
    {
        std::string song;

        if (verse_number == 0){
            song = "No more bottles of beer on the wall, no more bottles of beer.\n"
        "Go to the store and buy some more, 99 bottles of beer on the wall.\n";
        }else if (verse_number == 1){
            song = "1 bottle of beer on the wall, 1 bottle of beer.\n"
        "Take it down and pass it around, no more bottles of beer on the wall.\n";
        }else{
            song = generate_generic_verse(verse_number);
        }

        return song;
    };

}