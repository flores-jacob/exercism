namespace squares
{
    int square_of_sums(int n){
        int result = 0;
        for (int i=0; i<=n; i++){
            result += i;
        };
        result = result * result;
        return result;
    };

    int sum_of_squares(int n)
    {
        int result = 0;
        for (int i=0; i<=n; i++){
            result += (i * i);
        };
        return result;
    };
    int difference(int n){
        return square_of_sums(n) - sum_of_squares(n);
    };
}
