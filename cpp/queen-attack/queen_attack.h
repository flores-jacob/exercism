#include <utility>
#include <stdexcept>

namespace queen_attack
{
    class chess_board
    {
        private:
            std::pair<int, int> white_pos;
            std::pair<int, int> black_pos;
        public:
            chess_board();
            chess_board(std::pair<int, int> white_pos_in, std::pair<int, int> black_pos_in);
            std::pair<int, int> white() const;
            std::pair<int, int> black() const;

            operator std::string() const;
    };

    chess_board::chess_board()
    {
        white_pos = std::make_pair(0, 3);
        black_pos = std::make_pair(7, 3);
    };
    chess_board::chess_board(std::pair<int, int> white_pos_in, std::pair<int, int> black_pos_in)
    {
        if (white_pos_in == black_pos_in){
            throw std::domain_error("positions should not be identical");
        };

        white_pos = white_pos_in;
        black_pos = black_pos_in;
    };

    std::pair<int, int> chess_board::white() const
    {
        return white_pos;
    };

    std::pair<int, int> chess_board::black() const
    {
        return black_pos;
    };

    chess_board::operator std::string() const
    {
        std::string chess_board_string;

        for(int i=0; i<8; i++){
            for (int k=0; k<8; k++){
                if (i == white_pos.first && k == white_pos.second){
                    chess_board_string += "W";
                }else if (i == black_pos.first && k == black_pos.second){
                    chess_board_string += "B";
                }else{
                    chess_board_string += "_";
                };
                if (k < 7){
                    chess_board_string += " ";
                };
            };
            chess_board_string += "\n";
        };

        return chess_board_string;
    };

}