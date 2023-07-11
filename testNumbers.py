''''''

import numpy as np

for number in np.arange(1,62):

    next_power_of_two = 2**np.ceil(np.log2(number))    
    print({number}, {next_power_of_two})
    print(f"Mutliplication factor {10**(next_power_of_two - number)}")
    