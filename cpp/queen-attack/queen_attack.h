#include <utility>

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
    };

    chess_board::chess_board()
    {
        white_pos = std::make_pair(0, 3);
        black_pos = std::make_pair(7, 3);
    };
    chess_board::chess_board(std::pair<int, int> white_pos_in, std::pair<int, int> black_pos_in)
    {
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

}