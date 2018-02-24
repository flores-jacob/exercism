#include <vector>
#include <stdexcept>
#include <ctime>
#include <iostream>
#include <cmath>

namespace prime
{
    int nth (int nth_prime){
        if (nth_prime == 0){
            throw std::domain_error("must request at least the first prime number");
        };

//        std::vector<int> discovered_primes = {2};
//
//        int current_int = 3;
//
//        // while we have not yet discovered up to n prime numbers
//        while (discovered_primes.size() < nth_prime){
//            // assume that current int is not divisible
//            bool divisible = false;
//            // we loop through each of the primes we have already discovered
//            for (int prime: discovered_primes){
//                // we check if the current int in question is divisible by any of the already discovered ones
//                if ((current_int >= prime) && (current_int % prime == 0)){
//                    divisible = true;
//                    // if it is divisible, then we increase the int count by one
//                    current_int += 2;
//                    // and we move on to the next item in the while loop
//                    break;
//                }
//            };
//            // if current int is not divisible by any of the previously discovered primes
//            // then we add it to the discovered primes vector
//            if (divisible == false){
//                discovered_primes.push_back(current_int);
//            };
//        };
//
//        return discovered_primes.back();

        int int_containing_prime_est;

        if (nth_prime < 6){
            // the 6th prime is 13, so we just get values beneath that
            int_containing_prime_est = 12;
        }else{
            // estimate lifted from https://primes.utm.edu/howmany.html
            int_containing_prime_est  = nth_prime * (std::log(nth_prime) + std::log(std::log(nth_prime - 1)));
        }

        // Initialize a vector assuming all numbers are primes
        std::vector<bool> is_prime(int_containing_prime_est, true);

        // The first element which maps to 1 is tagged to be not prime
        is_prime.at(0) = false;

        // Mark multiples of each number as not prime
        for (int i=2; i <=int_containing_prime_est - 1; i++){
            for (int p=i + i; p <= int_containing_prime_est; p+=i ){
                is_prime.at(p - 1) = false;
            };
        };

        // count up to the nth prime and return the corresponding value
        int prime_count = 0;
        for (int k=0; k<int_containing_prime_est; k++){
            if (is_prime.at(k) == true){
                prime_count++;
                if (prime_count >= nth_prime){
                    return k + 1;
                };
            };
        };

    };

    int test_speed(){

        std::clock_t start;
        start = std::clock();

        for(int i=0; i<20; i++){
            nth(10001);
        };

        std::cout << "Time: " << (std::clock() - start) / (double)(CLOCKS_PER_SEC / 1000) << " ms" << std::endl;

        return 0;

    };
};