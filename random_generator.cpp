/**
 * First, include the <random> header at the top of your code to make the std::random_device, std::mt19937, 
 * and std::uniform_int_distribution classes available.

Next, create an instance of std::random_device and 
use it to seed a random number generator (RNG) such as std::mt19937.

Then, use std::uniform_int_distribution to generate 
a random size for your vector. You can specify the minimum 
and maximum size values as parameters to the std::uniform_int_distribution constructor.
Once you have a random size for your vector, you can 
use a loop to generate random elements and add them to the vector.
 To generate a random element, you can use 
 std::uniform_int_distribution again, this time specifying 
 the minimum and maximum values for
 the random element as parameters.
*/

#include <iostream>
#include <vector>
#include <random> // for random_device, mt19937, and uniform_int_distribution

int main()
{
    // Create a random number generator and seed it with a random device
    std::random_device randomDevice;
    std::mt19937 rng(randomDevice());

    // Generate a random size for the vector
    std::uniform_int_distribution<int> vectorSizeDist(1, 10);
    int vectorSize = vectorSizeDist(rng);

    // Create a vector and fill it with random elements
    std::vector<int> randomVector;
    std::uniform_int_distribution<int> elementDist(-10, 10);
    for (int i = 0; i < vectorSize; ++i) {
        randomVector.push_back(elementDist(rng));
    }

    // Print the vector to verify its contents
    std::cout << "Random vector:" << std::endl;
    for (int element : randomVector) {
        std::cout << element << " ";
    }
    std::cout << std::endl;

    return 0;
}

#include <iostream>
#include <vector>
#include <ranges> // for ranges and range algorithms

int main()
{
    // Create a vector of integers
    std::vector<int> numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

    // Create a range object that represents the entire vector
    auto numbersRange = std::ranges::make_range(std::ranges::begin(numbers), std::ranges::end(numbers));

    // Use the filter algorithm to create a range of only the even numbers
    auto evenNumbersRange = std::ranges::filter(numbersRange, [](int x) { return x % 2 == 0; });

    // Use the transform algorithm to create a range of the square of each even number
    auto squaredEvenNumbersRange = std::ranges::transform(evenNumbersRange, [](int x) { return x * x; });

    // Print the elements of the final range to verify the results
    std::cout << "Squared even numbers:" << std::endl;
    for (int element : squaredEvenNumbersRange) {
        std::cout << element << " ";
    }
    std::cout << std::endl;

    return 0;
}