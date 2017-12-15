#include <string>

namespace food_chain
{
    std::string form_bottom(int n){
        // maybe just have one return keyword at the bottom? I figured that this is more readable this way, and breaks are no longer necessary
        switch (n){
            case 1: return "I don't know why she swallowed the fly. Perhaps she'll die.\n";
            case 2: return "She swallowed the spider to catch the fly.\n" + form_bottom(n - 1);
            case 3: return "She swallowed the bird to catch the spider that wriggled and jiggled and tickled inside her.\n" + form_bottom(n - 1);
            case 4: return "She swallowed the cat to catch the bird.\n" + form_bottom(n - 1);
            case 5: return "She swallowed the dog to catch the cat.\n" + form_bottom(n - 1);
            case 6: return "She swallowed the goat to catch the dog.\n" + form_bottom(n - 1);
            case 7: return "She swallowed the cow to catch the goat.\n" + form_bottom(n - 1);
            case 8: return "";
        };
    };

    std::string verse(int n)
    {
        std::string top;
        switch(n){
            case 1 : top = "I know an old lady who swallowed a fly.\n";
                     break;
            
            case 2 : top = "I know an old lady who swallowed a spider.\n"
                           "It wriggled and jiggled and tickled inside her.\n";
                     break;

            case 3: top = "I know an old lady who swallowed a bird.\n"
                          "How absurd to swallow a bird!\n";
                    break;

            case 4: top = "I know an old lady who swallowed a cat.\n"
                          "Imagine that, to swallow a cat!\n";
                    break;
            case 5: top = "I know an old lady who swallowed a dog.\n"
                          "What a hog, to swallow a dog!\n";
                    break;
            case 6: top = "I know an old lady who swallowed a goat.\n"
                          "Just opened her throat and swallowed a goat!\n";
                    break;
            case 7: top = "I know an old lady who swallowed a cow.\n"
                          "I don't know how she swallowed a cow!\n";
                    break;
            case 8: top = "I know an old lady who swallowed a horse.\n"
                          "She's dead, of course!\n";
                    break;
        };

        return top + form_bottom(n);
    };

    std::string verses(int n, int m)
    {
        std::string multiple_verses;
        for (int i=n; i<=m; i++){
            multiple_verses += verse(i);
            multiple_verses += "\n";
        };
        return multiple_verses;
    };

    std::string sing(){
        return verses(1,8);
    };
};
