#include <string>

namespace beer
{

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
        }else if (verse_number == 2){
            song = "2 bottles of beer on the wall, 2 bottles of beer.\n"
        "Take one down and pass it around, 1 bottle of beer on the wall.\n";
        }else{
            song = generate_generic_verse(verse_number);
        }

        return song;
    };

    std::string sing (int verse_start, int verse_end)
    {
        std::string song;

        for (int i=verse_start; i >= verse_end; i--){
            song += verse(i);
            if (i != verse_end){
                song += "\n";
            };
        };

        return song;

    };

    std::string sing(int verse_start){
        return sing(verse_start, 0);
    };


}