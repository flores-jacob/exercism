namespace grains
{
    unsigned long long int square(int square_number)
    {
        unsigned long long int grains_in_square = 1;

        for (int i=2; i<=square_number; i++){
            grains_in_square = grains_in_square * 2;
        };

        return grains_in_square;
    };

    unsigned long long int total()
    {
        unsigned long long int total = 0;
        for (int i=1; i<=64; i++)
        {
            total += square(i);
        };
        return total;
    };
};
