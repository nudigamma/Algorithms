# Scalar Multiplications
Implemented multiplications  from Algorithms Illuminated Part 1 (Roughgarden, Standford ) in Python. 

## Standard Multiplication  
to perform multiplication as taught in school , we perform n² multiplication and n² - n additions so we perform at maximum 2n² operations  ( assume you are doing a n * n multiplication and n = 4 . then take the maximum numbers
### Standard Multiplication Algorithm 
Coming soon

### Recursive Integer Multiplication  Algorithm 
input: two n-digit positive integers x and y  
output: the product of x.y  
Assumption: n is a power of 2 (even), and x and y have the same number of digits   
if n = 1 then  
    return x*y 
else 
    a,b := first and second half of x ,
    c,d:= first and second half y,
    recursively compute 
    ac := a*c  
    ad := a*d  
    bc := b*c  
    bd :=  b*d  
    return 10^n * ac + 10^(n/2) * (ad+bc) )+ bd

## Karatsuba multiplication 
Similar to the recursive multiplication algorithm above, but instead of computing recursively both ad and bc and then taking their sum in the last step, we recursively compute the multiplication (a+b)(c+d), then we subtract ac and bd to get the sum of bc +ad to use it directly in the last step  (Gauss's trick) 

### Kartsuba Multiplication Algorithm 
input: two n-digit positive integers x and y
output: the product of x and y
Assumption: n is a power of 2 ( even), x and y have the same number of digits  
if n = 1 then 
    return x*y    
else  
    a,b := first and second half of x 
    c,d = first and second half y 
    recursively compute  
    ac := a*c  
    a_d_b_c := (a+b)(c+d) 
    bd :=  b*d  
    ad_plus_bc = a_d_b_c - ac - bd  
    return 10^n * ac + 10^(n/2) * (ad_plus_bc )+ bd  

## General Karatsuba Multiplication 
The two algorithms above assume a 2^N number of digits. Both algorithms can be extended to handle an arbitrary number of digits ( odd and even ). The idea is to pad the number of digits with zeros  to the following 2^n number and then remove these zeros after the recursive multiplication happens. For example, if you want to multiply two numbers with nine digits each. First, you get the next 2^ n, which is 16 in this case, then pad the 9-digit numbers with ( 16 - 9 ) zeros. After the multiplication, remove 2*7 digits from the multiplication ( either by dividing ) or by converting the number to a string and trimming the excess zeros.  

## Python Implementation Notes :
### Note1:  Getting A, C, B, and D 
The general idea is to use integer division( //)  and the modulus operator(%); for example, if you want to split 1234 to 12 and 34   
a = 1234 // 10^(n/2) where n is the number of digits, will  give 12     
b = 1234 % 10^(n/2 ) where n is the number of digits, will give 34   
c = 4567 // 10^(n/2) where n is the number of digits, will  give 45     
d = 4567  % 10^(n/2 ) where n is the number of digits, will give 67   

### Note 2: Overflows in the number of digits computation 
You can use the int python type, which can take large numbers; otherwise, please ensure that the stored computation can be handled with the type. The zero padding can get large quickly. For example, the next 2*n for  several 17 digits is 32, which already overflows the double type. 
 
### Note 3: Does one less extra recursive call makes a difference?
One less recursive call saves almost 4 seconds on three hundred thousand runs.


### Note 4 : More efficient Implementation as suggested by Claude II 
Here are some ways the Karatsuba integer multiplication code could potentially be made more efficient:

Use a faster programming language like C/C++ instead of Python. Python has more overhead than lower-level languages.
Optimize the base case check. Instead of checking if n1 == 1, you could check if n1 <= some small cutoff value like 50 or 100 to switch to simple multiplication.
Unroll the first few layers of recursion. This avoids some function call overhead for small inputs.
Use fast integer math libraries for multiplication/addition instead of plain Python operators. Libraries like Numpy can speed up math operations.
Allocate result array once instead of creating new arrays at each recursion level. This reduces memory allocation overhead.
Limit recursion depth to avoid very deep recursion. At some point switch to schoolbook O(n^2) multiplication.
Store intermediate results to avoid recomputing. Trade memory for faster computation.
Optimize padding logic to minimize number of padding zeros required.
Precompute powers of 10 instead of computing them at each step.
Parallelize independent recursive calls. Multi-core CPUs can do steps in parallel.
Use Karatsuba only for large inputs and schoolbook method for smaller. Tune crossover point.
Implement FFT-based multiplication which is even faster for very large integers.
So in summary, there are many potential optimizations in data structures, algorithms, language choice, parallelism and careful tuning that could make Karatsuba integer multiplication much faster. The core algorithm is correct, but the implementation details can have a big impact on performanc